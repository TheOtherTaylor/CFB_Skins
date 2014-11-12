import re;

def processFile(inputFileName, outputFileName, lineProcessFunction):
	# Some regex's to help when processing.
	preprocessorDefinition = re.compile('class [\w]+;');
	classNameRegex = re.compile('class ([\w]+) : [\w]+');
	
	# Open the file and process it
	with open(inputFileName, 'r') as inputFile:
		with open(outputFileName, 'w') as outputFile:
			outputFile.write("// This file is automatically generated from '" + inputFileName + "'.\n// Do not hand-edit.\n\n");
			currentClassName = "";
			indentDepth = 0;
			for line in inputFile:
				shouldBeCommentedOut = False;
				if preprocessorDefinition.match(line):
					shouldBeCommentedOut = True;
				classNameMatch = classNameRegex.match(line);
				if (classNameMatch):
					currentClassName = classNameMatch.group(1);
				
				if "{" in line:
					indentDepth += 1;
				if "}" in line:
					indentDepth -= 1;
				
				if (not shouldBeCommentedOut):
					line = lineProcessFunction(line, currentClassName, indentDepth);
					
				if shouldBeCommentedOut:
					outputFile.write("// ");
				outputFile.write(line);

# Define some functions for processing lines
def processUnitLines(line, currentClassName, indentDepth):
	# Transform the base class name from a TW solder to a AR soldier
	line = line.replace("CFB_TW_Soldier", "CFB_AR_Soldier");
	
	# Change the base vehicle class so they show up in the AR section
	line = line.replace("CFB_TW_VehicleClass", "CFB_AR_VehicleClass");
	
	# Map the uniforms from TW -> AR. Also make sure the skin file is selected correctly.
	line = line.replace("CFB_TW_Uniform", "CFB_AR_Uniform");
	line = line.replace("CFB_TW_Rolled_Uniform", "CFB_AR_Rolled_Uniform");
	line = line.replace("CFB_TW_Tshirt_Uniform", "CFB_AR_Rolled_Uniform");
	line = line.replace("\cfb_skins\CADPAT_TW_Uniform_NATO.paa", "\cfb_skins\CADPAT_AR_Uniform_NATO.paa");
	
	# Change some of the equipment the unit starts with
	line = line.replace("NVGoggles_INDEP", "NVGoggles");
	line = line.replace("CFB_TW_Helmet", "CFB_AR_Helmet");
	line = line.replace("CFB_TW_Boonie", "CFB_AR_Helmet");
	line = line.replace("CFB_TW_Patrol", "CFB_AR_Helmet");
	line = line.replace("CFB_TW_Backpack", "CFB_AR_Backpack");
	line = line.replace("CFB_TW_Vest_Tactical", "CFB_AR_Vest_Tactical");
	line = line.replace("CFB_TW_Vest_PlateCarrier1", "CFB_AR_Vest_PlateCarrier1");
	line = line.replace("CFB_TW_Vest_PlateCarrier2", "CFB_AR_Vest_PlateCarrier2");
	
	# Change the weapons to silenced versions
	# line = line.replace("CFB_MX_Black_MRCO", "arifle_MX_ACO_pointer_snds_F");
	# line = line.replace("CFB_MXM_Black_SOS", "arifle_MXM_RCO_pointer_snds_F");
	# line = line.replace("CFB_MX_GL_Black_MRCO", "arifle_MX_GL_Holo_pointer_snds_F");
	# line = line.replace("CFB_MXC_Black_MRCO", "arifle_MXC_Holo_pointer_snds_F");

	return line;

def processGroupLines(line, currentClassName, indentDepth):
	# Transform the base class name from TW groups to JTF2 groups
	line = line.replace("CFB_Groups_CADPAT_TW", "CFB_Groups_AR");
	
	# Change the section names
	line = line.replace("Infantry (CADPAT TW)", "Infantry (CADPAT AR)");
	
	# Change the names of the units
	line = line.replace("CFB_TW_Soldier", "CFB_AR_Soldier");
	return line;

def processBackpackLines(line, currentClassName, indentDepth):
	# For each TW backpack generate a AR backpack that is identical
	line = line.replace("CFB_TW_Backpack", "CFB_AR_Backpack");
	
	# Replace the texture as well.
	line = line.replace("CADPAT_TW_Backpack", "CADPAT_AR_Backpack");
	
	#Replace the description
	line = line.replace("CADPAT TW", "CADPAT AR");
	return line;

def processHeadgearLines(line, currentClassName, indentDepth):
	# For each TW headgear generate a AR headgear that is identical
	line = line.replace("CFB_TW_", "CFB_AR_");
	
	#update the descriptions from "CADPAT TW XXX" to "CADPAT AR XXX"
	line = line.replace("CADPAT TW", "CADPAT AR");
	
	#Update the texture names from "CADPAT_TW_XXX" to "CADPAT_AR_XXX"
	line = line.replace("CADPAT_TW_", "CADPAT_AR_");
	return line;

def processUniformsLines(line, currentClassName, indentDepth):
	# For each TW uniform generate a AR uniform that is identical
	line = line.replace("CFB_TW_", "CFB_AR_");
	
	#update the descriptions from "CADPAT TW XXX" to "CADPAT AR XXX"
	line = line.replace("CADPAT TW", "CADPAT AR");
	
	#Update the texture names from "CADPAT_TW_XXX" to "CADPAT_AR_XXX"
	line = line.replace("CADPAT_TW_", "CADPAT_AR_");
	return line;

def processVestsLines(line, currentClassName, indentDepth):
	# For each TW vest generate a AR vest that is identical
	line = line.replace("CFB_TW_", "CFB_AR_");
	
	#update the descriptions from "CADPAT TW XXX" to "CADPAT AR XXX"
	line = line.replace("CADPAT TW", "CADPAT AR");
	
	#Update the texture names from "CADPAT_TW_XXX" to "CADPAT_AR_XXX"
	line = line.replace("CADPAT_TW_", "CADPAT_AR_");
	return line;

processFile("../src/@CFB_Skins/addons/cfb_skins/vehicles_units_tw.hpp", "../src/@CFB_Skins/addons/cfb_skins/vehicles_units_ar.hpp", processUnitLines);
processFile("../src/@CFB_Skins/addons/cfb_skins/groups_tw.hpp", "../src/@CFB_Skins/addons/cfb_skins/groups_ar.hpp", processGroupLines);
processFile("../src/@CFB_Skins/addons/cfb_skins/vehicles_backpacks_tw.hpp", "../src/@CFB_Skins/addons/cfb_skins/vehicles_backpacks_ar.hpp", processBackpackLines);
processFile("../src/@CFB_Skins/addons/cfb_skins/weapons_headgear_tw.hpp", "../src/@CFB_Skins/addons/cfb_skins/weapons_headgear_ar.hpp", processHeadgearLines);
processFile("../src/@CFB_Skins/addons/cfb_skins/weapons_uniforms_tw.hpp", "../src/@CFB_Skins/addons/cfb_skins/weapons_uniforms_ar.hpp", processUniformsLines);
processFile("../src/@CFB_Skins/addons/cfb_skins/weapons_vests_tw.hpp", "../src/@CFB_Skins/addons/cfb_skins/weapons_vests_ar.hpp", processVestsLines);
