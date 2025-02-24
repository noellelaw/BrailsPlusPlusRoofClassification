from brails.processors.vlm_image_classifier.CLIPClassifier import CLIPClassifier
from typing import Optional

class RoofMaterialLLM(CLIPClassifier):

        """
        The BuildingMaterialLLM classifier attempts to predict building materials  using large language models.

        Variables
        
        Methods:
        predict(ImageSet): To return the predictions for the set of images provided

        """
        
        def __init__(self, input_dict: Optional[dict] =None):
            
            """
            The class constructor sets up the path prompts or whatever.
            
            Args
                input_data: dict Optional. The init function looks into dict for values needed, e.g. path to prompts
            """
            super().__init__(input_dict = input_dict)
            self.input_dict = input_dict
            if(self.input_dict!=None):
                self.text_prompts = self.args['prompts']
                self.classes = self.args['classes']
            else:
                self.text_prompts = [
                    'thatch, in which tatch elements look very small and semi-ridged',
                    'green vegetation, in which green elements look small and non-uniform',
                    'limestone slates, in which limestone elements look small and ridged',
                    'stone slates, in which stone elements look small and ridged',
                    'clay tiles, in which clay elements look small and ridged',
                    'asphalt tiles, in which asphalt elements look small and ridged',
                    'concrete tiles, in which concrete elements look small and ridged',
                    'wood tiles, in which wood elements look small and ridged',
                    'metal sheet materials, in which metal elements look large and ridged or corrugated with vertical and horizontal overlaps or laid in large panels',
                    'polycarbonate sheet materials, in which polycarbonate elements look large and ridged or corrugated with vertical and horizontal overlaps or laid in large panels, and are clear or painted',
                    'glass sheet materials, in which glass elements look large and ridged or corrugated with vertical and horizontal overlaps or laid in large panels and transparent',
                    'amorphous concrete, in which concrete is a single element covering entire roof',
                    'amorphous asphalt, in which asphalt is a single element covering entire roof',
                    'amorphous membrane, in which membrane is a single element covering entire roof and could include rubber roofing, thermoplastic polyolefin, PVC',
                    'amorphous fabric, in which fabric is a single element covering entire roof and stretched over a frame',
                ]
                self.classes = [
                    'Thatch', 
                    'GreenVegetation', 
                    'LimestoneSlates', 
                    'StoneSlates', 
                    'ClayTiles', 
                    'AsphaltTiles', 
                    'ConcreteTiles', 
                    'WoodTiles', 
                    'MetalSheetMaterials', 
                    'PolycarbonateSheetMaterials',
                    'GlassSheetMaterials', 
                    'AmorphousConcrete', 
                    'AmorphousAsphalt', 
                    'AmorphousMembrane', 
                    'AmorphousFabric', 
                    ]
            self.template = "a photo of a building with a roof made of {}." 