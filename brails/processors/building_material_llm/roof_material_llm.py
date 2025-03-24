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
                    'thatch, where thatch elements look very small / semi-ridged',
                    'green vegetation, where green elements look small / non-uniform',
                    'limestone slates, where limestone elements look small / ridged',
                    'stone slates, where stone elements look small / ridged',
                    'clay tiles, where clay elements look small / ridged',
                    'asphalt tiles, where asphalt elements look small / ridged',
                    'concrete tiles, where concrete elements look small / ridged',
                    'wood tiles, where wood elements look small / ridged',
                    'metal sheet materials, where elements elements look large; ridged, corrugated, or laid in panels',
                    'polycarbonate sheet materials, where elements look large; ridged, corrugated, or laid in panels; and are clear or painted',
                    'glass sheet materials, where glass elements look large; ridged, corrugated, or laid in panels; and are clear',
                    'amorphous concrete, where concrete is a single element covering entire roof',
                    'amorphous asphalt, where asphalt is a single element covering entire roof',
                    'amorphous membrane, where it is a single element covering entire roof and could include rubber roofing, thermoplastic polyolefin, PVC',
                    'amorphous fabric, where fabric is a single element covering entire roof / stretched over a frame',
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