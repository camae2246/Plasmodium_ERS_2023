# Script for getting the subtelomeric and internal young regions
# Subtelomeric: Choose telomere window
# Internal: Choose internal window

# Input file example: Pf3D_database.txt
# Input file format: based on Pf3D_freqs4maps.csv (example included) obtained with PhyloChromoMap
# Input file with information of presence of gene families per intervals of chr
# A gene family is present if it is in more than 0.25 minor clades per major

# Change database path file to where your input file is located
#database = File.open('/Users/marioceron/Documents/plasmodium/map/subtelomeres/database_or.txt', 'r')
database = File.open('/Users/camae/Thesis/Input_RbScript/database/Pf3D_database.txt', 'r')
database = database.readlines()
#chrs = ["pf01", "pf02", "pf03", "pf04", "pf05", "pf06", "pf07", "pf08", "pf09", "pf10", "pf11", "pf12", "pf13", "pf14"]
chrs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]

print "telomere window (t) or internal window (i): "
answer = gets
print answer

#-------------------------
# window for sub-telomeres
#-------------------------

if answer =~ /t/    
    chrs.each do |chr|
        chr_pos = Array.new
        chrreb_pos = Array.new
        inter = Array.new
        database.each do |line|
            line = line.gsub(/$\n/, "")
            line = line.split("\t")
            mc = line[17]
#            mc = line[27]
            if mc.to_i >= 3
                if line[1] == chr
                    chr_pos.push(line[2])
                end            
            end
        end
        database_reb = database.reverse
        database_reb.each do |line|
            line = line.gsub(/$\n/, "")
            line = line.split("\t")
#            mc = line[27]
            mc = line[17]
            if mc.to_i >= 3
                if line[1] == chr
                    chrreb_pos.push(line[3])
                end            
            end
            
            if line[1] == chr
            	inter.push(line[2])
            end
            	
        end
#         print chr + "\t" + chr_pos[0] + "\t" + chr_pos[1] + "\t" + chrreb_pos[0] + "\t" + chrreb_pos[1] + "\n"
        print chr + ",1," + chr_pos[1] + "," + chrreb_pos[1] + "," + inter[0] + "\n"
    end
else
    
#----------------------------
# window for internal regions
#----------------------------

    if answer =~ /i/
        chrs.each do |chr|
            positionsWindows = Array.new
            
            #---------------------------------------------------------------------------------
            # The database contains all info for all chromosomes. So for every chr we need to
            # read the database
            #---------------------------------------------------------------------------------
            
            database.each do |line|               
                line = line.gsub(/$\n/, "")
                line = line.split("\t")
                subset = Array.new
                if line[1] == chr
                    
                    # ------------------------------------------------------------------------------
                    # For every chr we are going to take every locus and set it as initial position
                    # for the window. For every initial position we are going to increase the window by
                    # adding the line of every next locus. We are going to increase the indow until 
                    # 250000. <--- This is the main process (explained later)
                    #
                    # The variable positionsWindows will contain the first and the last loci of the
                    # window. We should consider these to points:
                    #
                    # 1. In the future lines we will have a window already set. So, for the next window
                    # we need to set position A to be after the last position of the past window.
                    # The problem is when there is not a previous window. In that case we should set lastPosB
                    # to zero.
                    #
                    # 2. For increasing the window we are appending lines from the database. But,
                    # the database contains lines for every chr. So, we should restrict to read only
                    # the lines of the current chr.
                    # -------------------------------------------------------------------------------
                    
                    positionA = line[2].to_i
                    
                    genesInter = 0    # <-- This variable will count conserved genes inside our current window.
                                      #     This is important for our criterion. So, in every new window the variable
                                      #     should be initialized to zero.
                    
                    # Solving point 1:
                    
                    if (positionsWindows.length) == 0
                        lastPosB = 0
                    else
                        lastPosB = positionsWindows[-1].split("\t")[1].to_i
                    end
                    
                    if positionA > lastPosB                           
                        database.each do |lineforSub|
                            linefS = lineforSub.gsub(/\n/, "")
                            linefS = linefS.split("\t")
                            
                            if linefS[1] == chr   # Here we solved point 2
                                
                                if linefS[2].to_i > positionA    # <--- Main process
                                    if (linefS[3].to_i - positionA) <= 200000 # <-- Main process
                                        
                                        #---------------------------------------------------------------
                                        # While we are increasing the window, we need to check the OGs
                                        # and collect how many 'mc' they have. Count the ones that have
                                        # more than 3 mc.
                                        #
                                        # The variable genesInter contains how many OGs with more than 3 mc
                                        # are in the current window. We set this script to stop increasing
                                        # the window if there are more than 1 OGs with more than 3 mc
                                        # --------------------------------------------------------------                                        
                                        
                                        if linefS[10] =~ /OG/
#                                            mc = linefS[27]   # only count MC when it has at least 25% of the mcs. 
                                            mc = linefS[17]   # only count MC when it has at least 25% of the mcs.                                             
#                                            puts "mc: " + mc
                                            if mc.to_i >= 3
                                                genesInter += 1
                                            end
                                        end
                                        
                                        # When the program is collecting lines (from the database) for increasing
                                        # the window, it is going to find one that contains an OG with more than
                                        # 3 mc. Then it adds 1 to genesInter. That line meets the conditional
                                        # 'genesInter <= 1'. When this occures again, genesInter will be 2 and
                                        # and it will not meet the conditinal. Here the window stops increasing. BUT,
                                        # genesInter can continue increasing because the program needs to read
                                        # 250.000 lines.
                                        #
                                        # As, this is a loop, the next window will be from the last locus of the last
                                        # window (see next comments) and genesInter will be initialized to zero.
                                        #-----------------------------------------------------------------

                                        if genesInter <= 1
                                            subset.push(lineforSub)
                                        end
                                    end
                                end
                            end
                        end
                        
                        #------------------------------------------------------------------------
                        # We already have a window with 0 or 1 OG that contains 3 or more mc.
                        # Now we need to consider the current window only if it is bigger than
                        # 69999. For doing this, we collect the fist and last locus of the window
                        # and calculate the difference between them.
                        #-------------------------------------------------------------------------
                        
                        firsPosA = subset[0].split("\t")[2].to_i
                        lastPosB = subset[-1].split("\t")[3].to_i
                        positionsWindows.push(firsPosA.to_s + "\t" + lastPosB.to_s)
                        
                        # FOR DEBUGGING --- If the window is bigger than 69999 (or your minimum window size for young region report), then we print all the lines of the window                        
                        #if (lastPosB-firsPosA) >= 69999
                        #    subset.each do |lineSub|
                        #        print lineSub
                        #    end
                        #end

                    end
                end
                
                # In this part of the process we should have a window. All variables 
                # should will be initialized for the next window.
                
            end
            
            # In this point all windows for a chr should have been collected. The variable positionsWindows
            # have the location info. This varible will be null for the next chr. So, firsPosA and lastPosB
            # will be also initialized.
            
#             print("\n")
#             puts "all windows of chr " + chr + ":"
#             for i in positionsWindows
#                 
#                 puts i
#             end
            
#             puts "windows bigger than 89kbp:"
            for i in positionsWindows
                if i.split("\t")[1].to_i - i.split("\t")[0].to_i >= 19999
#                     puts i
                    puts  chr + "," + i.split("\t")[0] + "," + i.split("\t")[1]
                end
            end
            
#             puts "end of chr (" + chr + ")\n"
            
        end
    else
        print "run again and choose t or i and press return\n"
    end
end