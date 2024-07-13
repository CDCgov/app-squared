# APPSquared 
## Antigenic Prediction from Protein Sequences Pipeline 
![APPSquared](https://github.com/nicolepaterson/APPSquared/blob/main/pipeline.png)

Heightened rates of evolution are observed at host:pathogen interfaces due to the high stakes of the interaction.
This is referred to in the field colloquially as evolutionary "molecular arms races" between a pathogen and the host it infects.
For influenza, the key players in this interaction are the influenza hemagglutinin receptor, host sialic acid isomers on the cell surface (which for some exhibit species-specific tropism), and antibodies whose binding strength, specificity and proximity to the receptor binding site are important determinants for how effectively the host neutralizes them. 
For this reason, mutations in the influenza receptor are closely monitored for public health purposes to ensure sufficient mutation in the influenza hemagglutinin has not occurred to result in lack of recognition by host antibodies, a phenomenon known as antigenic drift.
A commonly used method of quantifying antigenic drift is antigenic cartography, which charts distance between variants across a conceptual topology. This method is not particularly agile or simple to perform nor can it predict future phenotypes. As a result other methods for ranking antigenic drift have been explored recently with the rise and ubiquity of machine learning.

This pipeline was developed to generate datasets that include structural information from high frequency variant sequences 
*and* variants that are either not available at CDC or unable to be cultured in the laboratory.

This pipeline relies on the following open source programs:
- Rosetta <https://www.rosettacommons.org/software>
- Getcontacts <https://github.com/getcontacts/getcontacts>

Bespoke CDC code written by Dr. Nicholas Kovacs and Dr. Brian Mann.
- Structural distance calculator for generating fitness landscapes <https://git.biotech.cdc.gov/hxa6/fit_landscape>
- Glycosylation distance calculator

This pipeline generates biophysical information on each structure and includes the following, in addition to more granular features :
- Rosetta Energy Scores, total and per-residue (a measure of relative stability of protein in question)
- Root mean square difference - RMS (a scoring of the deviation in alignment between the protein and a reference structure)
- Relative surface accessibility per residue

To generate the structural distance values, please refer to the repo cited or contact the maintainer.

usage for running on scicomp in biolinux:

```
cd /path/to/pdb/files
bash /path/to/repo/BCH relax
``` 
```
cd /path/to/pdb/files
bash /path/to/repo/BCH tables
```
```
cd /path/to/pdb/files
bash /path/to/repo/BCH upload
```

set up necessary conda  environments: 
```
conda env create --name glyc --file=glyc.yaml
conda env create --name getcontacts --file=getcontacts.yaml
```

set up getcontacts library:
```
git clone https://github.com/getcontacts/getcontacts.git 
echo "export PATH=`pwd`/getcontacts:\$PATH" >> ~/.bashrc source ~/.bashrc
```
## Public Domain Standard Notice
This repository constitutes a work of the United States Government and is not subject to domestic copyright protection under 17 USC § 105. This repository is in the public domain within the United States, and copyright and related rights in the work worldwide are waived through the CC0 1.0 Universal public domain dedication. All contributions to this repository will be released under the CC0 dedication. By submitting a pull request you are agreeing to comply with this waiver of copyright interest.

## License Standard Notice
The repository utilizes code licensed under the terms of the Apache Software License and therefore is licensed under ASL v2 or later.

This source code in this repository is free: you can redistribute it and/or modify it under the terms of the Apache Software License version 2, or (at your option) any later version.

This source code in this repository is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the Apache Software License for more details.

## Privacy Standard Notice
This repository contains only non-sensitive, publicly available data and information. All material and community participation is covered by the Disclaimer and Code of Conduct. For more information about CDC's privacy policy, please visit http://www.cdc.gov/other/privacy.html.

## Contributing Standard Notice
Anyone is encouraged to contribute to the repository by forking and submitting a pull request. (If you are new to GitHub, you might start with a basic tutorial.) By contributing to this project, you grant a world-wide, royalty-free, perpetual, irrevocable, non-exclusive, transferable license to all users under the terms of the Apache Software License v2 or later.

All comments, messages, pull requests, and other submissions received through CDC including this GitHub page may be subject to applicable federal law, including but not limited to the Federal Records Act, and may be archived. Learn more at http://www.cdc.gov/other/privacy.html.

## Records Management Standard Notice
This repository is not a source of government records, it is to increase collaboration and collaborative potential. All government records will be published through the CDC web site.

## Additional Standard Notices
Please refer to CDC's Repository for more information about contributing to this repository, public domain notices and disclaimers, and code of conduct.

@patersonnicole
@kovacsnicholas
@mannbrian
