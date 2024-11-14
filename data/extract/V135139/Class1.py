class TEffectSourceDescriptor:
    def __init__(self, DescriptorId=None):
        self.DescriptorId = DescriptorId

    def __repr__(self):
        return f'<TEffectSourceDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['DescriptorId']]) + '>'


class TEffectsConstantes:
    def __init__(self, BrickEffectSourceDescriptor=None, CommanderEffectSourceDescriptor=None, HitCriticalEffectSourceDescriptor=None, TerrainCriticalEffectSourceDescriptor=None):
        self.BrickEffectSourceDescriptor = BrickEffectSourceDescriptor
        self.CommanderEffectSourceDescriptor = CommanderEffectSourceDescriptor
        self.HitCriticalEffectSourceDescriptor = HitCriticalEffectSourceDescriptor
        self.TerrainCriticalEffectSourceDescriptor = TerrainCriticalEffectSourceDescriptor

    def __repr__(self):
        return f'<TEffectsConstantes ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['BrickEffectSourceDescriptor', 'CommanderEffectSourceDescriptor', 'HitCriticalEffectSourceDescriptor', 'TerrainCriticalEffectSourceDescriptor']]) + '>'


class THelicopterWaypointWeightsDescriptor:
    def __init__(self, AnglesXY=None, AngularSpeedXY=None, AngleZ=None, Speed=None, Position=None, AnglularZSpeed=None):
        self.AnglesXY = AnglesXY
        self.AngularSpeedXY = AngularSpeedXY
        self.AngleZ = AngleZ
        self.Speed = Speed
        self.Position = Position
        self.AnglularZSpeed = AnglularZSpeed

    def __repr__(self):
        return f'<THelicopterWaypointWeightsDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['AnglesXY', 'AngularSpeedXY', 'AngleZ', 'Speed', 'Position', 'AnglularZSpeed']]) + '>'


class THelicopterWeightsManager:
    def __init__(self, HelicopterWeights=None, IntermediateWaypointHelicopterWeights=None, DefaultHelicopterWeights=None, DefaultIntermediateWaypointsHelicopterWeights=None, WaypointScoreThresholds=None, DefaultFinalWaypointScore=None, DefaultIntermediateWayPointScoreTolerance=None):
        self.HelicopterWeights = HelicopterWeights
        self.IntermediateWaypointHelicopterWeights = IntermediateWaypointHelicopterWeights
        self.DefaultHelicopterWeights = DefaultHelicopterWeights
        self.DefaultIntermediateWaypointsHelicopterWeights = DefaultIntermediateWaypointsHelicopterWeights
        self.WaypointScoreThresholds = WaypointScoreThresholds
        self.DefaultFinalWaypointScore = DefaultFinalWaypointScore
        self.DefaultIntermediateWayPointScoreTolerance = DefaultIntermediateWayPointScoreTolerance

    def __repr__(self):
        return f'<THelicopterWeightsManager ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['HelicopterWeights', 'IntermediateWaypointHelicopterWeights', 'DefaultHelicopterWeights', 'DefaultIntermediateWaypointsHelicopterWeights', 'WaypointScoreThresholds', 'DefaultFinalWaypointScore', 'DefaultIntermediateWayPointScoreTolerance']]) + '>'


class TInitialisationGameDistanceUnits:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TInitialisationGameDistanceUnits>'

class EGameDifficulty:
    def __init__(self, Values=None):
        self.Values = Values

    def __repr__(self):
        return f'<EGameDifficulty ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Values']]) + '>'


class TGameDifficultyListConfiguration:
    def __init__(self, MissionTypeToDifficulties=None):
        self.MissionTypeToDifficulties = MissionTypeToDifficulties

    def __repr__(self):
        return f'<TGameDifficultyListConfiguration ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MissionTypeToDifficulties']]) + '>'


class ModelDescriptor:
    def __init__(self, FileName=None, TextureDirectory=None):
        self.FileName = FileName
        self.TextureDirectory = TextureDirectory

    def __repr__(self):
        return f'<ModelDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['FileName', 'TextureDirectory']]) + '>'


class TConstantAlternativeSelector:
    def __init__(self, Key=None):
        self.Key = Key

    def __repr__(self):
        return f'<TConstantAlternativeSelector ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Key']]) + '>'


class TPilotLodSelector:
    def __init__(self, CameraMoverManagerModernWarfare=None, OptionalLimit=None, HighLowLimitInMeter=None, LowNoneLimitInMeter=None):
        self.CameraMoverManagerModernWarfare = CameraMoverManagerModernWarfare
        self.OptionalLimit = OptionalLimit
        self.HighLowLimitInMeter = HighLowLimitInMeter
        self.LowNoneLimitInMeter = LowNoneLimitInMeter

    def __repr__(self):
        return f'<TPilotLodSelector ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['CameraMoverManagerModernWarfare', 'OptionalLimit', 'HighLowLimitInMeter', 'LowNoneLimitInMeter']]) + '>'


class TCameraScaler:
    def __init__(self, ScaleOption=None, ScaleFactor=None, ScaleMinReferenceAltitude=None, Camera=None, ScaleMax=None):
        self.ScaleOption = ScaleOption
        self.ScaleFactor = ScaleFactor
        self.ScaleMinReferenceAltitude = ScaleMinReferenceAltitude
        self.Camera = Camera
        self.ScaleMax = ScaleMax

    def __repr__(self):
        return f'<TCameraScaler ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ScaleOption', 'ScaleFactor', 'ScaleMinReferenceAltitude', 'Camera', 'ScaleMax']]) + '>'


class TIdentityScaler:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TIdentityScaler>'


class TLodSelector:
    def __init__(self, HighMidLimitInMeter=None, CameraMoverManagerModernWarfare=None, MidLowLimitInMeter=None, OptionalLimit=None):
        self.HighMidLimitInMeter = HighMidLimitInMeter
        self.CameraMoverManagerModernWarfare = CameraMoverManagerModernWarfare
        self.MidLowLimitInMeter = MidLowLimitInMeter
        self.OptionalLimit = OptionalLimit

    def __repr__(self):
        return f'<TLodSelector ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['HighMidLimitInMeter', 'CameraMoverManagerModernWarfare', 'MidLowLimitInMeter', 'OptionalLimit']]) + '>'


class TTimelyDepictionReceiverFactory:
    def __init__(self, DepictionTemplate=None):
        self.DepictionTemplate = DepictionTemplate

    def __repr__(self):
        return f'<TTimelyDepictionReceiverFactory ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['DepictionTemplate']]) + '>'


class TDepictionTemplate:
    def __init__(self, Selector=None, CoatingName=None, Actions=None, DepictionAlternatives=None, Operators=None, AdditionalTextures=None, SubDepictions=None, ResidentMaterialTags=None, Scaler=None):
        self.Selector = Selector
        self.CoatingName = CoatingName
        self.Actions = Actions
        self.DepictionAlternatives = DepictionAlternatives
        self.Operators = Operators
        self.AdditionalTextures = AdditionalTextures
        self.SubDepictions = SubDepictions
        self.ResidentMaterialTags = ResidentMaterialTags
        self.Scaler = Scaler

    def __repr__(self):
        return f'<TDepictionTemplate ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Selector', 'CoatingName', 'Actions', 'DepictionAlternatives', 'Operators', 'AdditionalTextures', 'SubDepictions', 'ResidentMaterialTags', 'Scaler']]) + '>'


class DepictionDescriptor_LOD_High:
    def __init__(self, MeshDescriptor=None):
        self.MeshDescriptor = MeshDescriptor

    def __repr__(self):
        return f'<DepictionDescriptor_LOD_High ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MeshDescriptor']]) + '>'


class DepictionDescriptor_LOD_Mid:
    def __init__(self, MeshDescriptor=None):
        self.MeshDescriptor = MeshDescriptor

    def __repr__(self):
        return f'<DepictionDescriptor_LOD_Mid ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MeshDescriptor']]) + '>'


class DepictionDescriptor_LOD_Low:
    def __init__(self, MeshDescriptor=None, DisabledOperators=None):
        self.MeshDescriptor = MeshDescriptor
        self.DisabledOperators = DisabledOperators

    def __repr__(self):
        return f'<DepictionDescriptor_LOD_Low ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MeshDescriptor', 'DisabledOperators']]) + '>'


class TConstantScaler:
    def __init__(self, Scale=None):
        self.Scale = Scale

    def __repr__(self):
        return f'<TConstantScaler ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Scale']]) + '>'


class TSubDepiction:
    def __init__(self, Anchors=None, Depiction=None):
        self.Anchors = Anchors
        self.Depiction = Depiction

    def __repr__(self):
        return f'<TSubDepiction ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Anchors', 'Depiction']]) + '>'


class DepictionDescriptor_LOD_InfantryHigh:
    def __init__(self, MeshDescriptor=None):
        self.MeshDescriptor = MeshDescriptor

    def __repr__(self):
        return f'<DepictionDescriptor_LOD_InfantryHigh ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MeshDescriptor']]) + '>'


class DepictionDescriptor_LOD_InfantryLow:
    def __init__(self, MeshDescriptor=None):
        self.MeshDescriptor = MeshDescriptor

    def __repr__(self):
        return f'<DepictionDescriptor_LOD_InfantryLow ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MeshDescriptor']]) + '>'


class TEntityDescriptor:
    def __init__(self, ClassNameForDebug=None, ModulesDescriptors=None, World=None, DescriptorId=None):
        self.ClassNameForDebug = ClassNameForDebug
        self.ModulesDescriptors = ModulesDescriptors
        self.World = World
        self.DescriptorId = DescriptorId

    def __repr__(self):
        return f'<TEntityDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ClassNameForDebug', 'ModulesDescriptors', 'World', 'DescriptorId']]) + '>'


class TFlagsModuleDescriptor:
    def __init__(self, InitialFlagSet=None):
        self.InitialFlagSet = InitialFlagSet

    def __repr__(self):
        return f'<TFlagsModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['InitialFlagSet']]) + '>'


class TPositionModuleDescriptor:
    def __init__(self, InGeoDb=None):
        self.InGeoDb = InGeoDb

    def __repr__(self):
        return f'<TPositionModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['InGeoDb']]) + '>'


class TVisibilityModuleDescriptor:
    def __init__(self, VisionUnitType=None, UnitConcealmentBonus=None):
        self.VisionUnitType = VisionUnitType
        self.UnitConcealmentBonus = UnitConcealmentBonus

    def __repr__(self):
        return f'<TVisibilityModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['VisionUnitType', 'UnitConcealmentBonus']]) + '>'


class TLinkTeamModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TLinkTeamModuleDescriptor>'


class TPackSignauxModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TPackSignauxModuleDescriptor>'


class TTagsModuleDescriptor:
    def __init__(self, TagSet=None):
        self.TagSet = TagSet

    def __repr__(self):
        return f'<TTagsModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TagSet']]) + '>'


class TTargetDataModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TTargetDataModuleDescriptor>'


class TCameraShowroomModuleDescriptor:
    def __init__(self, SpawnType=None):
        self.SpawnType = SpawnType

    def __repr__(self):
        return f'<TCameraShowroomModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['SpawnType']]) + '>'


class TSoundDescriptor:
    def __init__(self, SoundSettings=None, TheSoundStream=None, UseSpecialLoop=None):
        self.SoundSettings = SoundSettings
        self.TheSoundStream = TheSoundStream
        self.UseSpecialLoop = UseSpecialLoop

    def __repr__(self):
        return f'<TSoundDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['SoundSettings', 'TheSoundStream', 'UseSpecialLoop']]) + '>'


class TSoundStream:
    def __init__(self, FileName=None):
        self.FileName = FileName

    def __repr__(self):
        return f'<TSoundStream ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['FileName']]) + '>'


class TUIRenderLayersManager:
    def __init__(self, RenderLayerArray=None):
        self.RenderLayerArray = RenderLayerArray

    def __repr__(self):
        return f'<TUIRenderLayersManager ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['RenderLayerArray']]) + '>'


class TUILayer:
    def __init__(self, UserInputLayer=None, Scene=None, RenderLayersManager=None):
        self.UserInputLayer = UserInputLayer
        self.Scene = Scene
        self.RenderLayersManager = RenderLayersManager

    def __repr__(self):
        return f'<TUILayer ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['UserInputLayer', 'Scene', 'RenderLayersManager']]) + '>'


class TUIDebugConsoleDescriptor:
    def __init__(self, UniqueName=None, ComponentFrame=None, IsClippable=None, HasBackground=None, BackgroundBlockColorToken=None, HasBorder=None, BorderLineColorToken=None, UniformDrawer=None, Components=None, TextSize=None, TextColor=None, InfoTextColor=None, SecondaryInfoTextColor=None, SuccessTextColor=None, FailureTextColor=None, TextSelectionColor=None, SelectionColor=None, SelectionColorNoFocus=None, MaxNumberOfCharacters=None, TextPosPixel=None, TextPosMagnifiable=None, TextPosRelative=None, TextWidthPixel=None, TextWidthMagnifiable=None, TextWidthRelative=None, TextMarginMagnifiable=None, MinFrameRelativeWidthHeight=None, TextStyle=None, SpeedAnimRatio=None):
        self.UniqueName = UniqueName
        self.ComponentFrame = ComponentFrame
        self.IsClippable = IsClippable
        self.HasBackground = HasBackground
        self.BackgroundBlockColorToken = BackgroundBlockColorToken
        self.HasBorder = HasBorder
        self.BorderLineColorToken = BorderLineColorToken
        self.UniformDrawer = UniformDrawer
        self.Components = Components
        self.TextSize = TextSize
        self.TextColor = TextColor
        self.InfoTextColor = InfoTextColor
        self.SecondaryInfoTextColor = SecondaryInfoTextColor
        self.SuccessTextColor = SuccessTextColor
        self.FailureTextColor = FailureTextColor
        self.TextSelectionColor = TextSelectionColor
        self.SelectionColor = SelectionColor
        self.SelectionColorNoFocus = SelectionColorNoFocus
        self.MaxNumberOfCharacters = MaxNumberOfCharacters
        self.TextPosPixel = TextPosPixel
        self.TextPosMagnifiable = TextPosMagnifiable
        self.TextPosRelative = TextPosRelative
        self.TextWidthPixel = TextWidthPixel
        self.TextWidthMagnifiable = TextWidthMagnifiable
        self.TextWidthRelative = TextWidthRelative
        self.TextMarginMagnifiable = TextMarginMagnifiable
        self.MinFrameRelativeWidthHeight = MinFrameRelativeWidthHeight
        self.TextStyle = TextStyle
        self.SpeedAnimRatio = SpeedAnimRatio

    def __repr__(self):
        return f'<TUIDebugConsoleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['UniqueName', 'ComponentFrame', 'IsClippable', 'HasBackground', 'BackgroundBlockColorToken', 'HasBorder', 'BorderLineColorToken', 'UniformDrawer', 'Components', 'TextSize', 'TextColor', 'InfoTextColor', 'SecondaryInfoTextColor', 'SuccessTextColor', 'FailureTextColor', 'TextSelectionColor', 'SelectionColor', 'SelectionColorNoFocus', 'MaxNumberOfCharacters', 'TextPosPixel', 'TextPosMagnifiable', 'TextPosRelative', 'TextWidthPixel', 'TextWidthMagnifiable', 'TextWidthRelative', 'TextMarginMagnifiable', 'MinFrameRelativeWidthHeight', 'TextStyle', 'SpeedAnimRatio']]) + '>'


class TUIFramePropertyRTTI:
    def __init__(self, RelativeOffset=None, MagnifiableWidthHeight=None, RelativeWidthHeight=None, AlignementToAnchor=None, PixelWidthHeight=None, AlignementToFather=None, MagnifiableOffset=None, PixelOffset=None):
        self.RelativeOffset = RelativeOffset
        self.MagnifiableWidthHeight = MagnifiableWidthHeight
        self.RelativeWidthHeight = RelativeWidthHeight
        self.AlignementToAnchor = AlignementToAnchor
        self.PixelWidthHeight = PixelWidthHeight
        self.AlignementToFather = AlignementToFather
        self.MagnifiableOffset = MagnifiableOffset
        self.PixelOffset = PixelOffset

    def __repr__(self):
        return f'<TUIFramePropertyRTTI ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['RelativeOffset', 'MagnifiableWidthHeight', 'RelativeWidthHeight', 'AlignementToAnchor', 'PixelWidthHeight', 'AlignementToFather', 'MagnifiableOffset', 'PixelOffset']]) + '>'


class BUCKSensibleAreaDescriptor:
    def __init__(self, MagnifierMultiplication=None, Components=None, FitStyle=None, HidePointerEvents=None, ElementName=None, MaskEvents=None, ComponentFrame=None):
        self.MagnifierMultiplication = MagnifierMultiplication
        self.Components = Components
        self.FitStyle = FitStyle
        self.HidePointerEvents = HidePointerEvents
        self.ElementName = ElementName
        self.MaskEvents = MaskEvents
        self.ComponentFrame = ComponentFrame

    def __repr__(self):
        return f'<BUCKSensibleAreaDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MagnifierMultiplication', 'Components', 'FitStyle', 'HidePointerEvents', 'ElementName', 'MaskEvents', 'ComponentFrame']]) + '>'


class TUIFormattedTextStyle:
    def __init__(self, TextStyle=None, ParagraphStyle=None, Typeface=None):
        self.TextStyle = TextStyle
        self.ParagraphStyle = ParagraphStyle
        self.Typeface = Typeface

    def __repr__(self):
        return f'<TUIFormattedTextStyle ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TextStyle', 'ParagraphStyle', 'Typeface']]) + '>'


class TTextStyle:
    def __init__(self, ColorUp=None, Stroke=None, FontSize=None, StrokeHardness=None, StrokeSize=None, ColorStroke=None, ColorBottom=None, Offset=None, UpperCase=None, TextThickness=None):
        self.ColorUp = ColorUp
        self.Stroke = Stroke
        self.FontSize = FontSize
        self.StrokeHardness = StrokeHardness
        self.StrokeSize = StrokeSize
        self.ColorStroke = ColorStroke
        self.ColorBottom = ColorBottom
        self.Offset = Offset
        self.UpperCase = UpperCase
        self.TextThickness = TextThickness

    def __repr__(self):
        return f'<TTextStyle ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ColorUp', 'Stroke', 'FontSize', 'StrokeHardness', 'StrokeSize', 'ColorStroke', 'ColorBottom', 'Offset', 'UpperCase', 'TextThickness']]) + '>'


class TParagraphStyle:
    def __init__(self, BigWordAction=None, Balanced=None, VerticalAlignment=None, LineWidth=None, InterLine=None, OpticalAlignment=None, Alignment=None):
        self.BigWordAction = BigWordAction
        self.Balanced = Balanced
        self.VerticalAlignment = VerticalAlignment
        self.LineWidth = LineWidth
        self.InterLine = InterLine
        self.OpticalAlignment = OpticalAlignment
        self.Alignment = Alignment

    def __repr__(self):
        return f'<TParagraphStyle ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['BigWordAction', 'Balanced', 'VerticalAlignment', 'LineWidth', 'InterLine', 'OpticalAlignment', 'Alignment']]) + '>'


class TUIDebugConsoleResources:
    def __init__(self, Handler=None, DebugConsole=None, UserInputLayer=None, LayerConsole=None, StyleGuide=None, UserInputBinder=None, Camera=None, World3D=None, Scene3D=None):
        self.Handler = Handler
        self.DebugConsole = DebugConsole
        self.UserInputLayer = UserInputLayer
        self.LayerConsole = LayerConsole
        self.StyleGuide = StyleGuide
        self.UserInputBinder = UserInputBinder
        self.Camera = Camera
        self.World3D = World3D
        self.Scene3D = Scene3D

    def __repr__(self):
        return f'<TUIDebugConsoleResources ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Handler', 'DebugConsole', 'UserInputLayer', 'LayerConsole', 'StyleGuide', 'UserInputBinder', 'Camera', 'World3D', 'Scene3D']]) + '>'


class TUIStyleGuide:
    def __init__(self, CommonResource=None, Typeface=None, TextStylesMap=None, TextSizesMap=None, LineSizesMap=None, LineHeightsMap=None, MagnifiableMarginsMap=None, BlockColorsMap=None, LineColorsMap=None, TextColorsMap=None, HintManagementProperties=None, HintableAreaDescriptor=None, TextFormatScript=None):
        self.CommonResource = CommonResource
        self.Typeface = Typeface
        self.TextStylesMap = TextStylesMap
        self.TextSizesMap = TextSizesMap
        self.LineSizesMap = LineSizesMap
        self.LineHeightsMap = LineHeightsMap
        self.MagnifiableMarginsMap = MagnifiableMarginsMap
        self.BlockColorsMap = BlockColorsMap
        self.LineColorsMap = LineColorsMap
        self.TextColorsMap = TextColorsMap
        self.HintManagementProperties = HintManagementProperties
        self.HintableAreaDescriptor = HintableAreaDescriptor
        self.TextFormatScript = TextFormatScript

    def __repr__(self):
        return f'<TUIStyleGuide ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['CommonResource', 'Typeface', 'TextStylesMap', 'TextSizesMap', 'LineSizesMap', 'LineHeightsMap', 'MagnifiableMarginsMap', 'BlockColorsMap', 'LineColorsMap', 'TextColorsMap', 'HintManagementProperties', 'HintableAreaDescriptor', 'TextFormatScript']]) + '>'


class TFloatRTTI:
    def __init__(self, Value=None):
        self.Value = Value

    def __repr__(self):
        return f'<TFloatRTTI ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Value']]) + '>'


class TColorRTTI:
    def __init__(self, Color=None):
        self.Color = Color

    def __repr__(self):
        return f'<TColorRTTI ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Color']]) + '>'


class TTextFormatScriptRTTI:
    def __init__(self, Commands=None):
        self.Commands = Commands

    def __repr__(self):
        return f'<TTextFormatScriptRTTI ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Commands']]) + '>'


class TTFSCommand_StyleChange:
    def __init__(self, Typeface=None, Style=None):
        self.Typeface = Typeface
        self.Style = Style

    def __repr__(self):
        return f'<TTFSCommand_StyleChange ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Typeface', 'Style']]) + '>'


class BUCKContainerDescriptor:
    def __init__(self, UniqueName=None, ChildFitToContent=None, BorderLineColorToken=None, Components=None, IsClippable=None, HidePointerEvents=None, FitStyle=None, UniformDrawer=None, ElementName=None, BackgroundBlockColorToken=None, ComponentFrame=None, MagnifierMultiplication=None, BorderThicknessToken=None, BordersToDraw=None, HasBackground=None, HasBorder=None):
        self.UniqueName = UniqueName
        self.ChildFitToContent = ChildFitToContent
        self.BorderLineColorToken = BorderLineColorToken
        self.Components = Components
        self.IsClippable = IsClippable
        self.HidePointerEvents = HidePointerEvents
        self.FitStyle = FitStyle
        self.UniformDrawer = UniformDrawer
        self.ElementName = ElementName
        self.BackgroundBlockColorToken = BackgroundBlockColorToken
        self.ComponentFrame = ComponentFrame
        self.MagnifierMultiplication = MagnifierMultiplication
        self.BorderThicknessToken = BorderThicknessToken
        self.BordersToDraw = BordersToDraw
        self.HasBackground = HasBackground
        self.HasBorder = HasBorder

    def __repr__(self):
        return f'<BUCKContainerDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['UniqueName', 'ChildFitToContent', 'BorderLineColorToken', 'Components', 'IsClippable', 'HidePointerEvents', 'FitStyle', 'UniformDrawer', 'ElementName', 'BackgroundBlockColorToken', 'ComponentFrame', 'MagnifierMultiplication', 'BorderThicknessToken', 'BordersToDraw', 'HasBackground', 'HasBorder']]) + '>'


class BUCKListDescriptor:
    def __init__(self, UniqueName=None, ChildFitToContent=None, BorderLineColorToken=None, AssumeChildrenAreClippable=None, Axis=None, MagnifiableWidthHeight=None, FirstMargin=None, TextToken=None, Elements=None, HidePointerEvents=None, ElementName=None, AssumeChildrenAreFixedSize=None, BackgroundBlockColorToken=None, ComponentFrame=None, ComponentDescriptor=None, BorderThicknessToken=None, HintExtendedToken=None, ClipContent=None, SortingType=None, GridAlign=None, BreadthComputationMode=None, ForegroundComponents=None, InterItemMargin=None, BackgroundComponents=None, HintBodyToken=None, HasBackground=None, PointerEventsToAllow=None, HasBorder=None, LastMargin=None):
        self.UniqueName = UniqueName
        self.ChildFitToContent = ChildFitToContent
        self.BorderLineColorToken = BorderLineColorToken
        self.AssumeChildrenAreClippable = AssumeChildrenAreClippable
        self.Axis = Axis
        self.MagnifiableWidthHeight = MagnifiableWidthHeight
        self.FirstMargin = FirstMargin
        self.TextToken = TextToken
        self.Elements = Elements
        self.HidePointerEvents = HidePointerEvents
        self.ElementName = ElementName
        self.AssumeChildrenAreFixedSize = AssumeChildrenAreFixedSize
        self.BackgroundBlockColorToken = BackgroundBlockColorToken
        self.ComponentFrame = ComponentFrame
        self.ComponentDescriptor = ComponentDescriptor
        self.BorderThicknessToken = BorderThicknessToken
        self.HintExtendedToken = HintExtendedToken
        self.ClipContent = ClipContent
        self.SortingType = SortingType
        self.GridAlign = GridAlign
        self.BreadthComputationMode = BreadthComputationMode
        self.ForegroundComponents = ForegroundComponents
        self.InterItemMargin = InterItemMargin
        self.BackgroundComponents = BackgroundComponents
        self.HintBodyToken = HintBodyToken
        self.HasBackground = HasBackground
        self.PointerEventsToAllow = PointerEventsToAllow
        self.HasBorder = HasBorder
        self.LastMargin = LastMargin

    def __repr__(self):
        return f'<BUCKListDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['UniqueName', 'ChildFitToContent', 'BorderLineColorToken', 'AssumeChildrenAreClippable', 'Axis', 'MagnifiableWidthHeight', 'FirstMargin', 'TextToken', 'Elements', 'HidePointerEvents', 'ElementName', 'AssumeChildrenAreFixedSize', 'BackgroundBlockColorToken', 'ComponentFrame', 'ComponentDescriptor', 'BorderThicknessToken', 'HintExtendedToken', 'ClipContent', 'SortingType', 'GridAlign', 'BreadthComputationMode', 'ForegroundComponents', 'InterItemMargin', 'BackgroundComponents', 'HintBodyToken', 'HasBackground', 'PointerEventsToAllow', 'HasBorder', 'LastMargin']]) + '>'


class TRTTILength:
    def __init__(self, Pixel=None, Magnifiable=None):
        self.Pixel = Pixel
        self.Magnifiable = Magnifiable

    def __repr__(self):
        return f'<TRTTILength ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Pixel', 'Magnifiable']]) + '>'


class BUCKListElementDescriptor:
    def __init__(self, MinSize=None, ExtendWeight=None, ComponentDescriptor=None):
        self.MinSize = MinSize
        self.ExtendWeight = ExtendWeight
        self.ComponentDescriptor = ComponentDescriptor

    def __repr__(self):
        return f'<BUCKListElementDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MinSize', 'ExtendWeight', 'ComponentDescriptor']]) + '>'


class TActionPointConsumptionGridConstantsDescriptor:
    def __init__(self, TerrainsBloquants=None, TerrainsRalentisseurs=None, TailleDeCaseApproximativeGRU=None, CouleurDeLaCourbe=None, EpaisseurDeLaCourbe=None):
        self.TerrainsBloquants = TerrainsBloquants
        self.TerrainsRalentisseurs = TerrainsRalentisseurs
        self.TailleDeCaseApproximativeGRU = TailleDeCaseApproximativeGRU
        self.CouleurDeLaCourbe = CouleurDeLaCourbe
        self.EpaisseurDeLaCourbe = EpaisseurDeLaCourbe

    def __repr__(self):
        return f'<TActionPointConsumptionGridConstantsDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TerrainsBloquants', 'TerrainsRalentisseurs', 'TailleDeCaseApproximativeGRU', 'CouleurDeLaCourbe', 'EpaisseurDeLaCourbe']]) + '>'


class TAirplaneConstantesModernWarfareDescriptor:
    def __init__(self, EvacuationAltitudeGRU=None, TempsEntreDeuxDecollagesEnSecondes=None, EvacWinchesterToutesLesArmesPrincipales=None, UtiliserArmesPendantEvac=None, FrontLandingGearMeshNodeName=None, BackLandingGearMeshNodeName=None):
        self.EvacuationAltitudeGRU = EvacuationAltitudeGRU
        self.TempsEntreDeuxDecollagesEnSecondes = TempsEntreDeuxDecollagesEnSecondes
        self.EvacWinchesterToutesLesArmesPrincipales = EvacWinchesterToutesLesArmesPrincipales
        self.UtiliserArmesPendantEvac = UtiliserArmesPendantEvac
        self.FrontLandingGearMeshNodeName = FrontLandingGearMeshNodeName
        self.BackLandingGearMeshNodeName = BackLandingGearMeshNodeName

    def __repr__(self):
        return f'<TAirplaneConstantesModernWarfareDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['EvacuationAltitudeGRU', 'TempsEntreDeuxDecollagesEnSecondes', 'EvacWinchesterToutesLesArmesPrincipales', 'UtiliserArmesPendantEvac', 'FrontLandingGearMeshNodeName', 'BackLandingGearMeshNodeName']]) + '>'


class TDynamicTerrainRegularPolygonDelimiter:
    def __init__(self, Radius=None, SideCount=None):
        self.Radius = Radius
        self.SideCount = SideCount

    def __repr__(self):
        return f'<TDynamicTerrainRegularPolygonDelimiter ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Radius', 'SideCount']]) + '>'


class TRoutConstants:
    def __init__(self, TestMoralNombreDes=None, TestMoralNombreFacesDes=None, TestMoralSeuil=None, LanceTestMoralPertePV=None, TempsEntreDeuxTestsMoralPertePV=None, LanceTestMoralSeuilSuppression=None, TempsEntreDeuxTestsMoralSeuilSuppression=None, EffetConditionSuppression=None, EffetAppliqueSuppression=None, SortieSeuilSuppression=None):
        self.TestMoralNombreDes = TestMoralNombreDes
        self.TestMoralNombreFacesDes = TestMoralNombreFacesDes
        self.TestMoralSeuil = TestMoralSeuil
        self.LanceTestMoralPertePV = LanceTestMoralPertePV
        self.TempsEntreDeuxTestsMoralPertePV = TempsEntreDeuxTestsMoralPertePV
        self.LanceTestMoralSeuilSuppression = LanceTestMoralSeuilSuppression
        self.TempsEntreDeuxTestsMoralSeuilSuppression = TempsEntreDeuxTestsMoralSeuilSuppression
        self.EffetConditionSuppression = EffetConditionSuppression
        self.EffetAppliqueSuppression = EffetAppliqueSuppression
        self.SortieSeuilSuppression = SortieSeuilSuppression

    def __repr__(self):
        return f'<TRoutConstants ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TestMoralNombreDes', 'TestMoralNombreFacesDes', 'TestMoralSeuil', 'LanceTestMoralPertePV', 'TempsEntreDeuxTestsMoralPertePV', 'LanceTestMoralSeuilSuppression', 'TempsEntreDeuxTestsMoralSeuilSuppression', 'EffetConditionSuppression', 'EffetAppliqueSuppression', 'SortieSeuilSuppression']]) + '>'


class TDistrictSpawner:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TDistrictSpawner>'


class TEvaluationMenaceConstantesDescriptor:
    def __init__(self, CercleMenaceGRU=None, EscapeRadiusGRU=None, DureeDeMemoireDeLaMenaceEnSecondes=None, ConsidererLesMenacesEnMouvementCommeDirectes=None):
        self.CercleMenaceGRU = CercleMenaceGRU
        self.EscapeRadiusGRU = EscapeRadiusGRU
        self.DureeDeMemoireDeLaMenaceEnSecondes = DureeDeMemoireDeLaMenaceEnSecondes
        self.ConsidererLesMenacesEnMouvementCommeDirectes = ConsidererLesMenacesEnMouvementCommeDirectes

    def __repr__(self):
        return f'<TEvaluationMenaceConstantesDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['CercleMenaceGRU', 'EscapeRadiusGRU', 'DureeDeMemoireDeLaMenaceEnSecondes', 'ConsidererLesMenacesEnMouvementCommeDirectes']]) + '>'


class TSpecificFactoryResources:
    def __init__(self, FactoryDisplayOrder=None, FactoryDescriptions=None):
        self.FactoryDisplayOrder = FactoryDisplayOrder
        self.FactoryDescriptions = FactoryDescriptions

    def __repr__(self):
        return f'<TSpecificFactoryResources ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['FactoryDisplayOrder', 'FactoryDescriptions']]) + '>'


class TSpecificFactoryDescription:
    def __init__(self, FactoryHintExtended=None, FactoryName=None, FactoryHintTitle=None, FactoryHintBody=None):
        self.FactoryHintExtended = FactoryHintExtended
        self.FactoryName = FactoryName
        self.FactoryHintTitle = FactoryHintTitle
        self.FactoryHintBody = FactoryHintBody

    def __repr__(self):
        return f'<TSpecificFactoryDescription ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['FactoryHintExtended', 'FactoryName', 'FactoryHintTitle', 'FactoryHintBody']]) + '>'


class TArrivalFormationConstantes:
    def __init__(self, UnitSpacingWidthLBU=None, FrontLineMinimalSizeLBU=None, DefaultFormationWidthToDepthRatio=None):
        self.UnitSpacingWidthLBU = UnitSpacingWidthLBU
        self.FrontLineMinimalSizeLBU = FrontLineMinimalSizeLBU
        self.DefaultFormationWidthToDepthRatio = DefaultFormationWidthToDepthRatio

    def __repr__(self):
        return f'<TArrivalFormationConstantes ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['UnitSpacingWidthLBU', 'FrontLineMinimalSizeLBU', 'DefaultFormationWidthToDepthRatio']]) + '>'


class TUnitFormationDescriptor:
    def __init__(self, FrontMarginLBU=None, SpacingDepthLBU=None, SpacingWidthLBU=None, FormationLines=None):
        self.FrontMarginLBU = FrontMarginLBU
        self.SpacingDepthLBU = SpacingDepthLBU
        self.SpacingWidthLBU = SpacingWidthLBU
        self.FormationLines = FormationLines

    def __repr__(self):
        return f'<TUnitFormationDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['FrontMarginLBU', 'SpacingDepthLBU', 'SpacingWidthLBU', 'FormationLines']]) + '>'


class TUnitFormationLineDescriptor:
    def __init__(self, UnitTypes=None):
        self.UnitTypes = UnitTypes

    def __repr__(self):
        return f'<TUnitFormationLineDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['UnitTypes']]) + '>'


class TFormationConstantes:
    def __init__(self, UnitFormationDescriptor=None, UnitDeploymentFormationDescriptor=None, DistanceMaintienClicPourDeplacementGhostGRU=None, SnapToFavorableTerrainRadiusGRU=None):
        self.UnitFormationDescriptor = UnitFormationDescriptor
        self.UnitDeploymentFormationDescriptor = UnitDeploymentFormationDescriptor
        self.DistanceMaintienClicPourDeplacementGhostGRU = DistanceMaintienClicPourDeplacementGhostGRU
        self.SnapToFavorableTerrainRadiusGRU = SnapToFavorableTerrainRadiusGRU

    def __repr__(self):
        return f'<TFormationConstantes ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['UnitFormationDescriptor', 'UnitDeploymentFormationDescriptor', 'DistanceMaintienClicPourDeplacementGhostGRU', 'SnapToFavorableTerrainRadiusGRU']]) + '>'


class TRollParameters:
    def __init__(self, DistanceToleranceGRU=None, PiercingThresholdBias=None, DicesNumberFaces=None, InterpolateRangeTable=None, RangeModifiersTable=None, SuccessiveHitModifiersTable=None, MinimalHitChanceWithECM=None):
        self.DistanceToleranceGRU = DistanceToleranceGRU
        self.PiercingThresholdBias = PiercingThresholdBias
        self.DicesNumberFaces = DicesNumberFaces
        self.InterpolateRangeTable = InterpolateRangeTable
        self.RangeModifiersTable = RangeModifiersTable
        self.SuccessiveHitModifiersTable = SuccessiveHitModifiersTable
        self.MinimalHitChanceWithECM = MinimalHitChanceWithECM

    def __repr__(self):
        return f'<TRollParameters ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['DistanceToleranceGRU', 'PiercingThresholdBias', 'DicesNumberFaces', 'InterpolateRangeTable', 'RangeModifiersTable', 'SuccessiveHitModifiersTable', 'MinimalHitChanceWithECM']]) + '>'


class TIAStratConstantesDescriptor_Specific:
    def __init__(self, AutoDeployNumberOfFrameWithoutProduction=None, SeedForIAStrat=None, CacherLesUnitesIdle=None, FollowUnitIfNoTarget=None, CanRequestTransportProduction=None, CanSelectTransportUnits=None, ForceSelectCurrentTransporter=None, NbMacroActionAllowedToProduceSimultaneous=None, RayonDOccupationDansLaGeoDbProdution_ValeurMinGRU=None, RayonDOccupationDansLaGeoDbProdution_ValeurMaxGRU=None, ForbiddenTagsByMission=None, MinUnitWeightToReserveCorridor=None, UnitTagAndWeightToReserveCorridor=None, ControlRatioMinToControl=None, ZoneKnowledgeDuration=None, CommandZoneWeight=None, MinDistanceToRequireTransportGRU=None, MaxDistanceToAcceptTransportRequestGRU=None, ForbidToLoadNewUnits=None, IAStartDelay=None, UnitPowerInformationData=None, ShouldConsiderAPBounceAsDangerous=None, ShouldConsiderPierceAsDangerous=None, APPierceDangerousness=None, ArtilleryStrikeThreatLifeTime=None, DistanceToSeekDistrictForUnitInDefenseGRU=None, DistanceToSeekDefenseUnitForUnitInDefenseGRU=None, DistanceToSeekForestForUnitInDefenseGRU=None, DistanceToSeekPolygonCenterForUnitInDefenseGRU=None, UseAntiStackingForVehicles=None, UseAntiStackingForInfantry=None, MaxNumberOfStackingUnits=None, ObjectiveAttackOwnershipRatio=None, DefenseMacroActionFleePowerRatio=None, OrderedDefensePointTypeToUnitTag=None, MaxDistanceForNearCoverDefensePoint=None, DefaultDefensePointScoringFeature=None, TaggedDefensePointScoringFeature=None, AnticipationDelay=None, OffAnticipationDistanceCoef=None, MinAnticipationDistanceCoef=None, MaxAnticipationDistanceCoef=None, MergeGroupDistInPolygon=None, AddToGroupDistInPolygon=None, DistToValidateRegroupPointInPolygon=None, NumberOfDangerousIndiceAlwaysIgnoredForTacticalPathInCover=None, SecondsToIgnoreDangerousIndiceForTacticalPathInCover=None, BlitzkriegMultiplierForTacticalPathInCover=None, NumberOfDangerousIndicesToIgnoreForRegroupPoint=None, DistanceToRetreatForFleeGRU=None, TimeToWaitAfterFleeToGoBackToOriginalPositionInSeconds=None, TimeSinceLastShotReceivedForFlee=None, UpdateRetreatPointInterval=None, NumberTicksForIdle=None, MinSupplyStock=None, MinLifeRatioForRetreat=None, MinFuelRatioForRetreat=None, ZoneFillerType=None, DefaultInMapArtilleryAmount=None, DefaultOutMapArtilleryAmount=None, DefaultTransportSettings=None, DefaultTransportIsRequiredProduction=None, RoEConstantes=None, CommanderTagSet=None, HelicoSafeCollisionPlanesOrderByTag=None, IAStratPathCostCacheFilePath=None, IAStratDistanceFromNotDefendedCommandZoneGRU=None, HysteresisDistanceForCommandUnitAlreadyAssignToCommandZoneGRU=None, CapturableCommandZoneMoveOutAndCapturePowerRatioForAIDifficulty=None, MinimumScoreRatioForStayInCommandZonePerIADifficulty=None, ProductionCapturableRadiusCheckMultiplier=None, SupplyMinDistanceCheckGRU=None, SupplyDistanceToStopGRU=None, IAStratPathCacheCostPathfindType=None, DeployOffRoadUnitsTags=None, MinSpeedForSearchZone=None):
        self.AutoDeployNumberOfFrameWithoutProduction = AutoDeployNumberOfFrameWithoutProduction
        self.SeedForIAStrat = SeedForIAStrat
        self.CacherLesUnitesIdle = CacherLesUnitesIdle
        self.FollowUnitIfNoTarget = FollowUnitIfNoTarget
        self.CanRequestTransportProduction = CanRequestTransportProduction
        self.CanSelectTransportUnits = CanSelectTransportUnits
        self.ForceSelectCurrentTransporter = ForceSelectCurrentTransporter
        self.NbMacroActionAllowedToProduceSimultaneous = NbMacroActionAllowedToProduceSimultaneous
        self.RayonDOccupationDansLaGeoDbProdution_ValeurMinGRU = RayonDOccupationDansLaGeoDbProdution_ValeurMinGRU
        self.RayonDOccupationDansLaGeoDbProdution_ValeurMaxGRU = RayonDOccupationDansLaGeoDbProdution_ValeurMaxGRU
        self.ForbiddenTagsByMission = ForbiddenTagsByMission
        self.MinUnitWeightToReserveCorridor = MinUnitWeightToReserveCorridor
        self.UnitTagAndWeightToReserveCorridor = UnitTagAndWeightToReserveCorridor
        self.ControlRatioMinToControl = ControlRatioMinToControl
        self.ZoneKnowledgeDuration = ZoneKnowledgeDuration
        self.CommandZoneWeight = CommandZoneWeight
        self.MinDistanceToRequireTransportGRU = MinDistanceToRequireTransportGRU
        self.MaxDistanceToAcceptTransportRequestGRU = MaxDistanceToAcceptTransportRequestGRU
        self.ForbidToLoadNewUnits = ForbidToLoadNewUnits
        self.IAStartDelay = IAStartDelay
        self.UnitPowerInformationData = UnitPowerInformationData
        self.ShouldConsiderAPBounceAsDangerous = ShouldConsiderAPBounceAsDangerous
        self.ShouldConsiderPierceAsDangerous = ShouldConsiderPierceAsDangerous
        self.APPierceDangerousness = APPierceDangerousness
        self.ArtilleryStrikeThreatLifeTime = ArtilleryStrikeThreatLifeTime
        self.DistanceToSeekDistrictForUnitInDefenseGRU = DistanceToSeekDistrictForUnitInDefenseGRU
        self.DistanceToSeekDefenseUnitForUnitInDefenseGRU = DistanceToSeekDefenseUnitForUnitInDefenseGRU
        self.DistanceToSeekForestForUnitInDefenseGRU = DistanceToSeekForestForUnitInDefenseGRU
        self.DistanceToSeekPolygonCenterForUnitInDefenseGRU = DistanceToSeekPolygonCenterForUnitInDefenseGRU
        self.UseAntiStackingForVehicles = UseAntiStackingForVehicles
        self.UseAntiStackingForInfantry = UseAntiStackingForInfantry
        self.MaxNumberOfStackingUnits = MaxNumberOfStackingUnits
        self.ObjectiveAttackOwnershipRatio = ObjectiveAttackOwnershipRatio
        self.DefenseMacroActionFleePowerRatio = DefenseMacroActionFleePowerRatio
        self.OrderedDefensePointTypeToUnitTag = OrderedDefensePointTypeToUnitTag
        self.MaxDistanceForNearCoverDefensePoint = MaxDistanceForNearCoverDefensePoint
        self.DefaultDefensePointScoringFeature = DefaultDefensePointScoringFeature
        self.TaggedDefensePointScoringFeature = TaggedDefensePointScoringFeature
        self.AnticipationDelay = AnticipationDelay
        self.OffAnticipationDistanceCoef = OffAnticipationDistanceCoef
        self.MinAnticipationDistanceCoef = MinAnticipationDistanceCoef
        self.MaxAnticipationDistanceCoef = MaxAnticipationDistanceCoef
        self.MergeGroupDistInPolygon = MergeGroupDistInPolygon
        self.AddToGroupDistInPolygon = AddToGroupDistInPolygon
        self.DistToValidateRegroupPointInPolygon = DistToValidateRegroupPointInPolygon
        self.NumberOfDangerousIndiceAlwaysIgnoredForTacticalPathInCover = NumberOfDangerousIndiceAlwaysIgnoredForTacticalPathInCover
        self.SecondsToIgnoreDangerousIndiceForTacticalPathInCover = SecondsToIgnoreDangerousIndiceForTacticalPathInCover
        self.BlitzkriegMultiplierForTacticalPathInCover = BlitzkriegMultiplierForTacticalPathInCover
        self.NumberOfDangerousIndicesToIgnoreForRegroupPoint = NumberOfDangerousIndicesToIgnoreForRegroupPoint
        self.DistanceToRetreatForFleeGRU = DistanceToRetreatForFleeGRU
        self.TimeToWaitAfterFleeToGoBackToOriginalPositionInSeconds = TimeToWaitAfterFleeToGoBackToOriginalPositionInSeconds
        self.TimeSinceLastShotReceivedForFlee = TimeSinceLastShotReceivedForFlee
        self.UpdateRetreatPointInterval = UpdateRetreatPointInterval
        self.NumberTicksForIdle = NumberTicksForIdle
        self.MinSupplyStock = MinSupplyStock
        self.MinLifeRatioForRetreat = MinLifeRatioForRetreat
        self.MinFuelRatioForRetreat = MinFuelRatioForRetreat
        self.ZoneFillerType = ZoneFillerType
        self.DefaultInMapArtilleryAmount = DefaultInMapArtilleryAmount
        self.DefaultOutMapArtilleryAmount = DefaultOutMapArtilleryAmount
        self.DefaultTransportSettings = DefaultTransportSettings
        self.DefaultTransportIsRequiredProduction = DefaultTransportIsRequiredProduction
        self.RoEConstantes = RoEConstantes
        self.CommanderTagSet = CommanderTagSet
        self.HelicoSafeCollisionPlanesOrderByTag = HelicoSafeCollisionPlanesOrderByTag
        self.IAStratPathCostCacheFilePath = IAStratPathCostCacheFilePath
        self.IAStratDistanceFromNotDefendedCommandZoneGRU = IAStratDistanceFromNotDefendedCommandZoneGRU
        self.HysteresisDistanceForCommandUnitAlreadyAssignToCommandZoneGRU = HysteresisDistanceForCommandUnitAlreadyAssignToCommandZoneGRU
        self.CapturableCommandZoneMoveOutAndCapturePowerRatioForAIDifficulty = CapturableCommandZoneMoveOutAndCapturePowerRatioForAIDifficulty
        self.MinimumScoreRatioForStayInCommandZonePerIADifficulty = MinimumScoreRatioForStayInCommandZonePerIADifficulty
        self.ProductionCapturableRadiusCheckMultiplier = ProductionCapturableRadiusCheckMultiplier
        self.SupplyMinDistanceCheckGRU = SupplyMinDistanceCheckGRU
        self.SupplyDistanceToStopGRU = SupplyDistanceToStopGRU
        self.IAStratPathCacheCostPathfindType = IAStratPathCacheCostPathfindType
        self.DeployOffRoadUnitsTags = DeployOffRoadUnitsTags
        self.MinSpeedForSearchZone = MinSpeedForSearchZone

    def __repr__(self):
        return f'<TIAStratConstantesDescriptor_Specific ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['AutoDeployNumberOfFrameWithoutProduction', 'SeedForIAStrat', 'CacherLesUnitesIdle', 'FollowUnitIfNoTarget', 'CanRequestTransportProduction', 'CanSelectTransportUnits', 'ForceSelectCurrentTransporter', 'NbMacroActionAllowedToProduceSimultaneous', 'RayonDOccupationDansLaGeoDbProdution_ValeurMinGRU', 'RayonDOccupationDansLaGeoDbProdution_ValeurMaxGRU', 'ForbiddenTagsByMission', 'MinUnitWeightToReserveCorridor', 'UnitTagAndWeightToReserveCorridor', 'ControlRatioMinToControl', 'ZoneKnowledgeDuration', 'CommandZoneWeight', 'MinDistanceToRequireTransportGRU', 'MaxDistanceToAcceptTransportRequestGRU', 'ForbidToLoadNewUnits', 'IAStartDelay', 'UnitPowerInformationData', 'ShouldConsiderAPBounceAsDangerous', 'ShouldConsiderPierceAsDangerous', 'APPierceDangerousness', 'ArtilleryStrikeThreatLifeTime', 'DistanceToSeekDistrictForUnitInDefenseGRU', 'DistanceToSeekDefenseUnitForUnitInDefenseGRU', 'DistanceToSeekForestForUnitInDefenseGRU', 'DistanceToSeekPolygonCenterForUnitInDefenseGRU', 'UseAntiStackingForVehicles', 'UseAntiStackingForInfantry', 'MaxNumberOfStackingUnits', 'ObjectiveAttackOwnershipRatio', 'DefenseMacroActionFleePowerRatio', 'OrderedDefensePointTypeToUnitTag', 'MaxDistanceForNearCoverDefensePoint', 'DefaultDefensePointScoringFeature', 'TaggedDefensePointScoringFeature', 'AnticipationDelay', 'OffAnticipationDistanceCoef', 'MinAnticipationDistanceCoef', 'MaxAnticipationDistanceCoef', 'MergeGroupDistInPolygon', 'AddToGroupDistInPolygon', 'DistToValidateRegroupPointInPolygon', 'NumberOfDangerousIndiceAlwaysIgnoredForTacticalPathInCover', 'SecondsToIgnoreDangerousIndiceForTacticalPathInCover', 'BlitzkriegMultiplierForTacticalPathInCover', 'NumberOfDangerousIndicesToIgnoreForRegroupPoint', 'DistanceToRetreatForFleeGRU', 'TimeToWaitAfterFleeToGoBackToOriginalPositionInSeconds', 'TimeSinceLastShotReceivedForFlee', 'UpdateRetreatPointInterval', 'NumberTicksForIdle', 'MinSupplyStock', 'MinLifeRatioForRetreat', 'MinFuelRatioForRetreat', 'ZoneFillerType', 'DefaultInMapArtilleryAmount', 'DefaultOutMapArtilleryAmount', 'DefaultTransportSettings', 'DefaultTransportIsRequiredProduction', 'RoEConstantes', 'CommanderTagSet', 'HelicoSafeCollisionPlanesOrderByTag', 'IAStratPathCostCacheFilePath', 'IAStratDistanceFromNotDefendedCommandZoneGRU', 'HysteresisDistanceForCommandUnitAlreadyAssignToCommandZoneGRU', 'CapturableCommandZoneMoveOutAndCapturePowerRatioForAIDifficulty', 'MinimumScoreRatioForStayInCommandZonePerIADifficulty', 'ProductionCapturableRadiusCheckMultiplier', 'SupplyMinDistanceCheckGRU', 'SupplyDistanceToStopGRU', 'IAStratPathCacheCostPathfindType', 'DeployOffRoadUnitsTags', 'MinSpeedForSearchZone']]) + '>'


class TDefensePointScoringFeature:
    def __init__(self, DefensePointPositioning=None, DefensePointScoringValue=None):
        self.DefensePointPositioning = DefensePointPositioning
        self.DefensePointScoringValue = DefensePointScoringValue

    def __repr__(self):
        return f'<TDefensePointScoringFeature ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['DefensePointPositioning', 'DefensePointScoringValue']]) + '>'


class TCircleZoneFiller:
    def __init__(self, Radius=None):
        self.Radius = Radius

    def __repr__(self):
        return f'<TCircleZoneFiller ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Radius']]) + '>'


class TUnitPowerInformationConstante:
    def __init__(self, UnitPowerAntiAirMultiplier=None, UnitPowerDistrictCoeff=None, UnitPowerTerrainCoeff=None, UnitPowerBuildingMultiplier=None, UnitPowerUnarmedOrPinnedMultiplier=None, DefaultDistanceToConsiderOtherUnitsPowerGRU=None):
        self.UnitPowerAntiAirMultiplier = UnitPowerAntiAirMultiplier
        self.UnitPowerDistrictCoeff = UnitPowerDistrictCoeff
        self.UnitPowerTerrainCoeff = UnitPowerTerrainCoeff
        self.UnitPowerBuildingMultiplier = UnitPowerBuildingMultiplier
        self.UnitPowerUnarmedOrPinnedMultiplier = UnitPowerUnarmedOrPinnedMultiplier
        self.DefaultDistanceToConsiderOtherUnitsPowerGRU = DefaultDistanceToConsiderOtherUnitsPowerGRU

    def __repr__(self):
        return f'<TUnitPowerInformationConstante ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['UnitPowerAntiAirMultiplier', 'UnitPowerDistrictCoeff', 'UnitPowerTerrainCoeff', 'UnitPowerBuildingMultiplier', 'UnitPowerUnarmedOrPinnedMultiplier', 'DefaultDistanceToConsiderOtherUnitsPowerGRU']]) + '>'


class TRoEConstantes:
    def __init__(self, UnarmedVehiculeBehavior=None, MissilesBehavior=None, ShotReactionBehavior=None, ActivateAutoResale=None):
        self.UnarmedVehiculeBehavior = UnarmedVehiculeBehavior
        self.MissilesBehavior = MissilesBehavior
        self.ShotReactionBehavior = ShotReactionBehavior
        self.ActivateAutoResale = ActivateAutoResale

    def __repr__(self):
        return f'<TRoEConstantes ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['UnarmedVehiculeBehavior', 'MissilesBehavior', 'ShotReactionBehavior', 'ActivateAutoResale']]) + '>'


class TIAStratAirstrikeConstantes:
    def __init__(self, UseAirstrikeDefenseSystem=None, DefenseAirstrikeSettings=None, UseAirStrikeOpportunisticAttack=None, OpportunisticSingleTargetAirstrikeSettings=None, OpportunisticTargetInGroupAirstrikeSettings=None, TargetPowerForOpportunisticSingleTargetAirStrike=None, TargetPowerForOpportunisticTargetInGroupAirStrike=None, RadiusForOpportunisticTargetInGroupAirStrikeGRU=None, MinNbrOfTargetsForOpportunisticTargetInGroupAirStrike=None, StrikeLimitations=None, AirplaneWaitForDecisionTime=None, ThreatOutOfCorridorDevaluationValue=None):
        self.UseAirstrikeDefenseSystem = UseAirstrikeDefenseSystem
        self.DefenseAirstrikeSettings = DefenseAirstrikeSettings
        self.UseAirStrikeOpportunisticAttack = UseAirStrikeOpportunisticAttack
        self.OpportunisticSingleTargetAirstrikeSettings = OpportunisticSingleTargetAirstrikeSettings
        self.OpportunisticTargetInGroupAirstrikeSettings = OpportunisticTargetInGroupAirstrikeSettings
        self.TargetPowerForOpportunisticSingleTargetAirStrike = TargetPowerForOpportunisticSingleTargetAirStrike
        self.TargetPowerForOpportunisticTargetInGroupAirStrike = TargetPowerForOpportunisticTargetInGroupAirStrike
        self.RadiusForOpportunisticTargetInGroupAirStrikeGRU = RadiusForOpportunisticTargetInGroupAirStrikeGRU
        self.MinNbrOfTargetsForOpportunisticTargetInGroupAirStrike = MinNbrOfTargetsForOpportunisticTargetInGroupAirStrike
        self.StrikeLimitations = StrikeLimitations
        self.AirplaneWaitForDecisionTime = AirplaneWaitForDecisionTime
        self.ThreatOutOfCorridorDevaluationValue = ThreatOutOfCorridorDevaluationValue

    def __repr__(self):
        return f'<TIAStratAirstrikeConstantes ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['UseAirstrikeDefenseSystem', 'DefenseAirstrikeSettings', 'UseAirStrikeOpportunisticAttack', 'OpportunisticSingleTargetAirstrikeSettings', 'OpportunisticTargetInGroupAirstrikeSettings', 'TargetPowerForOpportunisticSingleTargetAirStrike', 'TargetPowerForOpportunisticTargetInGroupAirStrike', 'RadiusForOpportunisticTargetInGroupAirStrikeGRU', 'MinNbrOfTargetsForOpportunisticTargetInGroupAirStrike', 'StrikeLimitations', 'AirplaneWaitForDecisionTime', 'ThreatOutOfCorridorDevaluationValue']]) + '>'


class TIAStratArtilleryStrikeConstantes:
    def __init__(self, ArtilleryStrikeSupportOffsetGRU=None, ArtilleryStrikeThreatBonusPerTags=None, ArtilleryRangeRatioPosition=None):
        self.ArtilleryStrikeSupportOffsetGRU = ArtilleryStrikeSupportOffsetGRU
        self.ArtilleryStrikeThreatBonusPerTags = ArtilleryStrikeThreatBonusPerTags
        self.ArtilleryRangeRatioPosition = ArtilleryRangeRatioPosition

    def __repr__(self):
        return f'<TIAStratArtilleryStrikeConstantes ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ArtilleryStrikeSupportOffsetGRU', 'ArtilleryStrikeThreatBonusPerTags', 'ArtilleryRangeRatioPosition']]) + '>'


class TIAStratVisionConstantes:
    def __init__(self, VisionParametersByDifficulty=None, VisionTestDefenseRatio=None, VisionTestHideUnitRatio=None):
        self.VisionParametersByDifficulty = VisionParametersByDifficulty
        self.VisionTestDefenseRatio = VisionTestDefenseRatio
        self.VisionTestHideUnitRatio = VisionTestHideUnitRatio

    def __repr__(self):
        return f'<TIAStratVisionConstantes ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['VisionParametersByDifficulty', 'VisionTestDefenseRatio', 'VisionTestHideUnitRatio']]) + '>'


class TMapSlicingConstantes:
    def __init__(self, NbPositionsPerPolygon=None, MaxNbUnitsPerPolygon=None, WaypointsInLightCoverTerrainTypes=None):
        self.NbPositionsPerPolygon = NbPositionsPerPolygon
        self.MaxNbUnitsPerPolygon = MaxNbUnitsPerPolygon
        self.WaypointsInLightCoverTerrainTypes = WaypointsInLightCoverTerrainTypes

    def __repr__(self):
        return f'<TMapSlicingConstantes ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['NbPositionsPerPolygon', 'MaxNbUnitsPerPolygon', 'WaypointsInLightCoverTerrainTypes']]) + '>'


class TFakeGunThreatDescriptor:
    def __init__(self, FakeThreatLifeTime=None, DistanceFromStartGRU=None, StepSize=None, DecalageAltitude=None, VisionRangeGRU=None, OwnerRatioForFakeGunThreat=None, GunList=None):
        self.FakeThreatLifeTime = FakeThreatLifeTime
        self.DistanceFromStartGRU = DistanceFromStartGRU
        self.StepSize = StepSize
        self.DecalageAltitude = DecalageAltitude
        self.VisionRangeGRU = VisionRangeGRU
        self.OwnerRatioForFakeGunThreat = OwnerRatioForFakeGunThreat
        self.GunList = GunList

    def __repr__(self):
        return f'<TFakeGunThreatDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['FakeThreatLifeTime', 'DistanceFromStartGRU', 'StepSize', 'DecalageAltitude', 'VisionRangeGRU', 'OwnerRatioForFakeGunThreat', 'GunList']]) + '>'


class TFakeGunDescriptor:
    def __init__(self, CurrentRangeGRU=None, TypeArme=None, IsPiercing=None, ColPlan=None, TirIndirect=None):
        self.CurrentRangeGRU = CurrentRangeGRU
        self.TypeArme = TypeArme
        self.IsPiercing = IsPiercing
        self.ColPlan = ColPlan
        self.TirIndirect = TirIndirect

    def __repr__(self):
        return f'<TFakeGunDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['CurrentRangeGRU', 'TypeArme', 'IsPiercing', 'ColPlan', 'TirIndirect']]) + '>'


class TDamageTypeRTTI:
    def __init__(self, Family=None, Index=None):
        self.Family = Family
        self.Index = Index

    def __repr__(self):
        return f'<TDamageTypeRTTI ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Family', 'Index']]) + '>'


class TIAStratVisionParameters:
    def __init__(self, KnowledgeTimerForAttackBehavior=None, UnitsKnowledge=None, KnowledgeMemoTimer=None):
        self.KnowledgeTimerForAttackBehavior = KnowledgeTimerForAttackBehavior
        self.UnitsKnowledge = UnitsKnowledge
        self.KnowledgeMemoTimer = KnowledgeMemoTimer

    def __repr__(self):
        return f'<TIAStratVisionParameters ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['KnowledgeTimerForAttackBehavior', 'UnitsKnowledge', 'KnowledgeMemoTimer']]) + '>'


class TIAStratWeaponConstantesDescriptor:
    def __init__(self, SafeDamageType=None, DamageWithMenaceForDangerounessArmor=None, AlwaysThreateningDamageFamily=None, MacroActionArtilleryDamageTypeThreat=None, AttackDamageTypeThreat=None, DamageTypeForPrincipalAmmo=None):
        self.SafeDamageType = SafeDamageType
        self.DamageWithMenaceForDangerounessArmor = DamageWithMenaceForDangerounessArmor
        self.AlwaysThreateningDamageFamily = AlwaysThreateningDamageFamily
        self.MacroActionArtilleryDamageTypeThreat = MacroActionArtilleryDamageTypeThreat
        self.AttackDamageTypeThreat = AttackDamageTypeThreat
        self.DamageTypeForPrincipalAmmo = DamageTypeForPrincipalAmmo

    def __repr__(self):
        return f'<TIAStratWeaponConstantesDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['SafeDamageType', 'DamageWithMenaceForDangerounessArmor', 'AlwaysThreateningDamageFamily', 'MacroActionArtilleryDamageTypeThreat', 'AttackDamageTypeThreat', 'DamageTypeForPrincipalAmmo']]) + '>'


class TInfluenceMapConstantesDescriptor:
    def __init__(self, DefaultDecay=None, DefaultMomentum=None, TailleDeCaseGRU=None, ManageInfluencePoints=None, MinValueInfluenceForOwnership=None, InfluenceMapName=None, EmptyCellDefaultOffset=None, UseMinValueForEmptyOwnerCell=None, SmoothDistance=None):
        self.DefaultDecay = DefaultDecay
        self.DefaultMomentum = DefaultMomentum
        self.TailleDeCaseGRU = TailleDeCaseGRU
        self.ManageInfluencePoints = ManageInfluencePoints
        self.MinValueInfluenceForOwnership = MinValueInfluenceForOwnership
        self.InfluenceMapName = InfluenceMapName
        self.EmptyCellDefaultOffset = EmptyCellDefaultOffset
        self.UseMinValueForEmptyOwnerCell = UseMinValueForEmptyOwnerCell
        self.SmoothDistance = SmoothDistance

    def __repr__(self):
        return f'<TInfluenceMapConstantesDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['DefaultDecay', 'DefaultMomentum', 'TailleDeCaseGRU', 'ManageInfluencePoints', 'MinValueInfluenceForOwnership', 'InfluenceMapName', 'EmptyCellDefaultOffset', 'UseMinValueForEmptyOwnerCell', 'SmoothDistance']]) + '>'


class TInfluenceMapDescriptors:
    def __init__(self, DecayActifUniquementEnPhaseDeCommandement=None, InfluenceMapDescriptor=None, ZoneInfluenceMapDescriptor=None):
        self.DecayActifUniquementEnPhaseDeCommandement = DecayActifUniquementEnPhaseDeCommandement
        self.InfluenceMapDescriptor = InfluenceMapDescriptor
        self.ZoneInfluenceMapDescriptor = ZoneInfluenceMapDescriptor

    def __repr__(self):
        return f'<TInfluenceMapDescriptors ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['DecayActifUniquementEnPhaseDeCommandement', 'InfluenceMapDescriptor', 'ZoneInfluenceMapDescriptor']]) + '>'


class TInfluenceMapConstantesSelector:
    def __init__(self, InfluenceConstByGameMode=None):
        self.InfluenceConstByGameMode = InfluenceConstByGameMode

    def __repr__(self):
        return f'<TInfluenceMapConstantesSelector ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['InfluenceConstByGameMode']]) + '>'


class TSupplyDescriptor:
    def __init__(self, DefaultSupplyRangeGRU=None, FuelSupplyBySecond=None, FuelSupplyCostBySecond=None, HealthSupplyBySecond=None, HealthSupplyCostBySecond=None, SupplySupplyBySecond=None, SupplySupplyCostBySecond=None, AmmunitionSupplyBySecond=None, CriticsSupplyBySecond=None, CriticsSupplyCostBySecond=None, FeedbackDrawer=None):
        self.DefaultSupplyRangeGRU = DefaultSupplyRangeGRU
        self.FuelSupplyBySecond = FuelSupplyBySecond
        self.FuelSupplyCostBySecond = FuelSupplyCostBySecond
        self.HealthSupplyBySecond = HealthSupplyBySecond
        self.HealthSupplyCostBySecond = HealthSupplyCostBySecond
        self.SupplySupplyBySecond = SupplySupplyBySecond
        self.SupplySupplyCostBySecond = SupplySupplyCostBySecond
        self.AmmunitionSupplyBySecond = AmmunitionSupplyBySecond
        self.CriticsSupplyBySecond = CriticsSupplyBySecond
        self.CriticsSupplyCostBySecond = CriticsSupplyCostBySecond
        self.FeedbackDrawer = FeedbackDrawer

    def __repr__(self):
        return f'<TSupplyDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['DefaultSupplyRangeGRU', 'FuelSupplyBySecond', 'FuelSupplyCostBySecond', 'HealthSupplyBySecond', 'HealthSupplyCostBySecond', 'SupplySupplyBySecond', 'SupplySupplyCostBySecond', 'AmmunitionSupplyBySecond', 'CriticsSupplyBySecond', 'CriticsSupplyCostBySecond', 'FeedbackDrawer']]) + '>'


class TSupplyFeedbackDrawer:
    def __init__(self, LineColor=None, ZOffset=None, LineThickness=None, FeedbackDescriptor=None):
        self.LineColor = LineColor
        self.ZOffset = ZOffset
        self.LineThickness = LineThickness
        self.FeedbackDescriptor = FeedbackDescriptor

    def __repr__(self):
        return f'<TSupplyFeedbackDrawer ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['LineColor', 'ZOffset', 'LineThickness', 'FeedbackDescriptor']]) + '>'


class TSupplyFeedbackDescriptor:
    def __init__(self, FeedbackScreenResilienceDuration=None, FeedbackFadeOutTime=None):
        self.FeedbackScreenResilienceDuration = FeedbackScreenResilienceDuration
        self.FeedbackFadeOutTime = FeedbackFadeOutTime

    def __repr__(self):
        return f'<TSupplyFeedbackDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['FeedbackScreenResilienceDuration', 'FeedbackFadeOutTime']]) + '>'


class TSpecificResourcesAccesser:
    def __init__(self, CommandPointResource=None, StrategicPointResource=None, TicketResource=None, FactoryResources=None):
        self.CommandPointResource = CommandPointResource
        self.StrategicPointResource = StrategicPointResource
        self.TicketResource = TicketResource
        self.FactoryResources = FactoryResources

    def __repr__(self):
        return f'<TSpecificResourcesAccesser ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['CommandPointResource', 'StrategicPointResource', 'TicketResource', 'FactoryResources']]) + '>'


class TNoiseDescriptor:
    def __init__(self, NoiseWaitTimeMin=None, NoiseWaitTimeMax=None, NoiseLerpTimeMin=None, NoiseLerpTimeMax=None):
        self.NoiseWaitTimeMin = NoiseWaitTimeMin
        self.NoiseWaitTimeMax = NoiseWaitTimeMax
        self.NoiseLerpTimeMin = NoiseLerpTimeMin
        self.NoiseLerpTimeMax = NoiseLerpTimeMax

    def __repr__(self):
        return f'<TNoiseDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['NoiseWaitTimeMin', 'NoiseWaitTimeMax', 'NoiseLerpTimeMin', 'NoiseLerpTimeMax']]) + '>'


class TSoldierAnimationDataDescriptor:
    def __init__(self, IdleLookProba=None, ProbaViolentDeath=None):
        self.IdleLookProba = IdleLookProba
        self.ProbaViolentDeath = ProbaViolentDeath

    def __repr__(self):
        return f'<TSoldierAnimationDataDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['IdleLookProba', 'ProbaViolentDeath']]) + '>'


class TSoldierSquadDataDescriptor:
    def __init__(self, OnHitProbaNormalWeapon=None, OnHitProbaOtherWeapon=None, FiringUnitRatio=None, DecalageSeFire=None):
        self.OnHitProbaNormalWeapon = OnHitProbaNormalWeapon
        self.OnHitProbaOtherWeapon = OnHitProbaOtherWeapon
        self.FiringUnitRatio = FiringUnitRatio
        self.DecalageSeFire = DecalageSeFire

    def __repr__(self):
        return f'<TSoldierSquadDataDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['OnHitProbaNormalWeapon', 'OnHitProbaOtherWeapon', 'FiringUnitRatio', 'DecalageSeFire']]) + '>'


class TColumnFormationDescriptor:
    def __init__(self, FrontWedgeDistanceFromLeaderGRU=None, BackWedgeDistanceFromLeaderGRU=None, InterSoldierDistanceGRU=None, WedgesAngle=None):
        self.FrontWedgeDistanceFromLeaderGRU = FrontWedgeDistanceFromLeaderGRU
        self.BackWedgeDistanceFromLeaderGRU = BackWedgeDistanceFromLeaderGRU
        self.InterSoldierDistanceGRU = InterSoldierDistanceGRU
        self.WedgesAngle = WedgesAngle

    def __repr__(self):
        return f'<TColumnFormationDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['FrontWedgeDistanceFromLeaderGRU', 'BackWedgeDistanceFromLeaderGRU', 'InterSoldierDistanceGRU', 'WedgesAngle']]) + '>'


class TLineFormationDescriptor:
    def __init__(self, InterSoldierDistanceGRU=None):
        self.InterSoldierDistanceGRU = InterSoldierDistanceGRU

    def __repr__(self):
        return f'<TLineFormationDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['InterSoldierDistanceGRU']]) + '>'


class TSoldierSquadMovementDataDescriptor:
    def __init__(self, NoiseMaxGRU=None, SoldierMaxAcceleration=None):
        self.NoiseMaxGRU = NoiseMaxGRU
        self.SoldierMaxAcceleration = SoldierMaxAcceleration

    def __repr__(self):
        return f'<TSoldierSquadMovementDataDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['NoiseMaxGRU', 'SoldierMaxAcceleration']]) + '>'


class TTransportConstantesDescriptor:
    def __init__(self, MaximalSpeedToUnload=None):
        self.MaximalSpeedToUnload = MaximalSpeedToUnload

    def __repr__(self):
        return f'<TTransportConstantesDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MaximalSpeedToUnload']]) + '>'


class TVisionConstantesDescriptor:
    def __init__(self, PorteeDeVisionGlobaleGRU=None):
        self.PorteeDeVisionGlobaleGRU = PorteeDeVisionGlobaleGRU

    def __repr__(self):
        return f'<TVisionConstantesDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['PorteeDeVisionGlobaleGRU']]) + '>'


class TWeaponConstantsDescriptor:
    def __init__(self, DefaultStressMultiplier=None, StressMultiplierPerDamageFamily=None, DefaultSuppressDamage=None, SuppressDamagePerFamily=None, ResistanceFamiliesNeedPiercing=None, PierceBonusForDamageFamilies=None, ResistanceToMimeticImpact=None, DefaultMimeticProjectile=None, DamageTypeToMimeticProjectile=None, BlindagesToIgnoreForDamageFamilies=None, EfficientShotMinAccuracy=None, EfficientShotMinPenetration=None, DefensiveSmokeRangeMaxGRU=None):
        self.DefaultStressMultiplier = DefaultStressMultiplier
        self.StressMultiplierPerDamageFamily = StressMultiplierPerDamageFamily
        self.DefaultSuppressDamage = DefaultSuppressDamage
        self.SuppressDamagePerFamily = SuppressDamagePerFamily
        self.ResistanceFamiliesNeedPiercing = ResistanceFamiliesNeedPiercing
        self.PierceBonusForDamageFamilies = PierceBonusForDamageFamilies
        self.ResistanceToMimeticImpact = ResistanceToMimeticImpact
        self.DefaultMimeticProjectile = DefaultMimeticProjectile
        self.DamageTypeToMimeticProjectile = DamageTypeToMimeticProjectile
        self.BlindagesToIgnoreForDamageFamilies = BlindagesToIgnoreForDamageFamilies
        self.EfficientShotMinAccuracy = EfficientShotMinAccuracy
        self.EfficientShotMinPenetration = EfficientShotMinPenetration
        self.DefensiveSmokeRangeMaxGRU = DefensiveSmokeRangeMaxGRU

    def __repr__(self):
        return f'<TWeaponConstantsDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['DefaultStressMultiplier', 'StressMultiplierPerDamageFamily', 'DefaultSuppressDamage', 'SuppressDamagePerFamily', 'ResistanceFamiliesNeedPiercing', 'PierceBonusForDamageFamilies', 'ResistanceToMimeticImpact', 'DefaultMimeticProjectile', 'DamageTypeToMimeticProjectile', 'BlindagesToIgnoreForDamageFamilies', 'EfficientShotMinAccuracy', 'EfficientShotMinPenetration', 'DefensiveSmokeRangeMaxGRU']]) + '>'


class TWeaponTypePrioritiesHolder:
    def __init__(self, WeaponTypes=None, DistanceToConsiderAsFarGRU=None, Score_OnRange=None, Score_OutOfRange=None):
        self.WeaponTypes = WeaponTypes
        self.DistanceToConsiderAsFarGRU = DistanceToConsiderAsFarGRU
        self.Score_OnRange = Score_OnRange
        self.Score_OutOfRange = Score_OutOfRange

    def __repr__(self):
        return f'<TWeaponTypePrioritiesHolder ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['WeaponTypes', 'DistanceToConsiderAsFarGRU', 'Score_OnRange', 'Score_OutOfRange']]) + '>'


class TWreckageConstantsDescriptor:
    def __init__(self, MultiplicateurMasseObstacle=None, DetruireQuandEcrase=None, ExploserQuandEcrase=None):
        self.MultiplicateurMasseObstacle = MultiplicateurMasseObstacle
        self.DetruireQuandEcrase = DetruireQuandEcrase
        self.ExploserQuandEcrase = ExploserQuandEcrase

    def __repr__(self):
        return f'<TWreckageConstantsDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MultiplicateurMasseObstacle', 'DetruireQuandEcrase', 'ExploserQuandEcrase']]) + '>'


class EAllianceStyleModernWarfare:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<EAllianceStyleModernWarfare>'


class EAutoresolveAdvantage:
    def __init__(self, Values=None):
        self.Values = Values

    def __repr__(self):
        return f'<EAutoresolveAdvantage ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Values']]) + '>'


class EIADifficulty:
    def __init__(self, Values=None):
        self.Values = Values

    def __repr__(self):
        return f'<EIADifficulty ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Values']]) + '>'


class TIADifficultyListConfiguration:
    def __init__(self, HumanIADifficulty=None, IAAnyDifficulty=None, DefaultIADifficulty=None, ScriptedDifficulty=None, IADifficultyList=None):
        self.HumanIADifficulty = HumanIADifficulty
        self.IAAnyDifficulty = IAAnyDifficulty
        self.DefaultIADifficulty = DefaultIADifficulty
        self.ScriptedDifficulty = ScriptedDifficulty
        self.IADifficultyList = IADifficultyList

    def __repr__(self):
        return f'<TIADifficultyListConfiguration ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['HumanIADifficulty', 'IAAnyDifficulty', 'DefaultIADifficulty', 'ScriptedDifficulty', 'IADifficultyList']]) + '>'


class TIADifficultyConfiguration:
    def __init__(self, IADifficultyHint=None, IAName=None, IADifficultyName=None):
        self.IADifficultyHint = IADifficultyHint
        self.IAName = IAName
        self.IADifficultyName = IADifficultyName

    def __repr__(self):
        return f'<TIADifficultyConfiguration ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['IADifficultyHint', 'IAName', 'IADifficultyName']]) + '>'


class EPlayerColor:
    def __init__(self, Values=None):
        self.Values = Values

    def __repr__(self):
        return f'<EPlayerColor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Values']]) + '>'


class TCombatAdvantageDefinition:
    def __init__(self, AdvantageValue=None, ShowTextForAdvantageWinner=None, HintToken=None, TextToken=None, TagToCheckAgainst=None, TagToCheck=None):
        self.AdvantageValue = AdvantageValue
        self.ShowTextForAdvantageWinner = ShowTextForAdvantageWinner
        self.HintToken = HintToken
        self.TextToken = TextToken
        self.TagToCheckAgainst = TagToCheckAgainst
        self.TagToCheck = TagToCheck

    def __repr__(self):
        return f'<TCombatAdvantageDefinition ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['AdvantageValue', 'ShowTextForAdvantageWinner', 'HintToken', 'TextToken', 'TagToCheckAgainst', 'TagToCheck']]) + '>'


class TStrategicAutoresolveAlea:
    def __init__(self, ModificationValue=None, TriggerWeight=None, TextToken=None):
        self.ModificationValue = ModificationValue
        self.TriggerWeight = TriggerWeight
        self.TextToken = TextToken

    def __repr__(self):
        return f'<TStrategicAutoresolveAlea ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ModificationValue', 'TriggerWeight', 'TextToken']]) + '>'


class TStrategicAutoResolveConstantes:
    def __init__(self, AleasByCombatType=None, PertesAttaquant=None, PertesDefenseur=None, PawnPowerBonusFactorByTerrainTypeAndPlayerSide=None, ApplyPawnPowerBonusOnSupportUnit=None, AvantagesByCombatType=None, CombatNoAntiAirAdvantageType=None, AirUnitTags=None, InfantryUnitTags=None, VictoryTypeByBalanceOfPowerByTerrainType=None, PertePourAttaquantSelonDecalageCombatAerien=None, PertePourDefenseurSelonDecalageCombatAerien=None, VictoryTypeByBalanceOfPowerCombatAerien=None, PertePourAttaquantSelonDecalageCombatSolAir=None, PertePourDefenseurSelonDecalageCombatSolAir=None, VictoryTypeByBalanceOfPowerCombatSolAir=None, PertePourAttaquantSelonDecalageCombatAirSol=None, PertePourDefenseurSelonDecalageCombatAirSol=None, VictoryTypeByBalanceOfPowerCombatAirSol=None, APLossForInterceptorAndPassingPawnByVictoryTypeForAttackerAirBattle=None, APLossForInterceptorAndPassingPawnByVictoryTypeForAttackerAirGroundBattle=None, APLossForInterceptorAndPassingPawnByVictoryTypeForAttackerGroundAirBattle=None):
        self.AleasByCombatType = AleasByCombatType
        self.PertesAttaquant = PertesAttaquant
        self.PertesDefenseur = PertesDefenseur
        self.PawnPowerBonusFactorByTerrainTypeAndPlayerSide = PawnPowerBonusFactorByTerrainTypeAndPlayerSide
        self.ApplyPawnPowerBonusOnSupportUnit = ApplyPawnPowerBonusOnSupportUnit
        self.AvantagesByCombatType = AvantagesByCombatType
        self.CombatNoAntiAirAdvantageType = CombatNoAntiAirAdvantageType
        self.AirUnitTags = AirUnitTags
        self.InfantryUnitTags = InfantryUnitTags
        self.VictoryTypeByBalanceOfPowerByTerrainType = VictoryTypeByBalanceOfPowerByTerrainType
        self.PertePourAttaquantSelonDecalageCombatAerien = PertePourAttaquantSelonDecalageCombatAerien
        self.PertePourDefenseurSelonDecalageCombatAerien = PertePourDefenseurSelonDecalageCombatAerien
        self.VictoryTypeByBalanceOfPowerCombatAerien = VictoryTypeByBalanceOfPowerCombatAerien
        self.PertePourAttaquantSelonDecalageCombatSolAir = PertePourAttaquantSelonDecalageCombatSolAir
        self.PertePourDefenseurSelonDecalageCombatSolAir = PertePourDefenseurSelonDecalageCombatSolAir
        self.VictoryTypeByBalanceOfPowerCombatSolAir = VictoryTypeByBalanceOfPowerCombatSolAir
        self.PertePourAttaquantSelonDecalageCombatAirSol = PertePourAttaquantSelonDecalageCombatAirSol
        self.PertePourDefenseurSelonDecalageCombatAirSol = PertePourDefenseurSelonDecalageCombatAirSol
        self.VictoryTypeByBalanceOfPowerCombatAirSol = VictoryTypeByBalanceOfPowerCombatAirSol
        self.APLossForInterceptorAndPassingPawnByVictoryTypeForAttackerAirBattle = APLossForInterceptorAndPassingPawnByVictoryTypeForAttackerAirBattle
        self.APLossForInterceptorAndPassingPawnByVictoryTypeForAttackerAirGroundBattle = APLossForInterceptorAndPassingPawnByVictoryTypeForAttackerAirGroundBattle
        self.APLossForInterceptorAndPassingPawnByVictoryTypeForAttackerGroundAirBattle = APLossForInterceptorAndPassingPawnByVictoryTypeForAttackerGroundAirBattle

    def __repr__(self):
        return f'<TStrategicAutoResolveConstantes ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['AleasByCombatType', 'PertesAttaquant', 'PertesDefenseur', 'PawnPowerBonusFactorByTerrainTypeAndPlayerSide', 'ApplyPawnPowerBonusOnSupportUnit', 'AvantagesByCombatType', 'CombatNoAntiAirAdvantageType', 'AirUnitTags', 'InfantryUnitTags', 'VictoryTypeByBalanceOfPowerByTerrainType', 'PertePourAttaquantSelonDecalageCombatAerien', 'PertePourDefenseurSelonDecalageCombatAerien', 'VictoryTypeByBalanceOfPowerCombatAerien', 'PertePourAttaquantSelonDecalageCombatSolAir', 'PertePourDefenseurSelonDecalageCombatSolAir', 'VictoryTypeByBalanceOfPowerCombatSolAir', 'PertePourAttaquantSelonDecalageCombatAirSol', 'PertePourDefenseurSelonDecalageCombatAirSol', 'VictoryTypeByBalanceOfPowerCombatAirSol', 'APLossForInterceptorAndPassingPawnByVictoryTypeForAttackerAirBattle', 'APLossForInterceptorAndPassingPawnByVictoryTypeForAttackerAirGroundBattle', 'APLossForInterceptorAndPassingPawnByVictoryTypeForAttackerGroundAirBattle']]) + '>'


class TIAStratStrategicConstantesDescriptor:
    def __init__(self, NbAirplanesToKeepBeforeUsingAirDeny=None, NbAirplanesToKeepBeforeUsingBombard=None, DistanceMaxToAssignPawnToExistingGroupGRU=None, DistanceMaxForPawnToBeAvailableForCurrentObjectiveGRU=None, MaxCellsDistanceFromFrontlineAllowedOutOfSupply=None, MaxFatigueToBeSelectedForStrategicBattle=None, AttackAndDefensePowerRatioForAttackersToMoveBack=None, PawnWithTagToPlaceFarthestFromEnemy=None, StartBattleDescriptorByType=None, BombardTargetMinimumPowerValue=None, DefenseBonusByTerrainType=None, TerrainThatGenerateDefensePoint=None, DistanceInCellsFromEnemiesToActivateInnerDefensePoints=None, MinAttackPowerToAttackInPriority=None, PrioritaryAttackTargetMaxDistanceFromFrontLine=None, DefaultRankForPrioritaryDefensePoint=None, NumberPositionRankToPlaceUnits=None, MinimumRankForWeakestBattleUnitDefensePoint=None, MinimumRankForStrongestBattleUnitDefensePoint=None, MinimumRankForWeakestBattleUnitAttackPoint=None, MinimumRankForStrongestBattleUnitAttackPoint=None, MinimumRankForSupportUnit=None, GroupPoolsSortedByPriority=None, PawnBattleRolesToCoverWithSupport=None):
        self.NbAirplanesToKeepBeforeUsingAirDeny = NbAirplanesToKeepBeforeUsingAirDeny
        self.NbAirplanesToKeepBeforeUsingBombard = NbAirplanesToKeepBeforeUsingBombard
        self.DistanceMaxToAssignPawnToExistingGroupGRU = DistanceMaxToAssignPawnToExistingGroupGRU
        self.DistanceMaxForPawnToBeAvailableForCurrentObjectiveGRU = DistanceMaxForPawnToBeAvailableForCurrentObjectiveGRU
        self.MaxCellsDistanceFromFrontlineAllowedOutOfSupply = MaxCellsDistanceFromFrontlineAllowedOutOfSupply
        self.MaxFatigueToBeSelectedForStrategicBattle = MaxFatigueToBeSelectedForStrategicBattle
        self.AttackAndDefensePowerRatioForAttackersToMoveBack = AttackAndDefensePowerRatioForAttackersToMoveBack
        self.PawnWithTagToPlaceFarthestFromEnemy = PawnWithTagToPlaceFarthestFromEnemy
        self.StartBattleDescriptorByType = StartBattleDescriptorByType
        self.BombardTargetMinimumPowerValue = BombardTargetMinimumPowerValue
        self.DefenseBonusByTerrainType = DefenseBonusByTerrainType
        self.TerrainThatGenerateDefensePoint = TerrainThatGenerateDefensePoint
        self.DistanceInCellsFromEnemiesToActivateInnerDefensePoints = DistanceInCellsFromEnemiesToActivateInnerDefensePoints
        self.MinAttackPowerToAttackInPriority = MinAttackPowerToAttackInPriority
        self.PrioritaryAttackTargetMaxDistanceFromFrontLine = PrioritaryAttackTargetMaxDistanceFromFrontLine
        self.DefaultRankForPrioritaryDefensePoint = DefaultRankForPrioritaryDefensePoint
        self.NumberPositionRankToPlaceUnits = NumberPositionRankToPlaceUnits
        self.MinimumRankForWeakestBattleUnitDefensePoint = MinimumRankForWeakestBattleUnitDefensePoint
        self.MinimumRankForStrongestBattleUnitDefensePoint = MinimumRankForStrongestBattleUnitDefensePoint
        self.MinimumRankForWeakestBattleUnitAttackPoint = MinimumRankForWeakestBattleUnitAttackPoint
        self.MinimumRankForStrongestBattleUnitAttackPoint = MinimumRankForStrongestBattleUnitAttackPoint
        self.MinimumRankForSupportUnit = MinimumRankForSupportUnit
        self.GroupPoolsSortedByPriority = GroupPoolsSortedByPriority
        self.PawnBattleRolesToCoverWithSupport = PawnBattleRolesToCoverWithSupport

    def __repr__(self):
        return f'<TIAStratStrategicConstantesDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['NbAirplanesToKeepBeforeUsingAirDeny', 'NbAirplanesToKeepBeforeUsingBombard', 'DistanceMaxToAssignPawnToExistingGroupGRU', 'DistanceMaxForPawnToBeAvailableForCurrentObjectiveGRU', 'MaxCellsDistanceFromFrontlineAllowedOutOfSupply', 'MaxFatigueToBeSelectedForStrategicBattle', 'AttackAndDefensePowerRatioForAttackersToMoveBack', 'PawnWithTagToPlaceFarthestFromEnemy', 'StartBattleDescriptorByType', 'BombardTargetMinimumPowerValue', 'DefenseBonusByTerrainType', 'TerrainThatGenerateDefensePoint', 'DistanceInCellsFromEnemiesToActivateInnerDefensePoints', 'MinAttackPowerToAttackInPriority', 'PrioritaryAttackTargetMaxDistanceFromFrontLine', 'DefaultRankForPrioritaryDefensePoint', 'NumberPositionRankToPlaceUnits', 'MinimumRankForWeakestBattleUnitDefensePoint', 'MinimumRankForStrongestBattleUnitDefensePoint', 'MinimumRankForWeakestBattleUnitAttackPoint', 'MinimumRankForStrongestBattleUnitAttackPoint', 'MinimumRankForSupportUnit', 'GroupPoolsSortedByPriority', 'PawnBattleRolesToCoverWithSupport']]) + '>'


class TIAStartBattleDescriptor:
    def __init__(self, MinVictoryNeededToAttackForObjectiveStatus=None):
        self.MinVictoryNeededToAttackForObjectiveStatus = MinVictoryNeededToAttackForObjectiveStatus

    def __repr__(self):
        return f'<TIAStartBattleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MinVictoryNeededToAttackForObjectiveStatus']]) + '>'


class TIAGroupPool:
    def __init__(self, ZoneStatus=None, Validators=None, Behaviors=None, PossibleTags=None, Elements=None, Name=None):
        self.ZoneStatus = ZoneStatus
        self.Validators = Validators
        self.Behaviors = Behaviors
        self.PossibleTags = PossibleTags
        self.Elements = Elements
        self.Name = Name

    def __repr__(self):
        return f'<TIAGroupPool ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ZoneStatus', 'Validators', 'Behaviors', 'PossibleTags', 'Elements', 'Name']]) + '>'


class TIAGroupValidator:
    def __init__(self, ExcludedTags=None, BattleRole=None, PawnsCount=None):
        self.ExcludedTags = ExcludedTags
        self.BattleRole = BattleRole
        self.PawnsCount = PawnsCount

    def __repr__(self):
        return f'<TIAGroupValidator ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ExcludedTags', 'BattleRole', 'PawnsCount']]) + '>'


class TIAGroupPoolElement:
    def __init__(self, Comparator=None, PawnsCountByObjectiveWeight=None):
        self.Comparator = Comparator
        self.PawnsCountByObjectiveWeight = PawnsCountByObjectiveWeight

    def __repr__(self):
        return f'<TIAGroupPoolElement ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Comparator', 'PawnsCountByObjectiveWeight']]) + '>'


class TIAPawnsBehavior:
    def __init__(self, Placement=None, EndTurn=None, Filter=None, PreBattle=None):
        self.Placement = Placement
        self.EndTurn = EndTurn
        self.Filter = Filter
        self.PreBattle = PreBattle

    def __repr__(self):
        return f'<TIAPawnsBehavior ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Placement', 'EndTurn', 'Filter', 'PreBattle']]) + '>'


class TIAPawnsBehaviorFilterExhausted:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TIAPawnsBehaviorFilterExhausted>'


class TIAPawnsBehaviorExhaustedPlacement:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TIAPawnsBehaviorExhaustedPlacement>'


class TIAPawnsBehaviorFilterNotSupplied:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TIAPawnsBehaviorFilterNotSupplied>'


class TIAPawnsBehaviorNotSuppliedPlacement:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TIAPawnsBehaviorNotSuppliedPlacement>'


class TIAPawnsBehaviorFilterArtillery:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TIAPawnsBehaviorFilterArtillery>'


class TIAPawnsBehaviorArtilleryEndTurn:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TIAPawnsBehaviorArtilleryEndTurn>'


class TIAPawnsBehaviorFilterAntiAir:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TIAPawnsBehaviorFilterAntiAir>'


class TIAPawnsBehaviorAntiAirPlacement:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TIAPawnsBehaviorAntiAirPlacement>'


class TIAPawnsBehaviorAntiAirPreBattle:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TIAPawnsBehaviorAntiAirPreBattle>'


class TIAPawnsBehaviorAntiAirEndTurn:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TIAPawnsBehaviorAntiAirEndTurn>'


class TIAPawnsBehaviorFilterPawnsWithTargetToAttack:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TIAPawnsBehaviorFilterPawnsWithTargetToAttack>'


class TIAPawnsBehaviorAttackTargetPlacement:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TIAPawnsBehaviorAttackTargetPlacement>'


class TIAPawnsBehaviorFilterAcceptEveryPawns:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TIAPawnsBehaviorFilterAcceptEveryPawns>'


class TIAPawnsBehaviorAttackPlacement:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TIAPawnsBehaviorAttackPlacement>'


class TIAPawnsBehaviorDefensePlacement:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TIAPawnsBehaviorDefensePlacement>'


class TIAPawnsBehaviorFilterPawnsWithoutInfluence:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TIAPawnsBehaviorFilterPawnsWithoutInfluence>'


class TIAPawnsBehaviorMoveWithoutInfluenceEndTurn:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TIAPawnsBehaviorMoveWithoutInfluenceEndTurn>'


class TStrategicCameraConstantesDescriptor:
    def __init__(self, GoingBackDuration=None, GoBackWithStraightPath=None, IdleAltitude=None, FollowAltitude=None, OrderSpecificBehavior=None, IdleSite=None):
        self.GoingBackDuration = GoingBackDuration
        self.GoBackWithStraightPath = GoBackWithStraightPath
        self.IdleAltitude = IdleAltitude
        self.FollowAltitude = FollowAltitude
        self.OrderSpecificBehavior = OrderSpecificBehavior
        self.IdleSite = IdleSite

    def __repr__(self):
        return f'<TStrategicCameraConstantesDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['GoingBackDuration', 'GoBackWithStraightPath', 'IdleAltitude', 'FollowAltitude', 'OrderSpecificBehavior', 'IdleSite']]) + '>'


class TArmoryConstantes:
    def __init__(self, HalfSeparationEntreDeuxUnitSiDeuxUnit=None):
        self.HalfSeparationEntreDeuxUnitSiDeuxUnit = HalfSeparationEntreDeuxUnitSiDeuxUnit

    def __repr__(self):
        return f'<TArmoryConstantes ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['HalfSeparationEntreDeuxUnitSiDeuxUnit']]) + '>'


class TDeckGeneratorContainer:
    def __init__(self, DeckNameToGenerator=None):
        self.DeckNameToGenerator = DeckNameToGenerator

    def __repr__(self):
        return f'<TDeckGeneratorContainer ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['DeckNameToGenerator']]) + '>'


class TDeckGroupRules:
    def __init__(self, MaxNbSmartGroupByCombatGroup=None, MaxNbPackBySmartGroup=None, CanUseSamePackInSameSmartGroupSlot=None, MaxNbCombatGroupForGameMode=None, CombatGroupDefaultName=None, SmartGroupDefaultName=None, SmartGroupLeaderGradeList=None):
        self.MaxNbSmartGroupByCombatGroup = MaxNbSmartGroupByCombatGroup
        self.MaxNbPackBySmartGroup = MaxNbPackBySmartGroup
        self.CanUseSamePackInSameSmartGroupSlot = CanUseSamePackInSameSmartGroupSlot
        self.MaxNbCombatGroupForGameMode = MaxNbCombatGroupForGameMode
        self.CombatGroupDefaultName = CombatGroupDefaultName
        self.SmartGroupDefaultName = SmartGroupDefaultName
        self.SmartGroupLeaderGradeList = SmartGroupLeaderGradeList

    def __repr__(self):
        return f'<TDeckGroupRules ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MaxNbSmartGroupByCombatGroup', 'MaxNbPackBySmartGroup', 'CanUseSamePackInSameSmartGroupSlot', 'MaxNbCombatGroupForGameMode', 'CombatGroupDefaultName', 'SmartGroupDefaultName', 'SmartGroupLeaderGradeList']]) + '>'


class TFeedbackMessageDispatcher:
    def __init__(self, UnitAcknowDescriptor=None):
        self.UnitAcknowDescriptor = UnitAcknowDescriptor

    def __repr__(self):
        return f'<TFeedbackMessageDispatcher ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['UnitAcknowDescriptor']]) + '>'


class TModernWarfarePlayerXPCalculatorDescriptor:
    def __init__(self, XPMultiplierByVictoryType=None, XPMultiplierSkirmish=None, XPMultiplierMulti=None, XPMultiplierRanked=None, GameDurationInMinForMaxXP=None, MaxGameDurationXP=None, MaxWinstreakMultiplier=None):
        self.XPMultiplierByVictoryType = XPMultiplierByVictoryType
        self.XPMultiplierSkirmish = XPMultiplierSkirmish
        self.XPMultiplierMulti = XPMultiplierMulti
        self.XPMultiplierRanked = XPMultiplierRanked
        self.GameDurationInMinForMaxXP = GameDurationInMinForMaxXP
        self.MaxGameDurationXP = MaxGameDurationXP
        self.MaxWinstreakMultiplier = MaxWinstreakMultiplier

    def __repr__(self):
        return f'<TModernWarfarePlayerXPCalculatorDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['XPMultiplierByVictoryType', 'XPMultiplierSkirmish', 'XPMultiplierMulti', 'XPMultiplierRanked', 'GameDurationInMinForMaxXP', 'MaxGameDurationXP', 'MaxWinstreakMultiplier']]) + '>'


class TAllUnits:
    def __init__(self, PlayableUnitsByWorld=None):
        self.PlayableUnitsByWorld = PlayableUnitsByWorld

    def __repr__(self):
        return f'<TAllUnits ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['PlayableUnitsByWorld']]) + '>'


class TActionCall:
    def __init__(self, Par_Fumigene_Alpha=None, NamedParams=None, Par_Fumigene_Color=None, Action=None):
        self.Par_Fumigene_Alpha = Par_Fumigene_Alpha
        self.NamedParams = NamedParams
        self.Par_Fumigene_Color = Par_Fumigene_Color
        self.Action = Action

    def __repr__(self):
        return f'<TActionCall ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Par_Fumigene_Alpha', 'NamedParams', 'Par_Fumigene_Color', 'Action']]) + '>'


class TPinnableValue:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TPinnableValue>'


class TGamePhaseManagerDescriptor:
    def __init__(self, InitPhaseType=None, GamePhaseDescriptorList=None):
        self.InitPhaseType = InitPhaseType
        self.GamePhaseDescriptorList = GamePhaseDescriptorList

    def __repr__(self):
        return f'<TGamePhaseManagerDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['InitPhaseType', 'GamePhaseDescriptorList']]) + '>'


class TStrategicGamePhaseDescriptor:
    def __init__(self, GamePhaseType=None):
        self.GamePhaseType = GamePhaseType

    def __repr__(self):
        return f'<TStrategicGamePhaseDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['GamePhaseType']]) + '>'


class TWargameGamePhaseDescriptor:
    def __init__(self, GamePhaseType=None):
        self.GamePhaseType = GamePhaseType

    def __repr__(self):
        return f'<TWargameGamePhaseDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['GamePhaseType']]) + '>'


class TDeploiementGamePhaseDescriptor:
    def __init__(self, GamePhaseType=None, ListeProprietesTempsGrace=None):
        self.GamePhaseType = GamePhaseType
        self.ListeProprietesTempsGrace = ListeProprietesTempsGrace

    def __repr__(self):
        return f'<TDeploiementGamePhaseDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['GamePhaseType', 'ListeProprietesTempsGrace']]) + '>'


class TDeploiementGracePeriodDescriptor:
    def __init__(self, StepList=None, TempsGracePourTimerEnSecond=None):
        self.StepList = StepList
        self.TempsGracePourTimerEnSecond = TempsGracePourTimerEnSecond

    def __repr__(self):
        return f'<TDeploiementGracePeriodDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['StepList', 'TempsGracePourTimerEnSecond']]) + '>'


class TGracePeriodStepForDeploiementTimer:
    def __init__(self, MultiplicateurTempsGrace=None, TempsMaxEnSecondes=None):
        self.MultiplicateurTempsGrace = MultiplicateurTempsGrace
        self.TempsMaxEnSecondes = TempsMaxEnSecondes

    def __repr__(self):
        return f'<TGracePeriodStepForDeploiementTimer ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MultiplicateurTempsGrace', 'TempsMaxEnSecondes']]) + '>'


class TMissileCarriageConnoisseurHandler:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TMissileCarriageConnoisseurHandler>'


class TReinforcementManager:
    def __init__(self, ReinforcementColor=None, RoadSnapDistanceInLBU=None, LandCorridorTextOffset=None, AerialCorridorTextOffset=None):
        self.ReinforcementColor = ReinforcementColor
        self.RoadSnapDistanceInLBU = RoadSnapDistanceInLBU
        self.LandCorridorTextOffset = LandCorridorTextOffset
        self.AerialCorridorTextOffset = AerialCorridorTextOffset

    def __repr__(self):
        return f'<TReinforcementManager ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ReinforcementColor', 'RoadSnapDistanceInLBU', 'LandCorridorTextOffset', 'AerialCorridorTextOffset']]) + '>'


class TReverseScannerWithIdentificationDescriptor:
    def __init__(self, VisibilityRollRule=None):
        self.VisibilityRollRule = VisibilityRollRule

    def __repr__(self):
        return f'<TReverseScannerWithIdentificationDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['VisibilityRollRule']]) + '>'


class TModernWarfareVisibilityRollRule:
    def __init__(self, DistanceMultiplierRule=None, VisibilityRuleDescriptor=None, TimeBetweenEachIdentifyRoll=None, IdentifyBaseProbability=None):
        self.DistanceMultiplierRule = DistanceMultiplierRule
        self.VisibilityRuleDescriptor = VisibilityRuleDescriptor
        self.TimeBetweenEachIdentifyRoll = TimeBetweenEachIdentifyRoll
        self.IdentifyBaseProbability = IdentifyBaseProbability

    def __repr__(self):
        return f'<TModernWarfareVisibilityRollRule ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['DistanceMultiplierRule', 'VisibilityRuleDescriptor', 'TimeBetweenEachIdentifyRoll', 'IdentifyBaseProbability']]) + '>'


class TModernWarfareDistanceMultiplierRollRuleDescriptor:
    def __init__(self, Exposant=None, MultiplicateurAPorteeMinimaleEnMouvement=None, MultiplicateurAPorteeMaximaleEnMouvement=None, MultiplicateurAPorteeMaximale=None, MultiplicateurAPorteeMinimale=None, ExposantEnMouvement=None):
        self.Exposant = Exposant
        self.MultiplicateurAPorteeMinimaleEnMouvement = MultiplicateurAPorteeMinimaleEnMouvement
        self.MultiplicateurAPorteeMaximaleEnMouvement = MultiplicateurAPorteeMaximaleEnMouvement
        self.MultiplicateurAPorteeMaximale = MultiplicateurAPorteeMaximale
        self.MultiplicateurAPorteeMinimale = MultiplicateurAPorteeMinimale
        self.ExposantEnMouvement = ExposantEnMouvement

    def __repr__(self):
        return f'<TModernWarfareDistanceMultiplierRollRuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Exposant', 'MultiplicateurAPorteeMinimaleEnMouvement', 'MultiplicateurAPorteeMaximaleEnMouvement', 'MultiplicateurAPorteeMaximale', 'MultiplicateurAPorteeMinimale', 'ExposantEnMouvement']]) + '>'


class TScannerConfigurationDescriptor:
    def __init__(self, DetectionTBAGRU=None, SpecializedOpticalStrengths=None, OpticalStrength=None, OpticsAltitudeConfig=None, PorteeIdentification=None, PorteeVisionFOWGRU=None, OpticalStrengthAltitude=None, PorteeVisionGRU=None, PorteeVisionTBAGRU=None, SpecializedDetectionsGRU=None):
        self.DetectionTBAGRU = DetectionTBAGRU
        self.SpecializedOpticalStrengths = SpecializedOpticalStrengths
        self.OpticalStrength = OpticalStrength
        self.OpticsAltitudeConfig = OpticsAltitudeConfig
        self.PorteeIdentification = PorteeIdentification
        self.PorteeVisionFOWGRU = PorteeVisionFOWGRU
        self.OpticalStrengthAltitude = OpticalStrengthAltitude
        self.PorteeVisionGRU = PorteeVisionGRU
        self.PorteeVisionTBAGRU = PorteeVisionTBAGRU
        self.SpecializedDetectionsGRU = SpecializedDetectionsGRU

    def __repr__(self):
        return f'<TScannerConfigurationDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['DetectionTBAGRU', 'SpecializedOpticalStrengths', 'OpticalStrength', 'OpticsAltitudeConfig', 'PorteeIdentification', 'PorteeVisionFOWGRU', 'OpticalStrengthAltitude', 'PorteeVisionGRU', 'PorteeVisionTBAGRU', 'SpecializedDetectionsGRU']]) + '>'


class TModernWarfareVisibilityRollRuleDescriptor:
    def __init__(self, PourcentageCourteDistance=None, PourcentageMoyenneDistance=None, ModificateurCourteDistance=None, ModificateurMoyenneDistance=None, ModificateurLongueDistance=None, Time1ForReIdentModificateur=None, Time2ForReIdentModificateur=None, Time3ForReIdentModificateur=None, ModificateurReIdentAvantTime1=None, ModificateurReIdentAvantTime2=None, ModificateurReIdentAvantTime3=None, ModificateurCibleEnMouvement=None, ModificateurPlusieursIdentSuccessive=None):
        self.PourcentageCourteDistance = PourcentageCourteDistance
        self.PourcentageMoyenneDistance = PourcentageMoyenneDistance
        self.ModificateurCourteDistance = ModificateurCourteDistance
        self.ModificateurMoyenneDistance = ModificateurMoyenneDistance
        self.ModificateurLongueDistance = ModificateurLongueDistance
        self.Time1ForReIdentModificateur = Time1ForReIdentModificateur
        self.Time2ForReIdentModificateur = Time2ForReIdentModificateur
        self.Time3ForReIdentModificateur = Time3ForReIdentModificateur
        self.ModificateurReIdentAvantTime1 = ModificateurReIdentAvantTime1
        self.ModificateurReIdentAvantTime2 = ModificateurReIdentAvantTime2
        self.ModificateurReIdentAvantTime3 = ModificateurReIdentAvantTime3
        self.ModificateurCibleEnMouvement = ModificateurCibleEnMouvement
        self.ModificateurPlusieursIdentSuccessive = ModificateurPlusieursIdentSuccessive

    def __repr__(self):
        return f'<TModernWarfareVisibilityRollRuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['PourcentageCourteDistance', 'PourcentageMoyenneDistance', 'ModificateurCourteDistance', 'ModificateurMoyenneDistance', 'ModificateurLongueDistance', 'Time1ForReIdentModificateur', 'Time2ForReIdentModificateur', 'Time3ForReIdentModificateur', 'ModificateurReIdentAvantTime1', 'ModificateurReIdentAvantTime2', 'ModificateurReIdentAvantTime3', 'ModificateurCibleEnMouvement', 'ModificateurPlusieursIdentSuccessive']]) + '>'


class TWorldConstantes:
    def __init__(self, HelperVisibility=None):
        self.HelperVisibility = HelperVisibility

    def __repr__(self):
        return f'<TWorldConstantes ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['HelperVisibility']]) + '>'


class TWorldInterfaceDescriptorSelector:
    def __init__(self, DescriptorsByName=None):
        self.DescriptorsByName = DescriptorsByName

    def __repr__(self):
        return f'<TWorldInterfaceDescriptorSelector ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['DescriptorsByName']]) + '>'


class TWorldInterfaceDescriptor:
    def __init__(self, GamePhaseManagerDescriptor=None, World3D=None, ZoneManagerDescriptors=None, SoundAndMusicSwitchDescriptor=None):
        self.GamePhaseManagerDescriptor = GamePhaseManagerDescriptor
        self.World3D = World3D
        self.ZoneManagerDescriptors = ZoneManagerDescriptors
        self.SoundAndMusicSwitchDescriptor = SoundAndMusicSwitchDescriptor

    def __repr__(self):
        return f'<TWorldInterfaceDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['GamePhaseManagerDescriptor', 'World3D', 'ZoneManagerDescriptors', 'SoundAndMusicSwitchDescriptor']]) + '>'


class TZoneNamesDico:
    def __init__(self, CampToZoneNames=None):
        self.CampToZoneNames = CampToZoneNames

    def __repr__(self):
        return f'<TZoneNamesDico ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['CampToZoneNames']]) + '>'


class TDeploiementZoneManagerDescriptor:
    def __init__(self, AreaManagerProxy=None, ZoneNamesDico=None):
        self.AreaManagerProxy = AreaManagerProxy
        self.ZoneNamesDico = ZoneNamesDico

    def __repr__(self):
        return f'<TDeploiementZoneManagerDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['AreaManagerProxy', 'ZoneNamesDico']]) + '>'


class TCommandementZoneManagerDescriptor:
    def __init__(self, AreaManagerProxy=None, ZoneNamesDico=None):
        self.AreaManagerProxy = AreaManagerProxy
        self.ZoneNamesDico = ZoneNamesDico

    def __repr__(self):
        return f'<TCommandementZoneManagerDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['AreaManagerProxy', 'ZoneNamesDico']]) + '>'


class TZoneManagerForIAStratDescriptor:
    def __init__(self, AreaManagerProxy=None):
        self.AreaManagerProxy = AreaManagerProxy

    def __repr__(self):
        return f'<TZoneManagerForIAStratDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['AreaManagerProxy']]) + '>'


class TStrategicIAZoneManagerDescriptor:
    def __init__(self, AreaManagerProxy=None):
        self.AreaManagerProxy = AreaManagerProxy

    def __repr__(self):
        return f'<TStrategicIAZoneManagerDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['AreaManagerProxy']]) + '>'


class TNDFTransactionFileList:
    def __init__(self, Files=None):
        self.Files = Files

    def __repr__(self):
        return f'<TNDFTransactionFileList ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Files']]) + '>'


class TResourceMultiMaterialMesh:
    def __init__(self, FileName=None):
        self.FileName = FileName

    def __repr__(self):
        return f'<TResourceMultiMaterialMesh ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['FileName']]) + '>'


class CommonMeshDesc:
    def __init__(self, ModelFile=None):
        self.ModelFile = ModelFile

    def __repr__(self):
        return f'<CommonMeshDesc ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ModelFile']]) + '>'


class TResourceMatrixArrayAnimation:
    def __init__(self, FileName=None, PlayInLoop=None):
        self.FileName = FileName
        self.PlayInLoop = PlayInLoop

    def __repr__(self):
        return f'<TResourceMatrixArrayAnimation ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['FileName', 'PlayInLoop']]) + '>'


class DepictionOperator_AnimationDeployable:
    def __init__(self, DeployAnimation=None, FoldAnimation=None, IdleAnimation=None, MoveFrontAnimation=None, MoveBackAnimation=None, DeployFromMoveTime=None, DeployFromTurnTime=None, FoldForMoveTime=None, FoldForTurnTime=None):
        self.DeployAnimation = DeployAnimation
        self.FoldAnimation = FoldAnimation
        self.IdleAnimation = IdleAnimation
        self.MoveFrontAnimation = MoveFrontAnimation
        self.MoveBackAnimation = MoveBackAnimation
        self.DeployFromMoveTime = DeployFromMoveTime
        self.DeployFromTurnTime = DeployFromTurnTime
        self.FoldForMoveTime = FoldForMoveTime
        self.FoldForTurnTime = FoldForTurnTime

    def __repr__(self):
        return f'<DepictionOperator_AnimationDeployable ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['DeployAnimation', 'FoldAnimation', 'IdleAnimation', 'MoveFrontAnimation', 'MoveBackAnimation', 'DeployFromMoveTime', 'DeployFromTurnTime', 'FoldForMoveTime', 'FoldForTurnTime']]) + '>'


class TModuleSelector:
    def __init__(self, Selection=None, Default=None):
        self.Selection = Selection
        self.Default = Default

    def __repr__(self):
        return f'<TModuleSelector ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Selection', 'Default']]) + '>'


class TTargetCoordinatorModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TTargetCoordinatorModuleDescriptor>'


class TCoatingKitchen:
    def __init__(self, Cookbook=None, Pantry=None):
        self.Cookbook = Cookbook
        self.Pantry = Pantry

    def __repr__(self):
        return f'<TCoatingKitchen ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Cookbook', 'Pantry']]) + '>'


class TCoatingCookbook:
    def __init__(self, Recipes=None):
        self.Recipes = Recipes

    def __repr__(self):
        return f'<TCoatingCookbook ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Recipes']]) + '>'


class TCoatingRecipe:
    def __init__(self, Ingredients=None):
        self.Ingredients = Ingredients

    def __repr__(self):
        return f'<TCoatingRecipe ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Ingredients']]) + '>'


class TCoatingPantry:
    def __init__(self, Entries=None):
        self.Entries = Entries

    def __repr__(self):
        return f'<TCoatingPantry ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Entries']]) + '>'


class TCoatingIngredientOperator:
    def __init__(self, Descriptor=None):
        self.Descriptor = Descriptor

    def __repr__(self):
        return f'<TCoatingIngredientOperator ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Descriptor']]) + '>'


class TCosmeticTrapdoorOperatorDesc:
    def __init__(self, TrapdoorList=None, LoadSupportBoneName=None, LimitTranslationInMeter=None, TranslationDurationInSec=None, TrapdoorOpeningDurationInSec=None):
        self.TrapdoorList = TrapdoorList
        self.LoadSupportBoneName = LoadSupportBoneName
        self.LimitTranslationInMeter = LimitTranslationInMeter
        self.TranslationDurationInSec = TranslationDurationInSec
        self.TrapdoorOpeningDurationInSec = TrapdoorOpeningDurationInSec

    def __repr__(self):
        return f'<TCosmeticTrapdoorOperatorDesc ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TrapdoorList', 'LoadSupportBoneName', 'LimitTranslationInMeter', 'TranslationDurationInSec', 'TrapdoorOpeningDurationInSec']]) + '>'


class TTrapdoor:
    def __init__(self, LimitAngleInDegree=None, TrapdoorBoneName=None):
        self.LimitAngleInDegree = LimitAngleInDegree
        self.TrapdoorBoneName = TrapdoorBoneName

    def __repr__(self):
        return f'<TTrapdoor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['LimitAngleInDegree', 'TrapdoorBoneName']]) + '>'


class TCosmeticOffsetTurretWhileMovingOperatorDesc:
    def __init__(self, AngleInDegree=None):
        self.AngleInDegree = AngleInDegree

    def __repr__(self):
        return f'<TCosmeticOffsetTurretWhileMovingOperatorDesc ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['AngleInDegree']]) + '>'


class TCosmeticLandingGearOperatorDesc:
    def __init__(self, AnimationList=None):
        self.AnimationList = AnimationList

    def __repr__(self):
        return f'<TCosmeticLandingGearOperatorDesc ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['AnimationList']]) + '>'


class TBoneProceduralAnimation:
    def __init__(self, LimitValue=None, Axis=None, BoneName=None, Delay=None, Duration=None, IsTranslation=None):
        self.LimitValue = LimitValue
        self.Axis = Axis
        self.BoneName = BoneName
        self.Delay = Delay
        self.Duration = Duration
        self.IsTranslation = IsTranslation

    def __repr__(self):
        return f'<TBoneProceduralAnimation ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['LimitValue', 'Axis', 'BoneName', 'Delay', 'Duration', 'IsTranslation']]) + '>'


class TAirplaneDeviatorDesc:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TAirplaneDeviatorDesc>'


class TCosmeticSelectionStyleOperatorDesc:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TCosmeticSelectionStyleOperatorDesc>'


class TCosmeticSpottedStyleOperatorDesc:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TCosmeticSpottedStyleOperatorDesc>'


class TCosmeticGhostColorOperatorDesc:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TCosmeticGhostColorOperatorDesc>'


class TCosmeticPawnGhostColorOperatorDesc:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TCosmeticPawnGhostColorOperatorDesc>'


class TCosmeticTacticGhostColorOperatorDesc:
    def __init__(self, Color=None, Alphas=None, Blends=None):
        self.Color = Color
        self.Alphas = Alphas
        self.Blends = Blends

    def __repr__(self):
        return f'<TCosmeticTacticGhostColorOperatorDesc ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Color', 'Alphas', 'Blends']]) + '>'


class TCosmeticTeamColorOperatorDesc:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TCosmeticTeamColorOperatorDesc>'


class TCosmeticExplodedStyleOperatorDesc:
    def __init__(self, ExplodedDamageTextures=None):
        self.ExplodedDamageTextures = ExplodedDamageTextures

    def __repr__(self):
        return f'<TCosmeticExplodedStyleOperatorDesc ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ExplodedDamageTextures']]) + '>'


class TCosmeticSetToPoseOperatorDesc:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TCosmeticSetToPoseOperatorDesc>'


class TCosmeticAirplanePartsOperatorDesc:
    def __init__(self, OperatorId=None):
        self.OperatorId = OperatorId

    def __repr__(self):
        return f'<TCosmeticAirplanePartsOperatorDesc ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['OperatorId']]) + '>'


class TCosmeticMovementAirplaneOperatorDesc:
    def __init__(self, OperatorId=None):
        self.OperatorId = OperatorId

    def __repr__(self):
        return f'<TCosmeticMovementAirplaneOperatorDesc ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['OperatorId']]) + '>'


class TCosmeticAirplaneShadowOperatorDesc:
    def __init__(self, OperatorId=None):
        self.OperatorId = OperatorId

    def __repr__(self):
        return f'<TCosmeticAirplaneShadowOperatorDesc ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['OperatorId']]) + '>'


class TDepictionPylonSelector:
    def __init__(self, HighLimitInMeter=None, Camera=None):
        self.HighLimitInMeter = HighLimitInMeter
        self.Camera = Camera

    def __repr__(self):
        return f'<TDepictionPylonSelector ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['HighLimitInMeter', 'Camera']]) + '>'


class TGfxDescriptorChassis:
    def __init__(self, SpringY=None, SpringDamperMaxY=None, SpringX=None, SousMobileName=None, NoiseGridHeight=None, NoiseGridSize=None, SpringDamperMaxX=None, SpringDamperMultiplier=None, DamperY=None, Force=None, DamperX=None):
        self.SpringY = SpringY
        self.SpringDamperMaxY = SpringDamperMaxY
        self.SpringX = SpringX
        self.SousMobileName = SousMobileName
        self.NoiseGridHeight = NoiseGridHeight
        self.NoiseGridSize = NoiseGridSize
        self.SpringDamperMaxX = SpringDamperMaxX
        self.SpringDamperMultiplier = SpringDamperMultiplier
        self.DamperY = DamperY
        self.Force = Force
        self.DamperX = DamperX

    def __repr__(self):
        return f'<TGfxDescriptorChassis ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['SpringY', 'SpringDamperMaxY', 'SpringX', 'SousMobileName', 'NoiseGridHeight', 'NoiseGridSize', 'SpringDamperMaxX', 'SpringDamperMultiplier', 'DamperY', 'Force', 'DamperX']]) + '>'


class TStrategicEntityConstantes:
    def __init__(self, IAObjective=None, IAGroup=None):
        self.IAObjective = IAObjective
        self.IAGroup = IAGroup

    def __repr__(self):
        return f'<TStrategicEntityConstantes ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['IAObjective', 'IAGroup']]) + '>'


class TIAGroupPawnsModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TIAGroupPawnsModuleDescriptor>'


class TIALinkToObjectivesModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TIALinkToObjectivesModuleDescriptor>'


class TIATargetObjectiveModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TIATargetObjectiveModuleDescriptor>'


class TIAGroupPoolModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TIAGroupPoolModuleDescriptor>'


class TIAGroupTargetModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TIAGroupTargetModuleDescriptor>'


class TIAObjectiveZoneModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TIAObjectiveZoneModuleDescriptor>'


class TIAObjectiveStrategyStateModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TIAObjectiveStrategyStateModuleDescriptor>'


class TIAGeneralStrategy:
    def __init__(self, AllowToByPassNbMacroActionAllowedToProduceSimultaneous=None, StrategyName=None, FirstGenerator=None, TransitionList=None, DoNotCancelProduction=None, AuthorizedCorridorList=None):
        self.AllowToByPassNbMacroActionAllowedToProduceSimultaneous = AllowToByPassNbMacroActionAllowedToProduceSimultaneous
        self.StrategyName = StrategyName
        self.FirstGenerator = FirstGenerator
        self.TransitionList = TransitionList
        self.DoNotCancelProduction = DoNotCancelProduction
        self.AuthorizedCorridorList = AuthorizedCorridorList

    def __repr__(self):
        return f'<TIAGeneralStrategy ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['AllowToByPassNbMacroActionAllowedToProduceSimultaneous', 'StrategyName', 'FirstGenerator', 'TransitionList', 'DoNotCancelProduction', 'AuthorizedCorridorList']]) + '>'


class TSequenceGeneratorDescriptor:
    def __init__(self, NbMacroActionAllowedToProduceSimultaneous=None, ScalingGeneratorList=None, GeneratorList=None):
        self.NbMacroActionAllowedToProduceSimultaneous = NbMacroActionAllowedToProduceSimultaneous
        self.ScalingGeneratorList = ScalingGeneratorList
        self.GeneratorList = GeneratorList

    def __repr__(self):
        return f'<TSequenceGeneratorDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['NbMacroActionAllowedToProduceSimultaneous', 'ScalingGeneratorList', 'GeneratorList']]) + '>'


class TIASkirmishList_Specific:
    def __init__(self, IAStrategyForAutoDeploy=None, IAStrategyListForSoloCampaign=None, IAStrategyConfiguration=None, IAStrategyOverrideByMap=None, IAStrategyOverrideForTicketsEconomy=None):
        self.IAStrategyForAutoDeploy = IAStrategyForAutoDeploy
        self.IAStrategyListForSoloCampaign = IAStrategyListForSoloCampaign
        self.IAStrategyConfiguration = IAStrategyConfiguration
        self.IAStrategyOverrideByMap = IAStrategyOverrideByMap
        self.IAStrategyOverrideForTicketsEconomy = IAStrategyOverrideForTicketsEconomy

    def __repr__(self):
        return f'<TIASkirmishList_Specific ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['IAStrategyForAutoDeploy', 'IAStrategyListForSoloCampaign', 'IAStrategyConfiguration', 'IAStrategyOverrideByMap', 'IAStrategyOverrideForTicketsEconomy']]) + '>'


class TMacroActionDescriptor_Attack_Specific:
    def __init__(self, ParametresDeMission=None):
        self.ParametresDeMission = ParametresDeMission

    def __repr__(self):
        return f'<TMacroActionDescriptor_Attack_Specific ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ParametresDeMission']]) + '>'


class TGenerationSettingHolder:
    def __init__(self, GenerationType=None, NumberLaunchBasedOnGenerationType=None):
        self.GenerationType = GenerationType
        self.NumberLaunchBasedOnGenerationType = NumberLaunchBasedOnGenerationType

    def __repr__(self):
        return f'<TGenerationSettingHolder ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['GenerationType', 'NumberLaunchBasedOnGenerationType']]) + '>'


class TAirStrikeSettingHolder:
    def __init__(self, TypesDeRequetesAcceptees=None, Setting=None):
        self.TypesDeRequetesAcceptees = TypesDeRequetesAcceptees
        self.Setting = Setting

    def __repr__(self):
        return f'<TAirStrikeSettingHolder ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TypesDeRequetesAcceptees', 'Setting']]) + '>'


class TSupportSettingHolder:
    def __init__(self, SettingList=None):
        self.SettingList = SettingList

    def __repr__(self):
        return f'<TSupportSettingHolder ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['SettingList']]) + '>'


class TArtilleryAmountSettingHolder:
    def __init__(self, ArtilleryAmount=None):
        self.ArtilleryAmount = ArtilleryAmount

    def __repr__(self):
        return f'<TArtilleryAmountSettingHolder ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ArtilleryAmount']]) + '>'


class TBlitzkriegSettingHolder:
    def __init__(self, RatioFactorToDisableSelfPreservation=None, MinimumCostForSelfPreservation=None):
        self.RatioFactorToDisableSelfPreservation = RatioFactorToDisableSelfPreservation
        self.MinimumCostForSelfPreservation = MinimumCostForSelfPreservation

    def __repr__(self):
        return f'<TBlitzkriegSettingHolder ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['RatioFactorToDisableSelfPreservation', 'MinimumCostForSelfPreservation']]) + '>'


class TAttackRatioSettingHolder:
    def __init__(self, RatioMinimumPourAttaquer=None):
        self.RatioMinimumPourAttaquer = RatioMinimumPourAttaquer

    def __repr__(self):
        return f'<TAttackRatioSettingHolder ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['RatioMinimumPourAttaquer']]) + '>'


class TMacroActionProductionSettingHolder:
    def __init__(self, DisableReinforcement=None, DistanceToOptimumStartDuringDeploymentGRU=None, PoolModelList=None, OnlyAllowToSelectUnits=None, ProdProperties=None):
        self.DisableReinforcement = DisableReinforcement
        self.DistanceToOptimumStartDuringDeploymentGRU = DistanceToOptimumStartDuringDeploymentGRU
        self.PoolModelList = PoolModelList
        self.OnlyAllowToSelectUnits = OnlyAllowToSelectUnits
        self.ProdProperties = ProdProperties

    def __repr__(self):
        return f'<TMacroActionProductionSettingHolder ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['DisableReinforcement', 'DistanceToOptimumStartDuringDeploymentGRU', 'PoolModelList', 'OnlyAllowToSelectUnits', 'ProdProperties']]) + '>'


class TMacroActionLifetimeSettingHolder:
    def __init__(self, MaintainForever=None):
        self.MaintainForever = MaintainForever

    def __repr__(self):
        return f'<TMacroActionLifetimeSettingHolder ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MaintainForever']]) + '>'


class TDisableUnitToReleaseSettingHolder:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TDisableUnitToReleaseSettingHolder>'


class TMacroActionDescriptor_Defense_Specific:
    def __init__(self, ParametresDeMission=None):
        self.ParametresDeMission = ParametresDeMission

    def __repr__(self):
        return f'<TMacroActionDescriptor_Defense_Specific ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ParametresDeMission']]) + '>'


class TMacroActionDescriptor_Artillery_PlayerMission:
    def __init__(self, ParametresDeMission=None):
        self.ParametresDeMission = ParametresDeMission

    def __repr__(self):
        return f'<TMacroActionDescriptor_Artillery_PlayerMission ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ParametresDeMission']]) + '>'


class TArtilleryPositionningSettingHolder:
    def __init__(self, ArtilleryPositionOffsetGRU=None):
        self.ArtilleryPositionOffsetGRU = ArtilleryPositionOffsetGRU

    def __repr__(self):
        return f'<TArtilleryPositionningSettingHolder ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ArtilleryPositionOffsetGRU']]) + '>'


class TArtilleryPlayerMissionSettingHolder:
    def __init__(self, TargetFilter=None, MinDurationForTargetValidity=None, MaxDurationForTargetValidity=None, AuthorizedTargetTags=None):
        self.TargetFilter = TargetFilter
        self.MinDurationForTargetValidity = MinDurationForTargetValidity
        self.MaxDurationForTargetValidity = MaxDurationForTargetValidity
        self.AuthorizedTargetTags = AuthorizedTargetTags

    def __repr__(self):
        return f'<TArtilleryPlayerMissionSettingHolder ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TargetFilter', 'MinDurationForTargetValidity', 'MaxDurationForTargetValidity', 'AuthorizedTargetTags']]) + '>'


class TArtilleryStrikeSettingHolder:
    def __init__(self, SupportStrikeRatio=None, DelaytBetweenTargetDeathAndNewStrike=None):
        self.SupportStrikeRatio = SupportStrikeRatio
        self.DelaytBetweenTargetDeathAndNewStrike = DelaytBetweenTargetDeathAndNewStrike

    def __repr__(self):
        return f'<TArtilleryStrikeSettingHolder ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['SupportStrikeRatio', 'DelaytBetweenTargetDeathAndNewStrike']]) + '>'


class TMacroActionDescriptor_AirStrike_Specific:
    def __init__(self, ParametresDeMission=None):
        self.ParametresDeMission = ParametresDeMission

    def __repr__(self):
        return f'<TMacroActionDescriptor_AirStrike_Specific ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ParametresDeMission']]) + '>'


class TAirStrikeAcceptableThreatSettingHolder:
    def __init__(self, PercentAcceptableDangerousIndicesForAirplaneValidTarget=None):
        self.PercentAcceptableDangerousIndicesForAirplaneValidTarget = PercentAcceptableDangerousIndicesForAirplaneValidTarget

    def __repr__(self):
        return f'<TAirStrikeAcceptableThreatSettingHolder ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['PercentAcceptableDangerousIndicesForAirplaneValidTarget']]) + '>'


class TMacroActionDescriptor_AirReco_Specific:
    def __init__(self, ParametresDeMission=None):
        self.ParametresDeMission = ParametresDeMission

    def __repr__(self):
        return f'<TMacroActionDescriptor_AirReco_Specific ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ParametresDeMission']]) + '>'


class AirRecoMissionLaunchSettingHolderTemplate:
    def __init__(self, MaxAirplaneCountOnBattlefield=None, TicksBetweenTwoLaunch=None, TicksBetweenTwoMissions=None):
        self.MaxAirplaneCountOnBattlefield = MaxAirplaneCountOnBattlefield
        self.TicksBetweenTwoLaunch = TicksBetweenTwoLaunch
        self.TicksBetweenTwoMissions = TicksBetweenTwoMissions

    def __repr__(self):
        return f'<AirRecoMissionLaunchSettingHolderTemplate ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MaxAirplaneCountOnBattlefield', 'TicksBetweenTwoLaunch', 'TicksBetweenTwoMissions']]) + '>'


class TMacroActionDescriptor_Supply_Specific:
    def __init__(self, ParametresDeMission=None):
        self.ParametresDeMission = ParametresDeMission

    def __repr__(self):
        return f'<TMacroActionDescriptor_Supply_Specific ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ParametresDeMission']]) + '>'


class TSupplySettingHolder:
    def __init__(self, SupplyableMinimumRatio=None):
        self.SupplyableMinimumRatio = SupplyableMinimumRatio

    def __repr__(self):
        return f'<TSupplySettingHolder ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['SupplyableMinimumRatio']]) + '>'


class TPlayerMissionDescriptor:
    def __init__(self, UsePosition=None, ExclusionTags=None, MacroActionDescriptor=None, Mergeable=None, AuthorizedTags=None):
        self.UsePosition = UsePosition
        self.ExclusionTags = ExclusionTags
        self.MacroActionDescriptor = MacroActionDescriptor
        self.Mergeable = Mergeable
        self.AuthorizedTags = AuthorizedTags

    def __repr__(self):
        return f'<TPlayerMissionDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['UsePosition', 'ExclusionTags', 'MacroActionDescriptor', 'Mergeable', 'AuthorizedTags']]) + '>'


class TPlayerMissionConstantesDescriptor:
    def __init__(self, PlayerMissionDescriptorByType=None, MaxCustomZoneDistanceForSimilarGRU=None):
        self.PlayerMissionDescriptorByType = PlayerMissionDescriptorByType
        self.MaxCustomZoneDistanceForSimilarGRU = MaxCustomZoneDistanceForSimilarGRU

    def __repr__(self):
        return f'<TPlayerMissionConstantesDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['PlayerMissionDescriptorByType', 'MaxCustomZoneDistanceForSimilarGRU']]) + '>'


class TPlayerMissionOrderDescriptor:
    def __init__(self, DescriptorPriority=None, DebugName=None, UseMousePolicy=None):
        self.DescriptorPriority = DescriptorPriority
        self.DebugName = DebugName
        self.UseMousePolicy = UseMousePolicy

    def __repr__(self):
        return f'<TPlayerMissionOrderDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['DescriptorPriority', 'DebugName', 'UseMousePolicy']]) + '>'


class TUIPlayerMissionConstantesDescriptor:
    def __init__(self, PlayerMissionFeedbackDescriptorByType=None, StartFadeAlphaAfterTimeInSeconds=None, AlphaFadeDurationInSeconds=None):
        self.PlayerMissionFeedbackDescriptorByType = PlayerMissionFeedbackDescriptorByType
        self.StartFadeAlphaAfterTimeInSeconds = StartFadeAlphaAfterTimeInSeconds
        self.AlphaFadeDurationInSeconds = AlphaFadeDurationInSeconds

    def __repr__(self):
        return f'<TUIPlayerMissionConstantesDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['PlayerMissionFeedbackDescriptorByType', 'StartFadeAlphaAfterTimeInSeconds', 'AlphaFadeDurationInSeconds']]) + '>'


class TFeedbackStyleDescriptor:
    def __init__(self, Thickness=None, Color=None):
        self.Thickness = Thickness
        self.Color = Color

    def __repr__(self):
        return f'<TFeedbackStyleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Thickness', 'Color']]) + '>'


class TMacroActionDescriptor_CorridorDefense_Specific:
    def __init__(self, ParametresDeMission=None):
        self.ParametresDeMission = ParametresDeMission

    def __repr__(self):
        return f'<TMacroActionDescriptor_CorridorDefense_Specific ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ParametresDeMission']]) + '>'


class TMacroActionDescriptor_CorridorDynamicDefense_Specific:
    def __init__(self, ParametresDeMission=None):
        self.ParametresDeMission = ParametresDeMission

    def __repr__(self):
        return f'<TMacroActionDescriptor_CorridorDynamicDefense_Specific ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ParametresDeMission']]) + '>'


class TMacroActionDescriptor_Support_Specific:
    def __init__(self, ParametresDeMission=None):
        self.ParametresDeMission = ParametresDeMission

    def __repr__(self):
        return f'<TMacroActionDescriptor_Support_Specific ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ParametresDeMission']]) + '>'


class TCounterTagSettingHolder:
    def __init__(self, TagDeContre=None):
        self.TagDeContre = TagDeContre

    def __repr__(self):
        return f'<TCounterTagSettingHolder ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TagDeContre']]) + '>'


class TPoolModel:
    def __init__(self, ModelList=None):
        self.ModelList = ModelList

    def __repr__(self):
        return f'<TPoolModel ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ModelList']]) + '>'


class TPoolElement:
    def __init__(self, IndexPriorityOverPrice=None, Nb=None, DescriptorId=None, PriceComparisonMethod=None, Required=None, TagsPriority=None):
        self.IndexPriorityOverPrice = IndexPriorityOverPrice
        self.Nb = Nb
        self.DescriptorId = DescriptorId
        self.PriceComparisonMethod = PriceComparisonMethod
        self.Required = Required
        self.TagsPriority = TagsPriority

    def __repr__(self):
        return f'<TPoolElement ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['IndexPriorityOverPrice', 'Nb', 'DescriptorId', 'PriceComparisonMethod', 'Required', 'TagsPriority']]) + '>'


class TSupportSetting:
    def __init__(self, TagDeContre=None, TagAContrer=None, Ratio=None):
        self.TagDeContre = TagDeContre
        self.TagAContrer = TagAContrer
        self.Ratio = Ratio

    def __repr__(self):
        return f'<TSupportSetting ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TagDeContre', 'TagAContrer', 'Ratio']]) + '>'


class Template_Capture_Command_Zone:
    def __init__(self, PoolModelList=None, GenerationType=None, AlsoConsiderTheseDescriptorsForMaintain=None, NumberLaunchBasedOnGenerationType=None):
        self.PoolModelList = PoolModelList
        self.GenerationType = GenerationType
        self.AlsoConsiderTheseDescriptorsForMaintain = AlsoConsiderTheseDescriptorsForMaintain
        self.NumberLaunchBasedOnGenerationType = NumberLaunchBasedOnGenerationType

    def __repr__(self):
        return f'<Template_Capture_Command_Zone ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['PoolModelList', 'GenerationType', 'AlsoConsiderTheseDescriptorsForMaintain', 'NumberLaunchBasedOnGenerationType']]) + '>'


class TSequenceCondition_And:
    def __init__(self, Condition2=None, Condition1=None):
        self.Condition2 = Condition2
        self.Condition1 = Condition1

    def __repr__(self):
        return f'<TSequenceCondition_And ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Condition2', 'Condition1']]) + '>'


class TIAGeneralStrategyTransition:
    def __init__(self, Origine=None, Condition=None, Destination=None):
        self.Origine = Origine
        self.Condition = Condition
        self.Destination = Destination

    def __repr__(self):
        return f'<TIAGeneralStrategyTransition ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Origine', 'Condition', 'Destination']]) + '>'


class TSequenceCondition_AutoDeployFlagValue:
    def __init__(self, Value=None):
        self.Value = Value

    def __repr__(self):
        return f'<TSequenceCondition_AutoDeployFlagValue ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Value']]) + '>'


class TSequenceCondition_Not:
    def __init__(self, Condition=None):
        self.Condition = Condition

    def __repr__(self):
        return f'<TSequenceCondition_Not ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Condition']]) + '>'


class TSequenceCondition_Phase:
    def __init__(self, PhaseType=None):
        self.PhaseType = PhaseType

    def __repr__(self):
        return f'<TSequenceCondition_Phase ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['PhaseType']]) + '>'


class TSequenceCondition_True:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TSequenceCondition_True>'


class Template_SequenceConditionOpponentHasScoreHigher:
    def __init__(self, RatioValue=None, ScorePointType=None):
        self.RatioValue = RatioValue
        self.ScorePointType = ScorePointType

    def __repr__(self):
        return f'<Template_SequenceConditionOpponentHasScoreHigher ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['RatioValue', 'ScorePointType']]) + '>'


class TSequenceCondition_IsAttackingAlliance:
    def __init__(self, IsAttackingAlliance=None):
        self.IsAttackingAlliance = IsAttackingAlliance

    def __repr__(self):
        return f'<TSequenceCondition_IsAttackingAlliance ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['IsAttackingAlliance']]) + '>'


class Template_CubeActionOrderButtonInformationsDescriptor_WithSound:
    def __init__(self, LeftClickSound=None, SpotlightUniqueName=None, Mapping=None, CubeActionFunctionType=None, HintExtendedToken=None, ValidationTargetToken=None, ButtonTextToken=None, HintTitleToken=None, DebugName=None, CubeActionName=None, OrderToken=None, HintBodyToken=None, HintDico=None, ActionType=None):
        self.LeftClickSound = LeftClickSound
        self.SpotlightUniqueName = SpotlightUniqueName
        self.Mapping = Mapping
        self.CubeActionFunctionType = CubeActionFunctionType
        self.HintExtendedToken = HintExtendedToken
        self.ValidationTargetToken = ValidationTargetToken
        self.ButtonTextToken = ButtonTextToken
        self.HintTitleToken = HintTitleToken
        self.DebugName = DebugName
        self.CubeActionName = CubeActionName
        self.OrderToken = OrderToken
        self.HintBodyToken = HintBodyToken
        self.HintDico = HintDico
        self.ActionType = ActionType

    def __repr__(self):
        return f'<Template_CubeActionOrderButtonInformationsDescriptor_WithSound ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['LeftClickSound', 'SpotlightUniqueName', 'Mapping', 'CubeActionFunctionType', 'HintExtendedToken', 'ValidationTargetToken', 'ButtonTextToken', 'HintTitleToken', 'DebugName', 'CubeActionName', 'OrderToken', 'HintBodyToken', 'HintDico', 'ActionType']]) + '>'


class InterfaceSound:
    def __init__(self, FileName=None):
        self.FileName = FileName

    def __repr__(self):
        return f'<InterfaceSound ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['FileName']]) + '>'


class TIngameGamePadUserInputForTrailer:
    def __init__(self, UsePad=None, InputLayer=None, InGameManagerHandler=None, Scene=None, ScreenShotDirectoryName=None, ScreenShotBaseName=None, ActivePauseGameSpeed=None, PauseLock=None):
        self.UsePad = UsePad
        self.InputLayer = InputLayer
        self.InGameManagerHandler = InGameManagerHandler
        self.Scene = Scene
        self.ScreenShotDirectoryName = ScreenShotDirectoryName
        self.ScreenShotBaseName = ScreenShotBaseName
        self.ActivePauseGameSpeed = ActivePauseGameSpeed
        self.PauseLock = PauseLock

    def __repr__(self):
        return f'<TIngameGamePadUserInputForTrailer ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['UsePad', 'InputLayer', 'InGameManagerHandler', 'Scene', 'ScreenShotDirectoryName', 'ScreenShotBaseName', 'ActivePauseGameSpeed', 'PauseLock']]) + '>'


class TGDActionCallbackManager:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TGDActionCallbackManager>'


class TOrderEvaluatorCollectionListDescriptor:
    def __init__(self, CollectionByName=None):
        self.CollectionByName = CollectionByName

    def __repr__(self):
        return f'<TOrderEvaluatorCollectionListDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['CollectionByName']]) + '>'


class TOrderEvaluatorCollectionDescriptor:
    def __init__(self, GameplayLogicManagerHandler=None, OrderEvaluatorList=None):
        self.GameplayLogicManagerHandler = GameplayLogicManagerHandler
        self.OrderEvaluatorList = OrderEvaluatorList

    def __repr__(self):
        return f'<TOrderEvaluatorCollectionDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['GameplayLogicManagerHandler', 'OrderEvaluatorList']]) + '>'


class TOrderEvaluatorAny:
    def __init__(self, MouseWidgetSelector=None, FXFeedback=None, IgnoreDirectOrder=None, OrderToken=None, PlayFXFeedbackWithoutTargets=None, IsTargetAuthorized=None, IgnoreDefaultOrder=None):
        self.MouseWidgetSelector = MouseWidgetSelector
        self.FXFeedback = FXFeedback
        self.IgnoreDirectOrder = IgnoreDirectOrder
        self.OrderToken = OrderToken
        self.PlayFXFeedbackWithoutTargets = PlayFXFeedbackWithoutTargets
        self.IsTargetAuthorized = IsTargetAuthorized
        self.IgnoreDefaultOrder = IgnoreDefaultOrder

    def __repr__(self):
        return f'<TOrderEvaluatorAny ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MouseWidgetSelector', 'FXFeedback', 'IgnoreDirectOrder', 'OrderToken', 'PlayFXFeedbackWithoutTargets', 'IsTargetAuthorized', 'IgnoreDefaultOrder']]) + '>'


class TOrderEvaluatorFortifyAntiAir:
    def __init__(self, OrderToken=None, IgnoreDefaultOrder=None):
        self.OrderToken = OrderToken
        self.IgnoreDefaultOrder = IgnoreDefaultOrder

    def __repr__(self):
        return f'<TOrderEvaluatorFortifyAntiAir ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['OrderToken', 'IgnoreDefaultOrder']]) + '>'


class TOrderEvaluatorStrategicMove:
    def __init__(self, OrderToken=None, IgnoreDefaultOrder=None, FXFeedback=None, MouseWidgetSelector=None, PlayFXFeedbackWithoutTargets=None):
        self.OrderToken = OrderToken
        self.IgnoreDefaultOrder = IgnoreDefaultOrder
        self.FXFeedback = FXFeedback
        self.MouseWidgetSelector = MouseWidgetSelector
        self.PlayFXFeedbackWithoutTargets = PlayFXFeedbackWithoutTargets

    def __repr__(self):
        return f'<TOrderEvaluatorStrategicMove ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['OrderToken', 'IgnoreDefaultOrder', 'FXFeedback', 'MouseWidgetSelector', 'PlayFXFeedbackWithoutTargets']]) + '>'


class TOrderEvaluatorShootDefensiveSmoke:
    def __init__(self, OrderToken=None, IgnoreDefaultOrder=None, IgnoreDirectOrder=None):
        self.OrderToken = OrderToken
        self.IgnoreDefaultOrder = IgnoreDefaultOrder
        self.IgnoreDirectOrder = IgnoreDirectOrder

    def __repr__(self):
        return f'<TOrderEvaluatorShootDefensiveSmoke ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['OrderToken', 'IgnoreDefaultOrder', 'IgnoreDirectOrder']]) + '>'


class TOrderEvaluatorStop:
    def __init__(self, OrderToken=None, IgnoreDefaultOrder=None, IgnoreDirectOrder=None):
        self.OrderToken = OrderToken
        self.IgnoreDefaultOrder = IgnoreDefaultOrder
        self.IgnoreDirectOrder = IgnoreDirectOrder

    def __repr__(self):
        return f'<TOrderEvaluatorStop ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['OrderToken', 'IgnoreDefaultOrder', 'IgnoreDirectOrder']]) + '>'


class TOrderEvaluatorChangeAltitude:
    def __init__(self, OrderToken=None, IgnoreDefaultOrder=None, IgnoreDirectOrder=None):
        self.OrderToken = OrderToken
        self.IgnoreDefaultOrder = IgnoreDefaultOrder
        self.IgnoreDirectOrder = IgnoreDirectOrder

    def __repr__(self):
        return f'<TOrderEvaluatorChangeAltitude ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['OrderToken', 'IgnoreDefaultOrder', 'IgnoreDirectOrder']]) + '>'


class TOrderEvaluatorSpread:
    def __init__(self, OrderToken=None, IgnoreDefaultOrder=None, IgnoreDirectOrder=None):
        self.OrderToken = OrderToken
        self.IgnoreDefaultOrder = IgnoreDefaultOrder
        self.IgnoreDirectOrder = IgnoreDirectOrder

    def __repr__(self):
        return f'<TOrderEvaluatorSpread ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['OrderToken', 'IgnoreDefaultOrder', 'IgnoreDirectOrder']]) + '>'


class TOrderEvaluatorLoadIntoTransport:
    def __init__(self, OrderToken=None, IgnoreDefaultOrder=None, FXFeedback=None, MouseWidgetSelector=None):
        self.OrderToken = OrderToken
        self.IgnoreDefaultOrder = IgnoreDefaultOrder
        self.FXFeedback = FXFeedback
        self.MouseWidgetSelector = MouseWidgetSelector

    def __repr__(self):
        return f'<TOrderEvaluatorLoadIntoTransport ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['OrderToken', 'IgnoreDefaultOrder', 'FXFeedback', 'MouseWidgetSelector']]) + '>'


class TOrderEvaluatorLoadUnit:
    def __init__(self, OrderToken=None, IgnoreDefaultOrder=None, FXFeedback=None, MouseWidgetSelector=None):
        self.OrderToken = OrderToken
        self.IgnoreDefaultOrder = IgnoreDefaultOrder
        self.FXFeedback = FXFeedback
        self.MouseWidgetSelector = MouseWidgetSelector

    def __repr__(self):
        return f'<TOrderEvaluatorLoadUnit ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['OrderToken', 'IgnoreDefaultOrder', 'FXFeedback', 'MouseWidgetSelector']]) + '>'


class TOrderEvaluatorAssaultDistrict:
    def __init__(self, OrderToken=None, IgnoreDefaultOrder=None, IgnoreDirectOrder=None, FXFeedback=None, MouseWidgetSelector=None, OrderInterpretationForOrderDisplayAndAcknows=None):
        self.OrderToken = OrderToken
        self.IgnoreDefaultOrder = IgnoreDefaultOrder
        self.IgnoreDirectOrder = IgnoreDirectOrder
        self.FXFeedback = FXFeedback
        self.MouseWidgetSelector = MouseWidgetSelector
        self.OrderInterpretationForOrderDisplayAndAcknows = OrderInterpretationForOrderDisplayAndAcknows

    def __repr__(self):
        return f'<TOrderEvaluatorAssaultDistrict ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['OrderToken', 'IgnoreDefaultOrder', 'IgnoreDirectOrder', 'FXFeedback', 'MouseWidgetSelector', 'OrderInterpretationForOrderDisplayAndAcknows']]) + '>'


class TOrderEvaluatorEnterDistrict:
    def __init__(self, OrderToken=None, IgnoreDefaultOrder=None, FXFeedback=None, MouseWidgetSelector=None):
        self.OrderToken = OrderToken
        self.IgnoreDefaultOrder = IgnoreDefaultOrder
        self.FXFeedback = FXFeedback
        self.MouseWidgetSelector = MouseWidgetSelector

    def __repr__(self):
        return f'<TOrderEvaluatorEnterDistrict ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['OrderToken', 'IgnoreDefaultOrder', 'FXFeedback', 'MouseWidgetSelector']]) + '>'


class TOrderEvaluatorAttack:
    def __init__(self, MouseWidgetSelector=None, FXFeedback=None, OrderToken=None, PlayFXFeedbackWithoutTargets=None, IgnoreDefaultOrder=None):
        self.MouseWidgetSelector = MouseWidgetSelector
        self.FXFeedback = FXFeedback
        self.OrderToken = OrderToken
        self.PlayFXFeedbackWithoutTargets = PlayFXFeedbackWithoutTargets
        self.IgnoreDefaultOrder = IgnoreDefaultOrder

    def __repr__(self):
        return f'<TOrderEvaluatorAttack ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MouseWidgetSelector', 'FXFeedback', 'OrderToken', 'PlayFXFeedbackWithoutTargets', 'IgnoreDefaultOrder']]) + '>'


class TOrderEvaluatorMoveAndAttack:
    def __init__(self, ClampDestinationOnNavMesh=None, MouseWidgetSelector=None, FXFeedback=None, IgnoreDirectOrder=None, OrderInterpretationForOrderDisplayAndAcknows=None, OrderToken=None, PlayFXFeedbackWithoutTargets=None, IgnoreDefaultOrder=None):
        self.ClampDestinationOnNavMesh = ClampDestinationOnNavMesh
        self.MouseWidgetSelector = MouseWidgetSelector
        self.FXFeedback = FXFeedback
        self.IgnoreDirectOrder = IgnoreDirectOrder
        self.OrderInterpretationForOrderDisplayAndAcknows = OrderInterpretationForOrderDisplayAndAcknows
        self.OrderToken = OrderToken
        self.PlayFXFeedbackWithoutTargets = PlayFXFeedbackWithoutTargets
        self.IgnoreDefaultOrder = IgnoreDefaultOrder

    def __repr__(self):
        return f'<TOrderEvaluatorMoveAndAttack ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ClampDestinationOnNavMesh', 'MouseWidgetSelector', 'FXFeedback', 'IgnoreDirectOrder', 'OrderInterpretationForOrderDisplayAndAcknows', 'OrderToken', 'PlayFXFeedbackWithoutTargets', 'IgnoreDefaultOrder']]) + '>'


class TOrderEvaluatorShootOnPosition:
    def __init__(self, MouseWidgetSelector=None, FXFeedback=None, OrderInterpretationForOrderDisplayAndAcknows=None, OrderToken=None, PlayFXFeedbackWithoutTargets=None, IgnoreDefaultOrder=None):
        self.MouseWidgetSelector = MouseWidgetSelector
        self.FXFeedback = FXFeedback
        self.OrderInterpretationForOrderDisplayAndAcknows = OrderInterpretationForOrderDisplayAndAcknows
        self.OrderToken = OrderToken
        self.PlayFXFeedbackWithoutTargets = PlayFXFeedbackWithoutTargets
        self.IgnoreDefaultOrder = IgnoreDefaultOrder

    def __repr__(self):
        return f'<TOrderEvaluatorShootOnPosition ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MouseWidgetSelector', 'FXFeedback', 'OrderInterpretationForOrderDisplayAndAcknows', 'OrderToken', 'PlayFXFeedbackWithoutTargets', 'IgnoreDefaultOrder']]) + '>'


class TOrderEvaluatorUnloadAtPosition:
    def __init__(self, OrderToken=None, IgnoreDefaultOrder=None, FXFeedback=None, MouseWidgetSelector=None, PlayFXFeedbackWithoutTargets=None, ClampDestinationOnNavMesh=None):
        self.OrderToken = OrderToken
        self.IgnoreDefaultOrder = IgnoreDefaultOrder
        self.FXFeedback = FXFeedback
        self.MouseWidgetSelector = MouseWidgetSelector
        self.PlayFXFeedbackWithoutTargets = PlayFXFeedbackWithoutTargets
        self.ClampDestinationOnNavMesh = ClampDestinationOnNavMesh

    def __repr__(self):
        return f'<TOrderEvaluatorUnloadAtPosition ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['OrderToken', 'IgnoreDefaultOrder', 'FXFeedback', 'MouseWidgetSelector', 'PlayFXFeedbackWithoutTargets', 'ClampDestinationOnNavMesh']]) + '>'


class TOrderEvaluatorMove:
    def __init__(self, ClampDestinationOnNavMesh=None, MouseWidgetSelector=None, FXFeedback=None, OrderInterpretationForOrderDisplayAndAcknows=None, OrderToken=None, PlayFXFeedbackWithoutTargets=None, IgnoreDefaultOrder=None):
        self.ClampDestinationOnNavMesh = ClampDestinationOnNavMesh
        self.MouseWidgetSelector = MouseWidgetSelector
        self.FXFeedback = FXFeedback
        self.OrderInterpretationForOrderDisplayAndAcknows = OrderInterpretationForOrderDisplayAndAcknows
        self.OrderToken = OrderToken
        self.PlayFXFeedbackWithoutTargets = PlayFXFeedbackWithoutTargets
        self.IgnoreDefaultOrder = IgnoreDefaultOrder

    def __repr__(self):
        return f'<TOrderEvaluatorMove ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ClampDestinationOnNavMesh', 'MouseWidgetSelector', 'FXFeedback', 'OrderInterpretationForOrderDisplayAndAcknows', 'OrderToken', 'PlayFXFeedbackWithoutTargets', 'IgnoreDefaultOrder']]) + '>'


class TOrderEvaluatorUseAnyCapacite:
    def __init__(self, OrderToken=None, IgnoreDefaultOrder=None, MouseWidgetSelector=None):
        self.OrderToken = OrderToken
        self.IgnoreDefaultOrder = IgnoreDefaultOrder
        self.MouseWidgetSelector = MouseWidgetSelector

    def __repr__(self):
        return f'<TOrderEvaluatorUseAnyCapacite ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['OrderToken', 'IgnoreDefaultOrder', 'MouseWidgetSelector']]) + '>'


class TReplayHUDManager:
    def __init__(self, InGameManagerHandler=None):
        self.InGameManagerHandler = InGameManagerHandler

    def __repr__(self):
        return f'<TReplayHUDManager ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['InGameManagerHandler']]) + '>'


class TModernWarfareUnitNamesDico:
    def __init__(self, NationToDicoToken=None):
        self.NationToDicoToken = NationToDicoToken

    def __repr__(self):
        return f'<TModernWarfareUnitNamesDico ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['NationToDicoToken']]) + '>'


class TUIResourceTexture_Common:
    def __init__(self, FileName=None):
        self.FileName = FileName

    def __repr__(self):
        return f'<TUIResourceTexture_Common ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['FileName']]) + '>'


class TBUCKToolAdditionalTextureBank:
    def __init__(self, Textures=None):
        self.Textures = Textures

    def __repr__(self):
        return f'<TBUCKToolAdditionalTextureBank ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Textures']]) + '>'


class TBombAttackStrategyDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TBombAttackStrategyDescriptor>'


class TDiveAttackStrategyDescriptor:
    def __init__(self, MinPitchForDiveInDegree=None, MaxPitchForDiveInDegree=None, MinDiveAlignmentDuration=None):
        self.MinPitchForDiveInDegree = MinPitchForDiveInDegree
        self.MaxPitchForDiveInDegree = MaxPitchForDiveInDegree
        self.MinDiveAlignmentDuration = MinDiveAlignmentDuration

    def __repr__(self):
        return f'<TDiveAttackStrategyDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MinPitchForDiveInDegree', 'MaxPitchForDiveInDegree', 'MinDiveAlignmentDuration']]) + '>'


class TDiveMissileAttackStrategyDescriptor:
    def __init__(self, MinPitchForDiveInDegree=None, MaxPitchForDiveInDegree=None, MinDiveAlignmentDuration=None):
        self.MinPitchForDiveInDegree = MinPitchForDiveInDegree
        self.MaxPitchForDiveInDegree = MaxPitchForDiveInDegree
        self.MinDiveAlignmentDuration = MinDiveAlignmentDuration

    def __repr__(self):
        return f'<TDiveMissileAttackStrategyDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MinPitchForDiveInDegree', 'MaxPitchForDiveInDegree', 'MinDiveAlignmentDuration']]) + '>'


class TDiveBombAttackStrategyDescriptor:
    def __init__(self, MinPitchForDiveBombInDegree=None, PitchForDiveBombInDegree=None, MaxPitchForDiveBombInDegree=None, DiveBombRecoveryDuration=None):
        self.MinPitchForDiveBombInDegree = MinPitchForDiveBombInDegree
        self.PitchForDiveBombInDegree = PitchForDiveBombInDegree
        self.MaxPitchForDiveBombInDegree = MaxPitchForDiveBombInDegree
        self.DiveBombRecoveryDuration = DiveBombRecoveryDuration

    def __repr__(self):
        return f'<TDiveBombAttackStrategyDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MinPitchForDiveBombInDegree', 'PitchForDiveBombInDegree', 'MaxPitchForDiveBombInDegree', 'DiveBombRecoveryDuration']]) + '>'


class TDogfightAttackStrategyDescriptor:
    def __init__(self, MinDistanceBetweenFighterAndTargetForAttackOnSlowAirplaneStrategy=None, MaxDistanceBetweenFighterAndTargetForLateralMoveOnSlowAirplaneStrategy=None, SpeedRatioForAttackOnSlowAirplaneStrategy=None, SpeedRatioForAttackOnVerySlowAirplaneStrategy=None, MaxAngleDifferenceWithTargetInDegree=None, MaxAngleToConsiderTargetAheadInDegree=None, AngleToFakeTargetPositionInDegree=None):
        self.MinDistanceBetweenFighterAndTargetForAttackOnSlowAirplaneStrategy = MinDistanceBetweenFighterAndTargetForAttackOnSlowAirplaneStrategy
        self.MaxDistanceBetweenFighterAndTargetForLateralMoveOnSlowAirplaneStrategy = MaxDistanceBetweenFighterAndTargetForLateralMoveOnSlowAirplaneStrategy
        self.SpeedRatioForAttackOnSlowAirplaneStrategy = SpeedRatioForAttackOnSlowAirplaneStrategy
        self.SpeedRatioForAttackOnVerySlowAirplaneStrategy = SpeedRatioForAttackOnVerySlowAirplaneStrategy
        self.MaxAngleDifferenceWithTargetInDegree = MaxAngleDifferenceWithTargetInDegree
        self.MaxAngleToConsiderTargetAheadInDegree = MaxAngleToConsiderTargetAheadInDegree
        self.AngleToFakeTargetPositionInDegree = AngleToFakeTargetPositionInDegree

    def __repr__(self):
        return f'<TDogfightAttackStrategyDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MinDistanceBetweenFighterAndTargetForAttackOnSlowAirplaneStrategy', 'MaxDistanceBetweenFighterAndTargetForLateralMoveOnSlowAirplaneStrategy', 'SpeedRatioForAttackOnSlowAirplaneStrategy', 'SpeedRatioForAttackOnVerySlowAirplaneStrategy', 'MaxAngleDifferenceWithTargetInDegree', 'MaxAngleToConsiderTargetAheadInDegree', 'AngleToFakeTargetPositionInDegree']]) + '>'


class TStukaNosediveAttackStrategyDescriptor:
    def __init__(self, DistanceNosediveGRU=None, WaypointDistanceFromTargetGRU=None, AgilityMultiplicator=None):
        self.DistanceNosediveGRU = DistanceNosediveGRU
        self.WaypointDistanceFromTargetGRU = WaypointDistanceFromTargetGRU
        self.AgilityMultiplicator = AgilityMultiplicator

    def __repr__(self):
        return f'<TStukaNosediveAttackStrategyDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['DistanceNosediveGRU', 'WaypointDistanceFromTargetGRU', 'AgilityMultiplicator']]) + '>'


class TAirGroundMissileAttackStrategyDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TAirGroundMissileAttackStrategyDescriptor>'


class TDebugModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TDebugModuleDescriptor>'


class TTypeUnitModuleDescriptor:
    def __init__(self, TypeUnitFormation=None, MotherCountry=None, AcknowUnitType=None, Nationalite=None):
        self.TypeUnitFormation = TypeUnitFormation
        self.MotherCountry = MotherCountry
        self.AcknowUnitType = AcknowUnitType
        self.Nationalite = Nationalite

    def __repr__(self):
        return f'<TTypeUnitModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TypeUnitFormation', 'MotherCountry', 'AcknowUnitType', 'Nationalite']]) + '>'


class TEntityDescriptorConstantesSelector:
    def __init__(self, ConstantesByWorld=None):
        self.ConstantesByWorld = ConstantesByWorld

    def __repr__(self):
        return f'<TEntityDescriptorConstantesSelector ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ConstantesByWorld']]) + '>'


class TCriticalEffectModuleDescriptor:
    def __init__(self, PierceEffectsOnSides=None, TerrainCriticalEffectTimer=None, PierceEffectsOnRear=None, EffectsOnTop=None, RicochetEffectsOnFront=None, RicochetEffectsOnRear=None, EffectsOnSides=None, Bounds=None, EffectsFromTerrain=None, PierceEffectsOnTop=None, EffectsOnRear=None, RicochetEffectsOnSides=None, PierceEffectsOnFront=None, RicochetEffectsOnTop=None, EffectsOnFront=None):
        self.PierceEffectsOnSides = PierceEffectsOnSides
        self.TerrainCriticalEffectTimer = TerrainCriticalEffectTimer
        self.PierceEffectsOnRear = PierceEffectsOnRear
        self.EffectsOnTop = EffectsOnTop
        self.RicochetEffectsOnFront = RicochetEffectsOnFront
        self.RicochetEffectsOnRear = RicochetEffectsOnRear
        self.EffectsOnSides = EffectsOnSides
        self.Bounds = Bounds
        self.EffectsFromTerrain = EffectsFromTerrain
        self.PierceEffectsOnTop = PierceEffectsOnTop
        self.EffectsOnRear = EffectsOnRear
        self.RicochetEffectsOnSides = RicochetEffectsOnSides
        self.PierceEffectsOnFront = PierceEffectsOnFront
        self.RicochetEffectsOnTop = RicochetEffectsOnTop
        self.EffectsOnFront = EffectsOnFront

    def __repr__(self):
        return f'<TCriticalEffectModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['PierceEffectsOnSides', 'TerrainCriticalEffectTimer', 'PierceEffectsOnRear', 'EffectsOnTop', 'RicochetEffectsOnFront', 'RicochetEffectsOnRear', 'EffectsOnSides', 'Bounds', 'EffectsFromTerrain', 'PierceEffectsOnTop', 'EffectsOnRear', 'RicochetEffectsOnSides', 'PierceEffectsOnFront', 'RicochetEffectsOnTop', 'EffectsOnFront']]) + '>'


class AirplaneCriticalEffect_WingsDamaged:
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return f'<AirplaneCriticalEffect_WingsDamaged ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Roll']]) + '>'


class AirplaneCriticalEffect_EngineOnFire:
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return f'<AirplaneCriticalEffect_EngineOnFire ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Roll']]) + '>'


class AirplaneCriticalEffect_PropellerDamaged:
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return f'<AirplaneCriticalEffect_PropellerDamaged ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Roll']]) + '>'


class AirplaneCriticalEffect_EngineDamaged:
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return f'<AirplaneCriticalEffect_EngineDamaged ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Roll']]) + '>'


class AirplaneCriticalEffect_FloatCarburatorFailure:
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return f'<AirplaneCriticalEffect_FloatCarburatorFailure ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Roll']]) + '>'


class AirplaneCriticalEffect_OilLeak:
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return f'<AirplaneCriticalEffect_OilLeak ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Roll']]) + '>'


class AirplaneCriticalEffect_EngineOverheating:
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return f'<AirplaneCriticalEffect_EngineOverheating ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Roll']]) + '>'


class AirplaneCriticalEffect_EngineStalling:
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return f'<AirplaneCriticalEffect_EngineStalling ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Roll']]) + '>'


class AirplaneCriticalEffect_ElevatorDamaged:
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return f'<AirplaneCriticalEffect_ElevatorDamaged ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Roll']]) + '>'


class AirplaneCriticalEffect_FuelTankLeaking:
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return f'<AirplaneCriticalEffect_FuelTankLeaking ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Roll']]) + '>'


class AirplaneCriticalEffect_RadiatorDamaged:
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return f'<AirplaneCriticalEffect_RadiatorDamaged ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Roll']]) + '>'


class AirplaneCriticalEffect_RadiatorOverheating:
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return f'<AirplaneCriticalEffect_RadiatorOverheating ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Roll']]) + '>'


class AirplaneCriticalEffect_PilotInjured:
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return f'<AirplaneCriticalEffect_PilotInjured ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Roll']]) + '>'


class AirplaneCriticalEffect_PilotPanicked:
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return f'<AirplaneCriticalEffect_PilotPanicked ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Roll']]) + '>'


class AirplaneCriticalEffect_PilotUnconscious:
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return f'<AirplaneCriticalEffect_PilotUnconscious ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Roll']]) + '>'


class AirplaneCriticalEffect_WeaponsJammed:
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return f'<AirplaneCriticalEffect_WeaponsJammed ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Roll']]) + '>'


class AirplaneCriticalEffect_AileronDamaged:
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return f'<AirplaneCriticalEffect_AileronDamaged ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Roll']]) + '>'


class AirplaneCriticalEffect_TailDamaged:
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return f'<AirplaneCriticalEffect_TailDamaged ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Roll']]) + '>'


class AirplaneCriticalEffect_FuelTankOnFire:
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return f'<AirplaneCriticalEffect_FuelTankOnFire ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Roll']]) + '>'


class AirplaneCriticalEffect_RudderDamaged:
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return f'<AirplaneCriticalEffect_RudderDamaged ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Roll']]) + '>'


class TemplateCriticalEffectModule_GroundUnit:
    def __init__(self, PackEffetCritique=None):
        self.PackEffetCritique = PackEffetCritique

    def __repr__(self):
        return f'<TemplateCriticalEffectModule_GroundUnit ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['PackEffetCritique']]) + '>'


class HelicoCriticalEffect_HUD:
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return f'<HelicoCriticalEffect_HUD ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Roll']]) + '>'


class HelicoCriticalEffect_CrewInjured:
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return f'<HelicoCriticalEffect_CrewInjured ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Roll']]) + '>'


class HelicoCriticalEffect_MainRotorDamaged:
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return f'<HelicoCriticalEffect_MainRotorDamaged ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Roll']]) + '>'


class HelicoCriticalEffect_Turbine_Engine_Failure:
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return f'<HelicoCriticalEffect_Turbine_Engine_Failure ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Roll']]) + '>'


class HelicoCriticalEffect_turbineOnFire:
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return f'<HelicoCriticalEffect_turbineOnFire ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Roll']]) + '>'


class HelicoCriticalEffect_FuelTankOnFire:
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return f'<HelicoCriticalEffect_FuelTankOnFire ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Roll']]) + '>'


class HelicoCriticalEffect_FuelTankLeaking:
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return f'<HelicoCriticalEffect_FuelTankLeaking ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Roll']]) + '>'


class HelicoCriticalEffect_WeaponsJammed:
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return f'<HelicoCriticalEffect_WeaponsJammed ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Roll']]) + '>'


class HelicoCriticalEffect_Hydraulic_Fluid_Fire:
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return f'<HelicoCriticalEffect_Hydraulic_Fluid_Fire ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Roll']]) + '>'


class HelicoCriticalEffect_TailRotorDamaged:
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return f'<HelicoCriticalEffect_TailRotorDamaged ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Roll']]) + '>'


class CriticalEffect_AmmoExplosion:
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return f'<CriticalEffect_AmmoExplosion ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Roll']]) + '>'


class CriticalEffect_Bounce:
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return f'<CriticalEffect_Bounce ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Roll']]) + '>'


class TCriticalEffectDescriptor:
    def __init__(self, Token=None, HappeningKey=None, EffectsPack=None, TimeOut=None, RepairCost=None, Unique=None, DisplayOnDeath=None):
        self.Token = Token
        self.HappeningKey = HappeningKey
        self.EffectsPack = EffectsPack
        self.TimeOut = TimeOut
        self.RepairCost = RepairCost
        self.Unique = Unique
        self.DisplayOnDeath = DisplayOnDeath

    def __repr__(self):
        return f'<TCriticalEffectDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Token', 'HappeningKey', 'EffectsPack', 'TimeOut', 'RepairCost', 'Unique', 'DisplayOnDeath']]) + '>'


class TLocalisationDicoResource:
    def __init__(self, CanBeMissing=None, DicoToken=None, FileName=None):
        self.CanBeMissing = CanBeMissing
        self.DicoToken = DicoToken
        self.FileName = FileName

    def __repr__(self):
        return f'<TLocalisationDicoResource ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['CanBeMissing', 'DicoToken', 'FileName']]) + '>'


class TAllianceDescriptionModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TAllianceDescriptionModuleDescriptor>'


class TAllianceScoreModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TAllianceScoreModuleDescriptor>'


class TAllianceRelationsModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TAllianceRelationsModuleDescriptor>'


class TIAAllianceAirManagerModuleDescriptor:
    def __init__(self, MemoryTurnLength=None):
        self.MemoryTurnLength = MemoryTurnLength

    def __repr__(self):
        return f'<TIAAllianceAirManagerModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MemoryTurnLength']]) + '>'


class TGroupModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TGroupModuleDescriptor>'


class TStateEngineGroupModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TStateEngineGroupModuleDescriptor>'


class TActionPointsReachModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TActionPointsReachModuleDescriptor>'


class TIALinkToGroupModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TIALinkToGroupModuleDescriptor>'


class TStrategicSequenceModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TStrategicSequenceModuleDescriptor>'


class TStrategicAerialModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TStrategicAerialModuleDescriptor>'


class TTeamCurrencyManagerModuleDescriptor:
    def __init__(self, PiggyBanks=None):
        self.PiggyBanks = PiggyBanks

    def __repr__(self):
        return f'<TTeamCurrencyManagerModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['PiggyBanks']]) + '>'


class TPiggyBankDescriptor:
    def __init__(self, CurrencyType=None):
        self.CurrencyType = CurrencyType

    def __repr__(self):
        return f'<TPiggyBankDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['CurrencyType']]) + '>'


class TStrategicTeamProductionModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TStrategicTeamProductionModuleDescriptor>'


class TFactoryModuleDescriptor:
    def __init__(self, Factories=None):
        self.Factories = Factories

    def __repr__(self):
        return f'<TFactoryModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Factories']]) + '>'


class TVirtualFactoryDescriptor:
    def __init__(self, FactoryType=None, IsSimultaneous=None):
        self.FactoryType = FactoryType
        self.IsSimultaneous = IsSimultaneous

    def __repr__(self):
        return f'<TVirtualFactoryDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['FactoryType', 'IsSimultaneous']]) + '>'


class TTeamDescriptionModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TTeamDescriptionModuleDescriptor>'


class TTeamUnitsModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TTeamUnitsModuleDescriptor>'


class TEffectApplierModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TEffectApplierModuleDescriptor>'


class TLinkAllianceModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TLinkAllianceModuleDescriptor>'


class TTeamForAIModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TTeamForAIModuleDescriptor>'


class TTeamDefeatModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TTeamDefeatModuleDescriptor>'


class TTeamScoreModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TTeamScoreModuleDescriptor>'


class TTeamInitialCurrencyModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TTeamInitialCurrencyModuleDescriptor>'


class TFumigeneModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TFumigeneModuleDescriptor>'


class TStatisticsModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TStatisticsModuleDescriptor>'


class TIATeamStrategyModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TIATeamStrategyModuleDescriptor>'


class TStrategicStatisticModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TStrategicStatisticModuleDescriptor>'


class TEntityDescriptorConstantes:
    def __init__(self, GroupUnitDescriptor=None, AllianceUnitDescriptor=None, FakeTargetDescriptor=None, TeamUnitDescriptor=None):
        self.GroupUnitDescriptor = GroupUnitDescriptor
        self.AllianceUnitDescriptor = AllianceUnitDescriptor
        self.FakeTargetDescriptor = FakeTargetDescriptor
        self.TeamUnitDescriptor = TeamUnitDescriptor

    def __repr__(self):
        return f'<TEntityDescriptorConstantes ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['GroupUnitDescriptor', 'AllianceUnitDescriptor', 'FakeTargetDescriptor', 'TeamUnitDescriptor']]) + '>'


class TApparenceModelModuleDescriptor:
    def __init__(self, BlackHoleIdentifier=None, PickableObject=None, GameplayBBoxBoneName=None, ReferenceMesh=None, Depiction=None, DefaultVisibility=None):
        self.BlackHoleIdentifier = BlackHoleIdentifier
        self.PickableObject = PickableObject
        self.GameplayBBoxBoneName = GameplayBBoxBoneName
        self.ReferenceMesh = ReferenceMesh
        self.Depiction = Depiction
        self.DefaultVisibility = DefaultVisibility

    def __repr__(self):
        return f'<TApparenceModelModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['BlackHoleIdentifier', 'PickableObject', 'GameplayBBoxBoneName', 'ReferenceMesh', 'Depiction', 'DefaultVisibility']]) + '>'


class Template_DescriptorFire_Depiction:
    def __init__(self, FX=None, Radius=None, Density=None):
        self.FX = FX
        self.Radius = Radius
        self.Density = Density

    def __repr__(self):
        return f'<Template_DescriptorFire_Depiction ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['FX', 'Radius', 'Density']]) + '>'


class TFireModuleDescriptor:
    def __init__(self, TimeToLive=None, SpreadProbability=None, TimeBeforeSpreadAttempt=None, OverridenSpreadDescriptor=None, IsNewFireProbability=None, IgniteDistricts=None, SmokeDescriptor=None, TimeBetweenBurns=None, TimeBeforeSpreading=None, AmmunitionForBurn=None, RadiusGRU=None):
        self.TimeToLive = TimeToLive
        self.SpreadProbability = SpreadProbability
        self.TimeBeforeSpreadAttempt = TimeBeforeSpreadAttempt
        self.OverridenSpreadDescriptor = OverridenSpreadDescriptor
        self.IsNewFireProbability = IsNewFireProbability
        self.IgniteDistricts = IgniteDistricts
        self.SmokeDescriptor = SmokeDescriptor
        self.TimeBetweenBurns = TimeBetweenBurns
        self.TimeBeforeSpreading = TimeBeforeSpreading
        self.AmmunitionForBurn = AmmunitionForBurn
        self.RadiusGRU = RadiusGRU

    def __repr__(self):
        return f'<TFireModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TimeToLive', 'SpreadProbability', 'TimeBeforeSpreadAttempt', 'OverridenSpreadDescriptor', 'IsNewFireProbability', 'IgniteDistricts', 'SmokeDescriptor', 'TimeBetweenBurns', 'TimeBeforeSpreading', 'AmmunitionForBurn', 'RadiusGRU']]) + '>'


class TAmmunitionDescriptor:
    def __init__(self, TempsDeVisee=None, TirReflexe=None, MaxSuccessiveHitCount=None, IgnoreInflammabilityConditions=None, TargetUnitCenter=None, WeaponDescriptionToken=None, ShotWithoutPhysics=None, DispersionWithoutSorting=None, CanHarmAirplanes=None, PiercingWeapon=None, Arme=None, AltitudeAPorteeMinimaleGRU=None, FireDescriptor=None, TempsEntreDeuxSalves_Max=None, FlightTimeForSpeed=None, TempsEntreDeuxTirs=None, TempsEntreDeuxSalves_Min=None, DisplaySalveAccuracy=None, CanShootOnPosition=None, CorrectedShotDispersionMultiplier=None, InterfaceWeaponTexture=None, FireTriggeringProbability=None, NbSalvosShootOnPosition=None, TempsEntreDeuxSalves=None, PorteeMaximaleGRU=None, PorteeMaximaleHAGRU=None, HitRollRuleDescriptor=None, TempsEntreDeuxFx=None, MissileTimeBetweenCorrections=None, DistanceForSpeedGRU=None, PorteeMinimaleTBAGRU=None, NbrProjectilesSimultanes=None, AngleDispersion=None, AltitudeAPorteeMaximaleGRU=None, MinMaxCategory=None, RadiusSplashPhysicalDamagesGRU=None, AllowSuppressDamageWhenNoImpact=None, RadiusSplashSuppressDamagesGRU=None, ImpactHappening=None, AffichageMunitionParSalve=None, NoiseDissimulationMalus=None, SupplyCost=None, Name=None, ProjectileType=None, MaxAccelerationGRU=None, Guidance=None, FxPower=None, WeaponCursorType=None, WeaponForceNote=None, ShowDamageInUI=None, IsHarmlessForAllies=None, MissileDescriptor=None, PorteeMinimaleHAGRU=None, TirIndirect=None, FluidFriction=None, NbTirParSalves=None, SuppressDamages=None, TargetOnlyOneUnitInDistrict=None, Caliber=None, DamageTypeEvolutionOverRangeDescriptor=None, TraitsToken=None, DescriptorId=None, DispersionAtMaxRangeGRU=None, IsFireAndForget=None, ShotsBeforeMaxNoise=None, AffecteParNombre=None, PhysicalDamages=None, IsSubAmmunition=None, CanShootWhileMoving=None, PorteeMaximaleTBAGRU=None, MaximalSpeedGRU=None, TandemCharge=None, SmokeDescriptor=None, InterdireTirReflexe=None, PorteeMinimaleGRU=None, TypeCategoryName=None, ForceHitTopArmor=None, CorrectedShotAimtimeMultiplier=None, DispersionAtMinRangeGRU=None):
        self.TempsDeVisee = TempsDeVisee
        self.TirReflexe = TirReflexe
        self.MaxSuccessiveHitCount = MaxSuccessiveHitCount
        self.IgnoreInflammabilityConditions = IgnoreInflammabilityConditions
        self.TargetUnitCenter = TargetUnitCenter
        self.WeaponDescriptionToken = WeaponDescriptionToken
        self.ShotWithoutPhysics = ShotWithoutPhysics
        self.DispersionWithoutSorting = DispersionWithoutSorting
        self.CanHarmAirplanes = CanHarmAirplanes
        self.PiercingWeapon = PiercingWeapon
        self.Arme = Arme
        self.AltitudeAPorteeMinimaleGRU = AltitudeAPorteeMinimaleGRU
        self.FireDescriptor = FireDescriptor
        self.TempsEntreDeuxSalves_Max = TempsEntreDeuxSalves_Max
        self.FlightTimeForSpeed = FlightTimeForSpeed
        self.TempsEntreDeuxTirs = TempsEntreDeuxTirs
        self.TempsEntreDeuxSalves_Min = TempsEntreDeuxSalves_Min
        self.DisplaySalveAccuracy = DisplaySalveAccuracy
        self.CanShootOnPosition = CanShootOnPosition
        self.CorrectedShotDispersionMultiplier = CorrectedShotDispersionMultiplier
        self.InterfaceWeaponTexture = InterfaceWeaponTexture
        self.FireTriggeringProbability = FireTriggeringProbability
        self.NbSalvosShootOnPosition = NbSalvosShootOnPosition
        self.TempsEntreDeuxSalves = TempsEntreDeuxSalves
        self.PorteeMaximaleGRU = PorteeMaximaleGRU
        self.PorteeMaximaleHAGRU = PorteeMaximaleHAGRU
        self.HitRollRuleDescriptor = HitRollRuleDescriptor
        self.TempsEntreDeuxFx = TempsEntreDeuxFx
        self.MissileTimeBetweenCorrections = MissileTimeBetweenCorrections
        self.DistanceForSpeedGRU = DistanceForSpeedGRU
        self.PorteeMinimaleTBAGRU = PorteeMinimaleTBAGRU
        self.NbrProjectilesSimultanes = NbrProjectilesSimultanes
        self.AngleDispersion = AngleDispersion
        self.AltitudeAPorteeMaximaleGRU = AltitudeAPorteeMaximaleGRU
        self.MinMaxCategory = MinMaxCategory
        self.RadiusSplashPhysicalDamagesGRU = RadiusSplashPhysicalDamagesGRU
        self.AllowSuppressDamageWhenNoImpact = AllowSuppressDamageWhenNoImpact
        self.RadiusSplashSuppressDamagesGRU = RadiusSplashSuppressDamagesGRU
        self.ImpactHappening = ImpactHappening
        self.AffichageMunitionParSalve = AffichageMunitionParSalve
        self.NoiseDissimulationMalus = NoiseDissimulationMalus
        self.SupplyCost = SupplyCost
        self.Name = Name
        self.ProjectileType = ProjectileType
        self.MaxAccelerationGRU = MaxAccelerationGRU
        self.Guidance = Guidance
        self.FxPower = FxPower
        self.WeaponCursorType = WeaponCursorType
        self.WeaponForceNote = WeaponForceNote
        self.ShowDamageInUI = ShowDamageInUI
        self.IsHarmlessForAllies = IsHarmlessForAllies
        self.MissileDescriptor = MissileDescriptor
        self.PorteeMinimaleHAGRU = PorteeMinimaleHAGRU
        self.TirIndirect = TirIndirect
        self.FluidFriction = FluidFriction
        self.NbTirParSalves = NbTirParSalves
        self.SuppressDamages = SuppressDamages
        self.TargetOnlyOneUnitInDistrict = TargetOnlyOneUnitInDistrict
        self.Caliber = Caliber
        self.DamageTypeEvolutionOverRangeDescriptor = DamageTypeEvolutionOverRangeDescriptor
        self.TraitsToken = TraitsToken
        self.DescriptorId = DescriptorId
        self.DispersionAtMaxRangeGRU = DispersionAtMaxRangeGRU
        self.IsFireAndForget = IsFireAndForget
        self.ShotsBeforeMaxNoise = ShotsBeforeMaxNoise
        self.AffecteParNombre = AffecteParNombre
        self.PhysicalDamages = PhysicalDamages
        self.IsSubAmmunition = IsSubAmmunition
        self.CanShootWhileMoving = CanShootWhileMoving
        self.PorteeMaximaleTBAGRU = PorteeMaximaleTBAGRU
        self.MaximalSpeedGRU = MaximalSpeedGRU
        self.TandemCharge = TandemCharge
        self.SmokeDescriptor = SmokeDescriptor
        self.InterdireTirReflexe = InterdireTirReflexe
        self.PorteeMinimaleGRU = PorteeMinimaleGRU
        self.TypeCategoryName = TypeCategoryName
        self.ForceHitTopArmor = ForceHitTopArmor
        self.CorrectedShotAimtimeMultiplier = CorrectedShotAimtimeMultiplier
        self.DispersionAtMinRangeGRU = DispersionAtMinRangeGRU

    def __repr__(self):
        return f'<TAmmunitionDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TempsDeVisee', 'TirReflexe', 'MaxSuccessiveHitCount', 'IgnoreInflammabilityConditions', 'TargetUnitCenter', 'WeaponDescriptionToken', 'ShotWithoutPhysics', 'DispersionWithoutSorting', 'CanHarmAirplanes', 'PiercingWeapon', 'Arme', 'AltitudeAPorteeMinimaleGRU', 'FireDescriptor', 'TempsEntreDeuxSalves_Max', 'FlightTimeForSpeed', 'TempsEntreDeuxTirs', 'TempsEntreDeuxSalves_Min', 'DisplaySalveAccuracy', 'CanShootOnPosition', 'CorrectedShotDispersionMultiplier', 'InterfaceWeaponTexture', 'FireTriggeringProbability', 'NbSalvosShootOnPosition', 'TempsEntreDeuxSalves', 'PorteeMaximaleGRU', 'PorteeMaximaleHAGRU', 'HitRollRuleDescriptor', 'TempsEntreDeuxFx', 'MissileTimeBetweenCorrections', 'DistanceForSpeedGRU', 'PorteeMinimaleTBAGRU', 'NbrProjectilesSimultanes', 'AngleDispersion', 'AltitudeAPorteeMaximaleGRU', 'MinMaxCategory', 'RadiusSplashPhysicalDamagesGRU', 'AllowSuppressDamageWhenNoImpact', 'RadiusSplashSuppressDamagesGRU', 'ImpactHappening', 'AffichageMunitionParSalve', 'NoiseDissimulationMalus', 'SupplyCost', 'Name', 'ProjectileType', 'MaxAccelerationGRU', 'Guidance', 'FxPower', 'WeaponCursorType', 'WeaponForceNote', 'ShowDamageInUI', 'IsHarmlessForAllies', 'MissileDescriptor', 'PorteeMinimaleHAGRU', 'TirIndirect', 'FluidFriction', 'NbTirParSalves', 'SuppressDamages', 'TargetOnlyOneUnitInDistrict', 'Caliber', 'DamageTypeEvolutionOverRangeDescriptor', 'TraitsToken', 'DescriptorId', 'DispersionAtMaxRangeGRU', 'IsFireAndForget', 'ShotsBeforeMaxNoise', 'AffecteParNombre', 'PhysicalDamages', 'IsSubAmmunition', 'CanShootWhileMoving', 'PorteeMaximaleTBAGRU', 'MaximalSpeedGRU', 'TandemCharge', 'SmokeDescriptor', 'InterdireTirReflexe', 'PorteeMinimaleGRU', 'TypeCategoryName', 'ForceHitTopArmor', 'CorrectedShotAimtimeMultiplier', 'DispersionAtMinRangeGRU']]) + '>'


class TDiceHitRollRuleDescriptor:
    def __init__(self, DescriptorId=None, BaseCriticModifier=None, BaseHitValueModifiers=None, DistanceToTarget=None):
        self.DescriptorId = DescriptorId
        self.BaseCriticModifier = BaseCriticModifier
        self.BaseHitValueModifiers = BaseHitValueModifiers
        self.DistanceToTarget = DistanceToTarget

    def __repr__(self):
        return f'<TDiceHitRollRuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['DescriptorId', 'BaseCriticModifier', 'BaseHitValueModifiers', 'DistanceToTarget']]) + '>'


class TInfluencePositionModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TInfluencePositionModuleDescriptor>'


class TInfluenceDataModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TInfluenceDataModuleDescriptor>'


class TOrderDisplayModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TOrderDisplayModuleDescriptor>'


class TCapturableModuleDescriptor:
    def __init__(self, RadiusCaptureGRU=None):
        self.RadiusCaptureGRU = RadiusCaptureGRU

    def __repr__(self):
        return f'<TCapturableModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['RadiusCaptureGRU']]) + '>'


class TGroupableUnitModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TGroupableUnitModuleDescriptor>'


class TPlayerMissionModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TPlayerMissionModuleDescriptor>'


class TTargetManagerModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TTargetManagerModuleDescriptor>'


class TIAStratZoneIndexModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TIAStratZoneIndexModuleDescriptor>'


class TOrderableModuleDescriptor:
    def __init__(self, UnlockableOrders=None):
        self.UnlockableOrders = UnlockableOrders

    def __repr__(self):
        return f'<TOrderableModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['UnlockableOrders']]) + '>'


class Template_DescriptorSmoke_Depiction:
    def __init__(self, Radius=None, Height=None, Density=None):
        self.Radius = Radius
        self.Height = Height
        self.Density = Density

    def __repr__(self):
        return f'<Template_DescriptorSmoke_Depiction ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Radius', 'Height', 'Density']]) + '>'


class TSmokeModuleDescriptor:
    def __init__(self, AltitudeGRU=None, RadiusGRU=None, TimeToLive=None, Terrain=None):
        self.AltitudeGRU = AltitudeGRU
        self.RadiusGRU = RadiusGRU
        self.TimeToLive = TimeToLive
        self.Terrain = Terrain

    def __repr__(self):
        return f'<TSmokeModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['AltitudeGRU', 'RadiusGRU', 'TimeToLive', 'Terrain']]) + '>'


class DeckPackDescriptor:
    def __init__(self, Xp=None, Transport=None, Unit=None):
        self.Xp = Xp
        self.Transport = Transport
        self.Unit = Unit

    def __repr__(self):
        return f'<DeckPackDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Xp', 'Transport', 'Unit']]) + '>'


class TDeckDescriptor:
    def __init__(self, DeckDivision=None, DeckPackList=None, DeckCombatGroupList=None, DeckName=None, DeckIdentifier=None, Superior=None):
        self.DeckDivision = DeckDivision
        self.DeckPackList = DeckPackList
        self.DeckCombatGroupList = DeckCombatGroupList
        self.DeckName = DeckName
        self.DeckIdentifier = DeckIdentifier
        self.Superior = Superior

    def __repr__(self):
        return f'<TDeckDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['DeckDivision', 'DeckPackList', 'DeckCombatGroupList', 'DeckName', 'DeckIdentifier', 'Superior']]) + '>'


class TDeckCombatGroupDescriptor:
    def __init__(self, IsHQ=None, Name=None, SmartGroupList=None):
        self.IsHQ = IsHQ
        self.Name = Name
        self.SmartGroupList = SmartGroupList

    def __repr__(self):
        return f'<TDeckCombatGroupDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['IsHQ', 'Name', 'SmartGroupList']]) + '>'


class TDeckSmartGroupDescriptor:
    def __init__(self, IsHQ=None, Name=None, PackIndexUnitNumberList=None):
        self.IsHQ = IsHQ
        self.Name = Name
        self.PackIndexUnitNumberList = PackIndexUnitNumberList

    def __repr__(self):
        return f'<TDeckSmartGroupDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['IsHQ', 'Name', 'PackIndexUnitNumberList']]) + '>'


class TDeckDescriptorList:
    def __init__(self, DeckListForAutoFill=None, DeckListForIdentifier=None):
        self.DeckListForAutoFill = DeckListForAutoFill
        self.DeckListForIdentifier = DeckListForIdentifier

    def __repr__(self):
        return f'<TDeckDescriptorList ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['DeckListForAutoFill', 'DeckListForIdentifier']]) + '>'


class TDeckSerializer:
    def __init__(self, DivisionIds=None, UnitIds=None):
        self.DivisionIds = DivisionIds
        self.UnitIds = UnitIds

    def __repr__(self):
        return f'<TDeckSerializer ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['DivisionIds', 'UnitIds']]) + '>'


class TDeckDivisionList:
    def __init__(self, DivisionList=None):
        self.DivisionList = DivisionList

    def __repr__(self):
        return f'<TDeckDivisionList ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['DivisionList']]) + '>'


class TDeckDivisionRules:
    def __init__(self, DivisionRules=None):
        self.DivisionRules = DivisionRules

    def __repr__(self):
        return f'<TDeckDivisionRules ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['DivisionRules']]) + '>'


class TDeckDivisionRule:
    def __init__(self, UnitRuleList=None):
        self.UnitRuleList = UnitRuleList

    def __repr__(self):
        return f'<TDeckDivisionRule ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['UnitRuleList']]) + '>'


class TDeckUniteRule:
    def __init__(self, UnitDescriptor=None, NumberOfUnitInPack=None, NumberOfUnitInPackXPMultiplier=None, AvailableTransportList=None, AvailableWithoutTransport=None):
        self.UnitDescriptor = UnitDescriptor
        self.NumberOfUnitInPack = NumberOfUnitInPack
        self.NumberOfUnitInPackXPMultiplier = NumberOfUnitInPackXPMultiplier
        self.AvailableTransportList = AvailableTransportList
        self.AvailableWithoutTransport = AvailableWithoutTransport

    def __repr__(self):
        return f'<TDeckUniteRule ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['UnitDescriptor', 'NumberOfUnitInPack', 'NumberOfUnitInPackXPMultiplier', 'AvailableTransportList', 'AvailableWithoutTransport']]) + '>'


class TDeckDivisionDescriptor:
    def __init__(self, TypeTexture=None, PackList=None, CountryId=None, DescriptorId=None, DescriptionHintTitleToken=None, CostMatrix=None, DivisionTags=None, StrategicLabelColor=None, DivisionName=None, PortraitTexture=None, EmblemTexture=None, CfgName=None, DivisionPowerClassification=None, MaxActivationPoints=None, DivisionNationalite=None):
        self.TypeTexture = TypeTexture
        self.PackList = PackList
        self.CountryId = CountryId
        self.DescriptorId = DescriptorId
        self.DescriptionHintTitleToken = DescriptionHintTitleToken
        self.CostMatrix = CostMatrix
        self.DivisionTags = DivisionTags
        self.StrategicLabelColor = StrategicLabelColor
        self.DivisionName = DivisionName
        self.PortraitTexture = PortraitTexture
        self.EmblemTexture = EmblemTexture
        self.CfgName = CfgName
        self.DivisionPowerClassification = DivisionPowerClassification
        self.MaxActivationPoints = MaxActivationPoints
        self.DivisionNationalite = DivisionNationalite

    def __repr__(self):
        return f'<TDeckDivisionDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TypeTexture', 'PackList', 'CountryId', 'DescriptorId', 'DescriptionHintTitleToken', 'CostMatrix', 'DivisionTags', 'StrategicLabelColor', 'DivisionName', 'PortraitTexture', 'EmblemTexture', 'CfgName', 'DivisionPowerClassification', 'MaxActivationPoints', 'DivisionNationalite']]) + '>'


class BuildingCadavreModuleDescriptor:
    def __init__(self, CadavreDuration=None, ModuleDescriptorsToSteal=None):
        self.CadavreDuration = CadavreDuration
        self.ModuleDescriptorsToSteal = ModuleDescriptorsToSteal

    def __repr__(self):
        return f'<BuildingCadavreModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['CadavreDuration', 'ModuleDescriptorsToSteal']]) + '>'


class TExperienceModuleDescriptor:
    def __init__(self, ExperienceGainBySecond=None, CanWinExperience=None, ExperienceMultiplierBonusOnKill=None, ExperienceLevelsPackDescriptor=None):
        self.ExperienceGainBySecond = ExperienceGainBySecond
        self.CanWinExperience = CanWinExperience
        self.ExperienceMultiplierBonusOnKill = ExperienceMultiplierBonusOnKill
        self.ExperienceLevelsPackDescriptor = ExperienceLevelsPackDescriptor

    def __repr__(self):
        return f'<TExperienceModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ExperienceGainBySecond', 'CanWinExperience', 'ExperienceMultiplierBonusOnKill', 'ExperienceLevelsPackDescriptor']]) + '>'


class TSupplyModuleDescriptor:
    def __init__(self, SupplyCapacity=None, SupplyDescriptor=None, SupplyPriority=None):
        self.SupplyCapacity = SupplyCapacity
        self.SupplyDescriptor = SupplyDescriptor
        self.SupplyPriority = SupplyPriority

    def __repr__(self):
        return f'<TSupplyModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['SupplyCapacity', 'SupplyDescriptor', 'SupplyPriority']]) + '>'


class TBaseDamageModuleDescriptor:
    def __init__(self, StunDamageLevelsPack=None, MaxSuppressionDamages=None, MaxStunDamages=None, MaxPhysicalDamages=None, SuppressDamageLevelsPack=None, PhysicalDamageLevelsPack=None):
        self.StunDamageLevelsPack = StunDamageLevelsPack
        self.MaxSuppressionDamages = MaxSuppressionDamages
        self.MaxStunDamages = MaxStunDamages
        self.MaxPhysicalDamages = MaxPhysicalDamages
        self.SuppressDamageLevelsPack = SuppressDamageLevelsPack
        self.PhysicalDamageLevelsPack = PhysicalDamageLevelsPack

    def __repr__(self):
        return f'<TBaseDamageModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['StunDamageLevelsPack', 'MaxSuppressionDamages', 'MaxStunDamages', 'MaxPhysicalDamages', 'SuppressDamageLevelsPack', 'PhysicalDamageLevelsPack']]) + '>'


class TDamageModuleDescriptor:
    def __init__(self, KillWhenDamagesReachMax=None, UseTopArmorAgainstFire=None, SuppressDamagesRegenRatio=None, AutoOrientation=None, BlindageProperties=None, HitRollECM=None, StunDamagesRegen=None):
        self.KillWhenDamagesReachMax = KillWhenDamagesReachMax
        self.UseTopArmorAgainstFire = UseTopArmorAgainstFire
        self.SuppressDamagesRegenRatio = SuppressDamagesRegenRatio
        self.AutoOrientation = AutoOrientation
        self.BlindageProperties = BlindageProperties
        self.HitRollECM = HitRollECM
        self.StunDamagesRegen = StunDamagesRegen

    def __repr__(self):
        return f'<TDamageModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['KillWhenDamagesReachMax', 'UseTopArmorAgainstFire', 'SuppressDamagesRegenRatio', 'AutoOrientation', 'BlindageProperties', 'HitRollECM', 'StunDamagesRegen']]) + '>'


class TBlindageProperties:
    def __init__(self, ExplosiveReactiveArmor=None, ResistanceSides=None, ResistanceFront=None, ResistanceRear=None, ResistanceTop=None):
        self.ExplosiveReactiveArmor = ExplosiveReactiveArmor
        self.ResistanceSides = ResistanceSides
        self.ResistanceFront = ResistanceFront
        self.ResistanceRear = ResistanceRear
        self.ResistanceTop = ResistanceTop

    def __repr__(self):
        return f'<TBlindageProperties ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ExplosiveReactiveArmor', 'ResistanceSides', 'ResistanceFront', 'ResistanceRear', 'ResistanceTop']]) + '>'


class TResistanceTypeRTTI:
    def __init__(self, Family=None, Index=None):
        self.Family = Family
        self.Index = Index

    def __repr__(self):
        return f'<TResistanceTypeRTTI ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Family', 'Index']]) + '>'


class BuildingApparenceModelModuleDescriptor:
    def __init__(self, BlackHoleIdentifier=None, SymbolName=None):
        self.BlackHoleIdentifier = BlackHoleIdentifier
        self.SymbolName = SymbolName

    def __repr__(self):
        return f'<BuildingApparenceModelModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['BlackHoleIdentifier', 'SymbolName']]) + '>'


class TCadavreGeneratorModuleDescriptor:
    def __init__(self, CadavreDescriptor=None):
        self.CadavreDescriptor = CadavreDescriptor

    def __repr__(self):
        return f'<TCadavreGeneratorModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['CadavreDescriptor']]) + '>'


class TIAStratModuleDescriptor:
    def __init__(self, DatabaseId=None, GameplayBehavior=None):
        self.DatabaseId = DatabaseId
        self.GameplayBehavior = GameplayBehavior

    def __repr__(self):
        return f'<TIAStratModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['DatabaseId', 'GameplayBehavior']]) + '>'


class TProductionModuleDescriptor:
    def __init__(self, Factory=None, ProductionRessourcesNeeded=None, ProductionTime=None):
        self.Factory = Factory
        self.ProductionRessourcesNeeded = ProductionRessourcesNeeded
        self.ProductionTime = ProductionTime

    def __repr__(self):
        return f'<TProductionModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Factory', 'ProductionRessourcesNeeded', 'ProductionTime']]) + '>'


class TTacticalLabelModuleDescriptor:
    def __init__(self, IdentifiedTexture=None, PositionHeightOffset=None, NbSoldiers=None, UnidentifiedTexture=None, MultiSelectionSortingOrder=None):
        self.IdentifiedTexture = IdentifiedTexture
        self.PositionHeightOffset = PositionHeightOffset
        self.NbSoldiers = NbSoldiers
        self.UnidentifiedTexture = UnidentifiedTexture
        self.MultiSelectionSortingOrder = MultiSelectionSortingOrder

    def __repr__(self):
        return f'<TTacticalLabelModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['IdentifiedTexture', 'PositionHeightOffset', 'NbSoldiers', 'UnidentifiedTexture', 'MultiSelectionSortingOrder']]) + '>'


class TBUCKToolAlternativeValues_TUIValueTextureNameFromTEugBMutableInteger:
    def __init__(self, CommandNameTrigger=None, Values=None, Alterator=None):
        self.CommandNameTrigger = CommandNameTrigger
        self.Values = Values
        self.Alterator = Alterator

    def __repr__(self):
        return f'<TBUCKToolAlternativeValues_TUIValueTextureNameFromTEugBMutableInteger ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['CommandNameTrigger', 'Values', 'Alterator']]) + '>'


class TUnitUpkeepModuleDescriptor:
    def __init__(self, UpkeepPercentage=None):
        self.UpkeepPercentage = UpkeepPercentage

    def __repr__(self):
        return f'<TUnitUpkeepModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['UpkeepPercentage']]) + '>'


class TUnitUIModuleDescriptor:
    def __init__(self, SpecialtiesList=None, DisplayRoadSpeedInKmph=None, InfoPanelConfigurationToken=None, NameToken=None, CountryTexture=None, GenerateName=None, MenuIconTexture=None, TypeStrategicCount=None, UpgradeFromUnit=None, UnitRole=None, ButtonTexture=None):
        self.SpecialtiesList = SpecialtiesList
        self.DisplayRoadSpeedInKmph = DisplayRoadSpeedInKmph
        self.InfoPanelConfigurationToken = InfoPanelConfigurationToken
        self.NameToken = NameToken
        self.CountryTexture = CountryTexture
        self.GenerateName = GenerateName
        self.MenuIconTexture = MenuIconTexture
        self.TypeStrategicCount = TypeStrategicCount
        self.UpgradeFromUnit = UpgradeFromUnit
        self.UnitRole = UnitRole
        self.ButtonTexture = ButtonTexture

    def __repr__(self):
        return f'<TUnitUIModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['SpecialtiesList', 'DisplayRoadSpeedInKmph', 'InfoPanelConfigurationToken', 'NameToken', 'CountryTexture', 'GenerateName', 'MenuIconTexture', 'TypeStrategicCount', 'UpgradeFromUnit', 'UnitRole', 'ButtonTexture']]) + '>'


class TCapaciteDescriptor:
    def __init__(self, Price=None, TypeCible=None, TagsCiblePossible=None, TargetEffect=None, InfluenceMapType=None, Name=None, ActionRadiusWithBoundingBox=None, AreaShape=None, CheckVisibility=None, MaxTargetNb=None, TargetEffectDuration=None, Declenchement=None, CanBeCastFromTransport=None, Conditions=None, RangeGRU=None, CumulEffect=None, CastTime=None, RadiusGRU=None, SelfEffectDuration=None, DisplayRangeColor=None, FeedbackActivationMask=None, TargetMySelf=None, NameToken=None, MinVirtualUnits=None, DescriptorId=None, TargetInBuilding=None, SelfEffect=None, Cooldown=None, MultiplyCost=None, AllowReflexDuringCast=None, TargetInSelf=None, DisplayRangeThickness=None, TargetTeamFilter=None, InfluenceMapAlliance=None, TargetInTransport=None, OrderMustSpreadTargets=None, TagsCibleExcluded=None, TargetWoundedFilter=None):
        self.Price = Price
        self.TypeCible = TypeCible
        self.TagsCiblePossible = TagsCiblePossible
        self.TargetEffect = TargetEffect
        self.InfluenceMapType = InfluenceMapType
        self.Name = Name
        self.ActionRadiusWithBoundingBox = ActionRadiusWithBoundingBox
        self.AreaShape = AreaShape
        self.CheckVisibility = CheckVisibility
        self.MaxTargetNb = MaxTargetNb
        self.TargetEffectDuration = TargetEffectDuration
        self.Declenchement = Declenchement
        self.CanBeCastFromTransport = CanBeCastFromTransport
        self.Conditions = Conditions
        self.RangeGRU = RangeGRU
        self.CumulEffect = CumulEffect
        self.CastTime = CastTime
        self.RadiusGRU = RadiusGRU
        self.SelfEffectDuration = SelfEffectDuration
        self.DisplayRangeColor = DisplayRangeColor
        self.FeedbackActivationMask = FeedbackActivationMask
        self.TargetMySelf = TargetMySelf
        self.NameToken = NameToken
        self.MinVirtualUnits = MinVirtualUnits
        self.DescriptorId = DescriptorId
        self.TargetInBuilding = TargetInBuilding
        self.SelfEffect = SelfEffect
        self.Cooldown = Cooldown
        self.MultiplyCost = MultiplyCost
        self.AllowReflexDuringCast = AllowReflexDuringCast
        self.TargetInSelf = TargetInSelf
        self.DisplayRangeThickness = DisplayRangeThickness
        self.TargetTeamFilter = TargetTeamFilter
        self.InfluenceMapAlliance = InfluenceMapAlliance
        self.TargetInTransport = TargetInTransport
        self.OrderMustSpreadTargets = OrderMustSpreadTargets
        self.TagsCibleExcluded = TagsCibleExcluded
        self.TargetWoundedFilter = TargetWoundedFilter

    def __repr__(self):
        return f'<TCapaciteDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Price', 'TypeCible', 'TagsCiblePossible', 'TargetEffect', 'InfluenceMapType', 'Name', 'ActionRadiusWithBoundingBox', 'AreaShape', 'CheckVisibility', 'MaxTargetNb', 'TargetEffectDuration', 'Declenchement', 'CanBeCastFromTransport', 'Conditions', 'RangeGRU', 'CumulEffect', 'CastTime', 'RadiusGRU', 'SelfEffectDuration', 'DisplayRangeColor', 'FeedbackActivationMask', 'TargetMySelf', 'NameToken', 'MinVirtualUnits', 'DescriptorId', 'TargetInBuilding', 'SelfEffect', 'Cooldown', 'MultiplyCost', 'AllowReflexDuringCast', 'TargetInSelf', 'DisplayRangeThickness', 'TargetTeamFilter', 'InfluenceMapAlliance', 'TargetInTransport', 'OrderMustSpreadTargets', 'TagsCibleExcluded', 'TargetWoundedFilter']]) + '>'


class TConditionTagRaisedInUnit:
    def __init__(self, Tag=None, DescriptorId=None, Amount=None):
        self.Tag = Tag
        self.DescriptorId = DescriptorId
        self.Amount = Amount

    def __repr__(self):
        return f'<TConditionTagRaisedInUnit ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Tag', 'DescriptorId', 'Amount']]) + '>'


class TConditionTagNotRaisedInUnit:
    def __init__(self, Tag=None, DescriptorId=None, Amount=None):
        self.Tag = Tag
        self.DescriptorId = DescriptorId
        self.Amount = Amount

    def __repr__(self):
        return f'<TConditionTagNotRaisedInUnit ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Tag', 'DescriptorId', 'Amount']]) + '>'


class TConditionNotInMovement:
    def __init__(self, DescriptorId=None):
        self.DescriptorId = DescriptorId

    def __repr__(self):
        return f'<TConditionNotInMovement ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['DescriptorId']]) + '>'


class TDamageLevelsPackDescriptor:
    def __init__(self, NameForDebug=None, DamageLevelsDescriptors=None, DescriptorId=None):
        self.NameForDebug = NameForDebug
        self.DamageLevelsDescriptors = DamageLevelsDescriptors
        self.DescriptorId = DescriptorId

    def __repr__(self):
        return f'<TDamageLevelsPackDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['NameForDebug', 'DamageLevelsDescriptors', 'DescriptorId']]) + '>'


class TDamageLevelDescriptor:
    def __init__(self, HitRollModifier=None, MoralModifier=None, EffectsPacks=None, FeedbackOnSelf=None, DescriptorId=None, LocalizationToken=None, TextColor=None, NameForDebug=None, Value=None, AnimationType=None):
        self.HitRollModifier = HitRollModifier
        self.MoralModifier = MoralModifier
        self.EffectsPacks = EffectsPacks
        self.FeedbackOnSelf = FeedbackOnSelf
        self.DescriptorId = DescriptorId
        self.LocalizationToken = LocalizationToken
        self.TextColor = TextColor
        self.NameForDebug = NameForDebug
        self.Value = Value
        self.AnimationType = AnimationType

    def __repr__(self):
        return f'<TDamageLevelDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['HitRollModifier', 'MoralModifier', 'EffectsPacks', 'FeedbackOnSelf', 'DescriptorId', 'LocalizationToken', 'TextColor', 'NameForDebug', 'Value', 'AnimationType']]) + '>'


class TGameplayDamageResistanceContainer:
    def __init__(self, ResistanceFamilyDefinitionList=None, DamageFamilyDefinitionList=None, Values=None):
        self.ResistanceFamilyDefinitionList = ResistanceFamilyDefinitionList
        self.DamageFamilyDefinitionList = DamageFamilyDefinitionList
        self.Values = Values

    def __repr__(self):
        return f'<TGameplayDamageResistanceContainer ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ResistanceFamilyDefinitionList', 'DamageFamilyDefinitionList', 'Values']]) + '>'


class TResistanceTypeFamilyDefinition:
    def __init__(self, MaxIndex=None, Family=None):
        self.MaxIndex = MaxIndex
        self.Family = Family

    def __repr__(self):
        return f'<TResistanceTypeFamilyDefinition ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MaxIndex', 'Family']]) + '>'


class TDamageTypeFamilyDefinition:
    def __init__(self, MaxIndex=None, Family=None):
        self.MaxIndex = MaxIndex
        self.Family = Family

    def __repr__(self):
        return f'<TDamageTypeFamilyDefinition ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MaxIndex', 'Family']]) + '>'


class TResistanceFamilyList:
    def __init__(self, Values=None):
        self.Values = Values

    def __repr__(self):
        return f'<TResistanceFamilyList ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Values']]) + '>'


class TDamageFamilyList:
    def __init__(self, Values=None):
        self.Values = Values

    def __repr__(self):
        return f'<TDamageFamilyList ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Values']]) + '>'


class TStairsDamageTypeEvolutionOverRangeDescriptor:
    def __init__(self, AP=None, DistanceGRU=None):
        self.AP = AP
        self.DistanceGRU = DistanceGRU

    def __repr__(self):
        return f'<TStairsDamageTypeEvolutionOverRangeDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['AP', 'DistanceGRU']]) + '>'


class TDistrictUnitsContainerModuleDescriptor:
    def __init__(self, AllowedTagSet=None, NbSlots=None):
        self.AllowedTagSet = AllowedTagSet
        self.NbSlots = NbSlots

    def __repr__(self):
        return f'<TDistrictUnitsContainerModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['AllowedTagSet', 'NbSlots']]) + '>'


class TDynamicTerrainModuleDescriptor:
    def __init__(self, TerrainToApplyOnInit=None, TerrainToApplyOnDeath=None):
        self.TerrainToApplyOnInit = TerrainToApplyOnInit
        self.TerrainToApplyOnDeath = TerrainToApplyOnDeath

    def __repr__(self):
        return f'<TDynamicTerrainModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TerrainToApplyOnInit', 'TerrainToApplyOnDeath']]) + '>'


class TShootingPointsModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TShootingPointsModuleDescriptor>'


class TMinimapDisplayModuleDescriptor:
    def __init__(self, FollowUnitOrientation=None, Texture=None):
        self.FollowUnitOrientation = FollowUnitOrientation
        self.Texture = Texture

    def __repr__(self):
        return f'<TMinimapDisplayModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['FollowUnitOrientation', 'Texture']]) + '>'


class TGameplayEffectsPacksList:
    def __init__(self, EffectsPacks=None):
        self.EffectsPacks = EffectsPacks

    def __repr__(self):
        return f'<TGameplayEffectsPacksList ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['EffectsPacks']]) + '>'


class TEffectsPackDescriptor:
    def __init__(self, NameForDebug=None, DescriptorId=None, EffectsDescriptors=None):
        self.NameForDebug = NameForDebug
        self.DescriptorId = DescriptorId
        self.EffectsDescriptors = EffectsDescriptors

    def __repr__(self):
        return f'<TEffectsPackDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['NameForDebug', 'DescriptorId', 'EffectsDescriptors']]) + '>'


class TUnitEffectIncreaseWeaponDispersionMaxRangeDescriptor:
    def __init__(self, ModifierType=None, ModifierValue=None):
        self.ModifierType = ModifierType
        self.ModifierValue = ModifierValue

    def __repr__(self):
        return f'<TUnitEffectIncreaseWeaponDispersionMaxRangeDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ModifierType', 'ModifierValue']]) + '>'


class TUnitEffectRaiseTagDescriptor:
    def __init__(self, TagListToRaise=None):
        self.TagListToRaise = TagListToRaise

    def __repr__(self):
        return f'<TUnitEffectRaiseTagDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TagListToRaise']]) + '>'


class TUnitEffectShowLabelIconDescriptor:
    def __init__(self, TextureToken=None):
        self.TextureToken = TextureToken

    def __repr__(self):
        return f'<TUnitEffectShowLabelIconDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TextureToken']]) + '>'


class TUnitEffectIncreaseDamageTakenDescriptor:
    def __init__(self, DamageType=None, ModifierType=None, BonusDamage=None):
        self.DamageType = DamageType
        self.ModifierType = ModifierType
        self.BonusDamage = BonusDamage

    def __repr__(self):
        return f'<TUnitEffectIncreaseDamageTakenDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['DamageType', 'ModifierType', 'BonusDamage']]) + '>'


class TStrategicSupplyMalusEffectDescriptor:
    def __init__(self, ModifierType=None, SupplyMalus=None):
        self.ModifierType = ModifierType
        self.SupplyMalus = SupplyMalus

    def __repr__(self):
        return f'<TStrategicSupplyMalusEffectDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ModifierType', 'SupplyMalus']]) + '>'


class TUnitEffectIncreaseInfluenceValueDescriptor:
    def __init__(self, Bonus=None, ModifierType=None):
        self.Bonus = Bonus
        self.ModifierType = ModifierType

    def __repr__(self):
        return f'<TUnitEffectIncreaseInfluenceValueDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Bonus', 'ModifierType']]) + '>'


class TUnitEffectIncreaseWeaponPorteeMaxDescriptor:
    def __init__(self, ModifierValue=None, ModifierValueGRU=None, ModifierType=None):
        self.ModifierValue = ModifierValue
        self.ModifierValueGRU = ModifierValueGRU
        self.ModifierType = ModifierType

    def __repr__(self):
        return f'<TUnitEffectIncreaseWeaponPorteeMaxDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ModifierValue', 'ModifierValueGRU', 'ModifierType']]) + '>'


class TUnitEffectIncreaseWeaponPorteeMaxHADescriptor:
    def __init__(self, ModifierValue=None, ModifierValueGRU=None, ModifierType=None):
        self.ModifierValue = ModifierValue
        self.ModifierValueGRU = ModifierValueGRU
        self.ModifierType = ModifierType

    def __repr__(self):
        return f'<TUnitEffectIncreaseWeaponPorteeMaxHADescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ModifierValue', 'ModifierValueGRU', 'ModifierType']]) + '>'


class TUnitEffectIncreaseWeaponPorteeMaxProjectileDescriptor:
    def __init__(self, ModifierValue=None, ModifierValueGRU=None, ModifierType=None):
        self.ModifierValue = ModifierValue
        self.ModifierValueGRU = ModifierValueGRU
        self.ModifierType = ModifierType

    def __repr__(self):
        return f'<TUnitEffectIncreaseWeaponPorteeMaxProjectileDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ModifierValue', 'ModifierValueGRU', 'ModifierType']]) + '>'


class TUnitEffectIncreaseWeaponPorteeMaxTBADescriptor:
    def __init__(self, ModifierValue=None, ModifierValueGRU=None, ModifierType=None):
        self.ModifierValue = ModifierValue
        self.ModifierValueGRU = ModifierValueGRU
        self.ModifierType = ModifierType

    def __repr__(self):
        return f'<TUnitEffectIncreaseWeaponPorteeMaxTBADescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ModifierValue', 'ModifierValueGRU', 'ModifierType']]) + '>'


class TUnitEffectIncreaseDispersionDescriptor:
    def __init__(self, BonusDispersion=None, ModifierType=None):
        self.BonusDispersion = BonusDispersion
        self.ModifierType = ModifierType

    def __repr__(self):
        return f'<TUnitEffectIncreaseDispersionDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['BonusDispersion', 'ModifierType']]) + '>'


class TUnitEffectAlterWeaponTempsEntreDeuxSalvesDescriptor:
    def __init__(self, ModifierType=None, ModifierValue=None):
        self.ModifierType = ModifierType
        self.ModifierValue = ModifierValue

    def __repr__(self):
        return f'<TUnitEffectAlterWeaponTempsEntreDeuxSalvesDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ModifierType', 'ModifierValue']]) + '>'


class TUnitEffectAlterWeaponTempsEntreDeuxTirsDescriptor:
    def __init__(self, ModifierType=None, ModifierValue=None):
        self.ModifierType = ModifierType
        self.ModifierValue = ModifierValue

    def __repr__(self):
        return f'<TUnitEffectAlterWeaponTempsEntreDeuxTirsDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ModifierType', 'ModifierValue']]) + '>'


class TUnitEffectIncreaseChassisRotationSpeedDescriptor:
    def __init__(self, ModifierType=None, BonusChassisRotationSpeed=None):
        self.ModifierType = ModifierType
        self.BonusChassisRotationSpeed = BonusChassisRotationSpeed

    def __repr__(self):
        return f'<TUnitEffectIncreaseChassisRotationSpeedDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ModifierType', 'BonusChassisRotationSpeed']]) + '>'


class TUnitEffectIncreaseTurretRotationSpeedDescriptor:
    def __init__(self, BonusTurretRotationSpeed=None, ModifierType=None):
        self.BonusTurretRotationSpeed = BonusTurretRotationSpeed
        self.ModifierType = ModifierType

    def __repr__(self):
        return f'<TUnitEffectIncreaseTurretRotationSpeedDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['BonusTurretRotationSpeed', 'ModifierType']]) + '>'


class TUnitEffectIncreaseSpeedDescriptor:
    def __init__(self, BonusSpeedBaseInPercent=None, ModifierType=None):
        self.BonusSpeedBaseInPercent = BonusSpeedBaseInPercent
        self.ModifierType = ModifierType

    def __repr__(self):
        return f'<TUnitEffectIncreaseSpeedDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['BonusSpeedBaseInPercent', 'ModifierType']]) + '>'


class TBonusWeaponAimtimeEffectDescriptor:
    def __init__(self, ModifierType=None, ModifierValue=None):
        self.ModifierType = ModifierType
        self.ModifierValue = ModifierValue

    def __repr__(self):
        return f'<TBonusWeaponAimtimeEffectDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ModifierType', 'ModifierValue']]) + '>'


class TUnitEffectBonusExperienceLevelDescriptor:
    def __init__(self, ModifierType=None, ExperienceLevelModifier=None):
        self.ModifierType = ModifierType
        self.ExperienceLevelModifier = ExperienceLevelModifier

    def __repr__(self):
        return f'<TUnitEffectBonusExperienceLevelDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ModifierType', 'ExperienceLevelModifier']]) + '>'


class TUnitEffectIncreaseDangerousnessDescriptor:
    def __init__(self, ModifierType=None, BonusDangerousness=None):
        self.ModifierType = ModifierType
        self.BonusDangerousness = BonusDangerousness

    def __repr__(self):
        return f'<TUnitEffectIncreaseDangerousnessDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ModifierType', 'BonusDangerousness']]) + '>'


class TUnitEffectTransportSlotNumberModificationDescriptor:
    def __init__(self, EffectOnTransportSlotNumber=None, ModifierType=None):
        self.EffectOnTransportSlotNumber = EffectOnTransportSlotNumber
        self.ModifierType = ModifierType

    def __repr__(self):
        return f'<TUnitEffectTransportSlotNumberModificationDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['EffectOnTransportSlotNumber', 'ModifierType']]) + '>'


class TUnitEffectIncreaseWeaponPhysicalDamagesDescriptor:
    def __init__(self, ModifierType=None, ModifierValue=None):
        self.ModifierType = ModifierType
        self.ModifierValue = ModifierValue

    def __repr__(self):
        return f'<TUnitEffectIncreaseWeaponPhysicalDamagesDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ModifierType', 'ModifierValue']]) + '>'


class TUnitEffectIncreaseVisionDescriptor:
    def __init__(self, ModifierType=None, BonusVisionBase=None):
        self.ModifierType = ModifierType
        self.BonusVisionBase = BonusVisionBase

    def __repr__(self):
        return f'<TUnitEffectIncreaseVisionDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ModifierType', 'BonusVisionBase']]) + '>'


class TUnitEffectIncreaseSpecializedDetectionDescriptor:
    def __init__(self, VisionType=None, ModifierType=None, BonusValueGRU=None, BonusValue=None):
        self.VisionType = VisionType
        self.ModifierType = ModifierType
        self.BonusValueGRU = BonusValueGRU
        self.BonusValue = BonusValue

    def __repr__(self):
        return f'<TUnitEffectIncreaseSpecializedDetectionDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['VisionType', 'ModifierType', 'BonusValueGRU', 'BonusValue']]) + '>'


class TUnitEffectIncreaseInfluenceValueMinDescriptor:
    def __init__(self, Bonus=None, ModifierType=None):
        self.Bonus = Bonus
        self.ModifierType = ModifierType

    def __repr__(self):
        return f'<TUnitEffectIncreaseInfluenceValueMinDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Bonus', 'ModifierType']]) + '>'


class TUnitEffectSetSelectableDescriptor:
    def __init__(self, Selectable=None):
        self.Selectable = Selectable

    def __repr__(self):
        return f'<TUnitEffectSetSelectableDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Selectable']]) + '>'


class TUnitEffectStopWithInertiaEffectDescriptor:
    def __init__(self, UpdateEachTick=None):
        self.UpdateEachTick = UpdateEachTick

    def __repr__(self):
        return f'<TUnitEffectStopWithInertiaEffectDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['UpdateEachTick']]) + '>'


class TDerouteUnitEffectDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TDerouteUnitEffectDescriptor>'


class TEffectInflictPhysicalDamageDescriptor:
    def __init__(self, ModifierType=None, PhysicalDamageValue=None):
        self.ModifierType = ModifierType
        self.PhysicalDamageValue = PhysicalDamageValue

    def __repr__(self):
        return f'<TEffectInflictPhysicalDamageDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ModifierType', 'PhysicalDamageValue']]) + '>'


class TUnitEffectIncreaseWeaponPrecisionArretDescriptor:
    def __init__(self, ModifierType=None, ModifierValue=None):
        self.ModifierType = ModifierType
        self.ModifierValue = ModifierValue

    def __repr__(self):
        return f'<TUnitEffectIncreaseWeaponPrecisionArretDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ModifierType', 'ModifierValue']]) + '>'


class TUnitEffectIncreaseWeaponPrecisionMouvementDescriptor:
    def __init__(self, ModifierType=None, ModifierValue=None):
        self.ModifierType = ModifierType
        self.ModifierValue = ModifierValue

    def __repr__(self):
        return f'<TUnitEffectIncreaseWeaponPrecisionMouvementDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ModifierType', 'ModifierValue']]) + '>'


class TUnitEffectRemoveUnitDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TUnitEffectRemoveUnitDescriptor>'


class TKillUnitEffectDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TKillUnitEffectDescriptor>'


class TEffectInflictSuppressDamageDescriptor:
    def __init__(self, ModifierType=None, SuppressDamageValue=None):
        self.ModifierType = ModifierType
        self.SuppressDamageValue = SuppressDamageValue

    def __repr__(self):
        return f'<TEffectInflictSuppressDamageDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ModifierType', 'SuppressDamageValue']]) + '>'


class TUnitEffectBonusPrecisionWhenTargetedDescriptor:
    def __init__(self, ModifierType=None, BonusPrecisionWhenTargeted=None):
        self.ModifierType = ModifierType
        self.BonusPrecisionWhenTargeted = BonusPrecisionWhenTargeted

    def __repr__(self):
        return f'<TUnitEffectBonusPrecisionWhenTargetedDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ModifierType', 'BonusPrecisionWhenTargeted']]) + '>'


class TUnitEffectIncreaseOpticalStrengthDescriptor:
    def __init__(self, ModifierType=None, BonusOpticalStrength=None):
        self.ModifierType = ModifierType
        self.BonusOpticalStrength = BonusOpticalStrength

    def __repr__(self):
        return f'<TUnitEffectIncreaseOpticalStrengthDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ModifierType', 'BonusOpticalStrength']]) + '>'


class TUnitEffectIncreaseWeaponPorteeMaxIgnoreSmokeDescriptor:
    def __init__(self, ModifierType=None, BonusWeaponPorteeMax=None):
        self.ModifierType = ModifierType
        self.BonusWeaponPorteeMax = BonusWeaponPorteeMax

    def __repr__(self):
        return f'<TUnitEffectIncreaseWeaponPorteeMaxIgnoreSmokeDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ModifierType', 'BonusWeaponPorteeMax']]) + '>'


class TUnitEffectReplaceArmorDescriptor:
    def __init__(self, BlindageLocation=None, ReplacementBlindage=None):
        self.BlindageLocation = BlindageLocation
        self.ReplacementBlindage = ReplacementBlindage

    def __repr__(self):
        return f'<TUnitEffectReplaceArmorDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['BlindageLocation', 'ReplacementBlindage']]) + '>'


class TUnitEffectIncreaseConcealmentBonusDescriptor:
    def __init__(self, ModifierType=None, BonusConcealmentBonus=None):
        self.ModifierType = ModifierType
        self.BonusConcealmentBonus = BonusConcealmentBonus

    def __repr__(self):
        return f'<TUnitEffectIncreaseConcealmentBonusDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ModifierType', 'BonusConcealmentBonus']]) + '>'


class TUnitEffectHealOverTimeDescriptor:
    def __init__(self, DamageType=None, HealUnitsPerSecond=None, NbUpdatePerSecond=None):
        self.DamageType = DamageType
        self.HealUnitsPerSecond = HealUnitsPerSecond
        self.NbUpdatePerSecond = NbUpdatePerSecond

    def __repr__(self):
        return f'<TUnitEffectHealOverTimeDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['DamageType', 'HealUnitsPerSecond', 'NbUpdatePerSecond']]) + '>'


class TUnitEffectChangeTeamDescriptor:
    def __init__(self, FutureTeam=None):
        self.FutureTeam = FutureTeam

    def __repr__(self):
        return f'<TUnitEffectChangeTeamDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['FutureTeam']]) + '>'


class TTeamIdentifierForUnitEffect:
    def __init__(self, TeamType=None, TeamNumber=None):
        self.TeamType = TeamType
        self.TeamNumber = TeamNumber

    def __repr__(self):
        return f'<TTeamIdentifierForUnitEffect ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TeamType', 'TeamNumber']]) + '>'


class TUnitEffectAddCapacityDescriptor:
    def __init__(self, CapacityToAdd=None):
        self.CapacityToAdd = CapacityToAdd

    def __repr__(self):
        return f'<TUnitEffectAddCapacityDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['CapacityToAdd']]) + '>'


class TEvacAirplaneEffectDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TEvacAirplaneEffectDescriptor>'


class TExperienceLevelsPackDescriptor:
    def __init__(self, NameForDebug=None, ExperienceLevelsDescriptors=None, DescriptorId=None):
        self.NameForDebug = NameForDebug
        self.ExperienceLevelsDescriptors = ExperienceLevelsDescriptors
        self.DescriptorId = DescriptorId

    def __repr__(self):
        return f'<TExperienceLevelsPackDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['NameForDebug', 'ExperienceLevelsDescriptors', 'DescriptorId']]) + '>'


class TExperienceLevelDescriptor:
    def __init__(self, ThresholdPriceMultiplier=None, HintTitleToken=None, IconsByNationality=None, ThresholdAdditionalValue=None, DescriptorId=None, HintBodyToken=None, LocalizationToken=None, NameForDebug=None, LevelEffectsPacks=None):
        self.ThresholdPriceMultiplier = ThresholdPriceMultiplier
        self.HintTitleToken = HintTitleToken
        self.IconsByNationality = IconsByNationality
        self.ThresholdAdditionalValue = ThresholdAdditionalValue
        self.DescriptorId = DescriptorId
        self.HintBodyToken = HintBodyToken
        self.LocalizationToken = LocalizationToken
        self.NameForDebug = NameForDebug
        self.LevelEffectsPacks = LevelEffectsPacks

    def __repr__(self):
        return f'<TExperienceLevelDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ThresholdPriceMultiplier', 'HintTitleToken', 'IconsByNationality', 'ThresholdAdditionalValue', 'DescriptorId', 'HintBodyToken', 'LocalizationToken', 'NameForDebug', 'LevelEffectsPacks']]) + '>'


class FXMissileFiring:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXMissileFiring ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FiringAndProjectile:
    def __init__(self, Happenings=None):
        self.Happenings = Happenings

    def __repr__(self):
        return f'<FiringAndProjectile ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Happenings']]) + '>'


class TRandomHappening:
    def __init__(self, Alternatives=None):
        self.Alternatives = Alternatives

    def __repr__(self):
        return f'<TRandomHappening ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Alternatives']]) + '>'


class FXFiring_0:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXFiring_0 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXProjectile_0:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXProjectile_0 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXFiring_1:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXFiring_1 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXProjectile_1:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXProjectile_1 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXFiring_2:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXFiring_2 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXProjectile_2:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXProjectile_2 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class TIntroduceMobileHappening:
    def __init__(self, Happening=None):
        self.Happening = Happening

    def __repr__(self):
        return f'<TIntroduceMobileHappening ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Happening']]) + '>'


class FXProjectile_3:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXProjectile_3 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXFiring_3:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXFiring_3 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXProjectile_4:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXProjectile_4 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXFiring_4:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXFiring_4 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXProjectile_5:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXProjectile_5 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXFiring_5:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXFiring_5 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXProjectile_6:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXProjectile_6 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXFiring_6:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXFiring_6 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXProjectile_7:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXProjectile_7 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXFiring_7:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXFiring_7 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXProjectile_8:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXProjectile_8 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXFiring_8:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXFiring_8 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXProjectile_9:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXProjectile_9 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXFiring_9:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXFiring_9 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXProjectile_10:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXProjectile_10 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXProjectile_11:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXProjectile_11 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXProjectile_12:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXProjectile_12 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXProjectile_13:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXProjectile_13 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXFiring_12:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXFiring_12 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXProjectile_14:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXProjectile_14 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXFiring_13:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXFiring_13 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXProjectile_15:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXProjectile_15 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXFiring_14:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXFiring_14 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXProjectile_16:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXProjectile_16 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXFiring_15:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXFiring_15 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXProjectile_17:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXProjectile_17 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXFiring_10:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXFiring_10 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXProjectile_18:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXProjectile_18 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXFiring_16:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXFiring_16 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXProjectile_19:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXProjectile_19 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXFiring_11:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXFiring_11 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXFiring_17:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXFiring_17 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXProjectile_20:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXProjectile_20 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXFiring_18:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXFiring_18 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXProjectile_21:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXProjectile_21 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXFiring_19:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXFiring_19 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXProjectile_22:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXProjectile_22 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXFiring_20:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXFiring_20 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXProjectile_23:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXProjectile_23 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXFiring_21:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXFiring_21 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class FXProjectile_24:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<FXProjectile_24 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class TCompositeHappening:
    def __init__(self, SubHappenings=None):
        self.SubHappenings = SubHappenings

    def __repr__(self):
        return f'<TCompositeHappening ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['SubHappenings']]) + '>'


class ImpactWrapper:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<ImpactWrapper ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class TImpactHappening:
    def __init__(self, Happenings=None):
        self.Happenings = Happenings

    def __repr__(self):
        return f'<TImpactHappening ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Happenings']]) + '>'


class TMissileCarriageConnoisseur:
    def __init__(self, PylonSet=None, WeaponInfos=None, MeshDescriptor=None):
        self.PylonSet = PylonSet
        self.WeaponInfos = WeaponInfos
        self.MeshDescriptor = MeshDescriptor

    def __repr__(self):
        return f'<TMissileCarriageConnoisseur ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['PylonSet', 'WeaponInfos', 'MeshDescriptor']]) + '>'


class TMissileCarriageWeaponInfo:
    def __init__(self, MountingType=None, MeshDescriptor=None, WeaponIndex=None, MissileType=None, Count=None):
        self.MountingType = MountingType
        self.MeshDescriptor = MeshDescriptor
        self.WeaponIndex = WeaponIndex
        self.MissileType = MissileType
        self.Count = Count

    def __repr__(self):
        return f'<TMissileCarriageWeaponInfo ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MountingType', 'MeshDescriptor', 'WeaponIndex', 'MissileType', 'Count']]) + '>'


class TMissileCarriageSubDepictionGenerator:
    def __init__(self, Missiles=None, MissileCarriageConnoisseur=None, ReferenceMesh=None, Pylons=None):
        self.Missiles = Missiles
        self.MissileCarriageConnoisseur = MissileCarriageConnoisseur
        self.ReferenceMesh = ReferenceMesh
        self.Pylons = Pylons

    def __repr__(self):
        return f'<TMissileCarriageSubDepictionGenerator ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Missiles', 'MissileCarriageConnoisseur', 'ReferenceMesh', 'Pylons']]) + '>'


class TMissileCarriageSubDepictionMissileInfo:
    def __init__(self, MissileIndex=None, Depiction=None, WeaponIndex=None):
        self.MissileIndex = MissileIndex
        self.Depiction = Depiction
        self.WeaponIndex = WeaponIndex

    def __repr__(self):
        return f'<TMissileCarriageSubDepictionMissileInfo ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MissileIndex', 'Depiction', 'WeaponIndex']]) + '>'


class TemplateDepictionMissileGroundUnit:
    def __init__(self, ProjectileModelResource=None, MissileNumber=None, PhysicalProperty=None):
        self.ProjectileModelResource = ProjectileModelResource
        self.MissileNumber = MissileNumber
        self.PhysicalProperty = PhysicalProperty

    def __repr__(self):
        return f'<TemplateDepictionMissileGroundUnit ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ProjectileModelResource', 'MissileNumber', 'PhysicalProperty']]) + '>'


class TStaticMissileCarriageSubDepictionGenerator:
    def __init__(self, Missiles=None, MissileCarriageConnoisseur=None, ReferenceMesh=None, Pylons=None):
        self.Missiles = Missiles
        self.MissileCarriageConnoisseur = MissileCarriageConnoisseur
        self.ReferenceMesh = ReferenceMesh
        self.Pylons = Pylons

    def __repr__(self):
        return f'<TStaticMissileCarriageSubDepictionGenerator ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Missiles', 'MissileCarriageConnoisseur', 'ReferenceMesh', 'Pylons']]) + '>'


class TStaticMissileCarriageSubDepictionMissileInfo:
    def __init__(self, Depiction=None, MissileCount=None, WeaponIndex=None):
        self.Depiction = Depiction
        self.MissileCount = MissileCount
        self.WeaponIndex = WeaponIndex

    def __repr__(self):
        return f'<TStaticMissileCarriageSubDepictionMissileInfo ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Depiction', 'MissileCount', 'WeaponIndex']]) + '>'


class TemplateDepictionMissileShowroom:
    def __init__(self, ProjectileModelResource=None):
        self.ProjectileModelResource = ProjectileModelResource

    def __repr__(self):
        return f'<TemplateDepictionMissileShowroom ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ProjectileModelResource']]) + '>'


class TDepictionDescriptor:
    def __init__(self, MeshDescriptor=None, SelectorId=None):
        self.MeshDescriptor = MeshDescriptor
        self.SelectorId = SelectorId

    def __repr__(self):
        return f'<TDepictionDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MeshDescriptor', 'SelectorId']]) + '>'


class TemplateDepictionStaticMissilesGroundUnit:
    def __init__(self, ProjectileModelResource=None, PhysicalProperty=None):
        self.ProjectileModelResource = ProjectileModelResource
        self.PhysicalProperty = PhysicalProperty

    def __repr__(self):
        return f'<TemplateDepictionStaticMissilesGroundUnit ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ProjectileModelResource', 'PhysicalProperty']]) + '>'


class TemplateDepictionStaticMissilesAirUnit:
    def __init__(self, ProjectileModelResource=None, PhysicalProperty=None):
        self.ProjectileModelResource = ProjectileModelResource
        self.PhysicalProperty = PhysicalProperty

    def __repr__(self):
        return f'<TemplateDepictionStaticMissilesAirUnit ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ProjectileModelResource', 'PhysicalProperty']]) + '>'


class Template_DescriptorMissileBase:
    def __init__(self, ProjectileModelResource=None, Actions=None):
        self.ProjectileModelResource = ProjectileModelResource
        self.Actions = Actions

    def __repr__(self):
        return f'<Template_DescriptorMissileBase ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ProjectileModelResource', 'Actions']]) + '>'


class template_PropulsionActionHappening:
    def __init__(self, Action=None):
        self.Action = Action

    def __repr__(self):
        return f'<template_PropulsionActionHappening ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Action']]) + '>'


class TGuidedMissileModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TGuidedMissileModuleDescriptor>'


class TGuidedMissileMovementModuleDescriptor:
    def __init__(self, UncontrollableConfig=None, RangeChaos=None, TerminalPhaseConfig=None, AngleMaxForRandomMouvUncontrollable=None, RotationSpeedWhenUncontrollable=None, TimeBetweenChaosUpdates=None, AscendantPhaseConfig=None, DefaultConfig=None, TimeMinBetweenRandomMoveWhenUncontrollable=None, TimeMaxBetweenRandomMoveWhenUncontrollable=None, CruiseAltitudeGRU=None):
        self.UncontrollableConfig = UncontrollableConfig
        self.RangeChaos = RangeChaos
        self.TerminalPhaseConfig = TerminalPhaseConfig
        self.AngleMaxForRandomMouvUncontrollable = AngleMaxForRandomMouvUncontrollable
        self.RotationSpeedWhenUncontrollable = RotationSpeedWhenUncontrollable
        self.TimeBetweenChaosUpdates = TimeBetweenChaosUpdates
        self.AscendantPhaseConfig = AscendantPhaseConfig
        self.DefaultConfig = DefaultConfig
        self.TimeMinBetweenRandomMoveWhenUncontrollable = TimeMinBetweenRandomMoveWhenUncontrollable
        self.TimeMaxBetweenRandomMoveWhenUncontrollable = TimeMaxBetweenRandomMoveWhenUncontrollable
        self.CruiseAltitudeGRU = CruiseAltitudeGRU

    def __repr__(self):
        return f'<TGuidedMissileMovementModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['UncontrollableConfig', 'RangeChaos', 'TerminalPhaseConfig', 'AngleMaxForRandomMouvUncontrollable', 'RotationSpeedWhenUncontrollable', 'TimeBetweenChaosUpdates', 'AscendantPhaseConfig', 'DefaultConfig', 'TimeMinBetweenRandomMoveWhenUncontrollable', 'TimeMaxBetweenRandomMoveWhenUncontrollable', 'CruiseAltitudeGRU']]) + '>'


class TGuidedMissileMovementConfigDescriptor:
    def __init__(self, MaxSpeedGRU=None, MaxAccelerationGRU=None, AutoGyr=None):
        self.MaxSpeedGRU = MaxSpeedGRU
        self.MaxAccelerationGRU = MaxAccelerationGRU
        self.AutoGyr = AutoGyr

    def __repr__(self):
        return f'<TGuidedMissileMovementConfigDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MaxSpeedGRU', 'MaxAccelerationGRU', 'AutoGyr']]) + '>'


class TDangerousnessModuleDescriptor:
    def __init__(self, Dangerousness=None):
        self.Dangerousness = Dangerousness

    def __repr__(self):
        return f'<TDangerousnessModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Dangerousness']]) + '>'


class TShowRoomEquivalenceManager:
    def __init__(self, UnitToShowRoomEquivalent=None):
        self.UnitToShowRoomEquivalent = UnitToShowRoomEquivalent

    def __repr__(self):
        return f'<TShowRoomEquivalenceManager ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['UnitToShowRoomEquivalent']]) + '>'


class TInfantrySquadModuleDescriptor:
    def __init__(self, SquadDataDescriptor=None, NbSoldatInGroupeCombat=None, InfantryMimeticName=None, MimeticDescriptor=None, WeaponUnitFXKey=None):
        self.SquadDataDescriptor = SquadDataDescriptor
        self.NbSoldatInGroupeCombat = NbSoldatInGroupeCombat
        self.InfantryMimeticName = InfantryMimeticName
        self.MimeticDescriptor = MimeticDescriptor
        self.WeaponUnitFXKey = WeaponUnitFXKey

    def __repr__(self):
        return f'<TInfantrySquadModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['SquadDataDescriptor', 'NbSoldatInGroupeCombat', 'InfantryMimeticName', 'MimeticDescriptor', 'WeaponUnitFXKey']]) + '>'


class Descriptor_Unit_MimeticUnit:
    def __init__(self, MimeticName=None, DescriptorId=None):
        self.MimeticName = MimeticName
        self.DescriptorId = DescriptorId

    def __repr__(self):
        return f'<Descriptor_Unit_MimeticUnit ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MimeticName', 'DescriptorId']]) + '>'


class TInfantrySquadWeaponAssignmentModuleDescriptor:
    def __init__(self, InitialSoldiersToTurretIndexMap=None):
        self.InitialSoldiersToTurretIndexMap = InitialSoldiersToTurretIndexMap

    def __repr__(self):
        return f'<TInfantrySquadWeaponAssignmentModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['InitialSoldiersToTurretIndexMap']]) + '>'


class UnitCadavreModuleDescriptor:
    def __init__(self, DeathExplosionAmmo=None, KillAsAirplane=None, ModuleDescriptorsToSteal=None, KillAsVehicule=None, KillAsHelico=None, CadavreDuration=None, KillAsInfanterie=None):
        self.DeathExplosionAmmo = DeathExplosionAmmo
        self.KillAsAirplane = KillAsAirplane
        self.ModuleDescriptorsToSteal = ModuleDescriptorsToSteal
        self.KillAsVehicule = KillAsVehicule
        self.KillAsHelico = KillAsHelico
        self.CadavreDuration = CadavreDuration
        self.KillAsInfanterie = KillAsInfanterie

    def __repr__(self):
        return f'<UnitCadavreModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['DeathExplosionAmmo', 'KillAsAirplane', 'ModuleDescriptorsToSteal', 'KillAsVehicule', 'KillAsHelico', 'CadavreDuration', 'KillAsInfanterie']]) + '>'


class HelicopterCadavrePositionModuleDescriptor:
    def __init__(self, NearGroundFlyingAltitudeGRU=None, LowAltitudeFlyingAltitudeGRU=None):
        self.NearGroundFlyingAltitudeGRU = NearGroundFlyingAltitudeGRU
        self.LowAltitudeFlyingAltitudeGRU = LowAltitudeFlyingAltitudeGRU

    def __repr__(self):
        return f'<HelicopterCadavrePositionModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['NearGroundFlyingAltitudeGRU', 'LowAltitudeFlyingAltitudeGRU']]) + '>'


class AirplaneCadavrePositionModuleDescriptor:
    def __init__(self, LowAltitudeFlyingAltitudeGRU=None):
        self.LowAltitudeFlyingAltitudeGRU = LowAltitudeFlyingAltitudeGRU

    def __repr__(self):
        return f'<AirplaneCadavrePositionModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['LowAltitudeFlyingAltitudeGRU']]) + '>'


class TemplateUnitCriticalModule:
    def __init__(self, Module=None):
        self.Module = Module

    def __repr__(self):
        return f'<TemplateUnitCriticalModule ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Module']]) + '>'


class VehicleApparenceModelModuleDescriptor:
    def __init__(self, BlackHoleIdentifier=None, Depiction=None, ReferenceMesh=None, GameplayBBoxBoneName=None):
        self.BlackHoleIdentifier = BlackHoleIdentifier
        self.Depiction = Depiction
        self.ReferenceMesh = ReferenceMesh
        self.GameplayBBoxBoneName = GameplayBBoxBoneName

    def __repr__(self):
        return f'<VehicleApparenceModelModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['BlackHoleIdentifier', 'Depiction', 'ReferenceMesh', 'GameplayBBoxBoneName']]) + '>'


class TAutoCoverModuleDescriptor:
    def __init__(self, AutoCoverRangeGRU=None, OccupationRadiusGRU=None, TerrainList=None, TerrainListMask=None, UseTerrainsForEscape=None):
        self.AutoCoverRangeGRU = AutoCoverRangeGRU
        self.OccupationRadiusGRU = OccupationRadiusGRU
        self.TerrainList = TerrainList
        self.TerrainListMask = TerrainListMask
        self.UseTerrainsForEscape = UseTerrainsForEscape

    def __repr__(self):
        return f'<TAutoCoverModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['AutoCoverRangeGRU', 'OccupationRadiusGRU', 'TerrainList', 'TerrainListMask', 'UseTerrainsForEscape']]) + '>'


class TRoutModuleDescriptor:
    def __init__(self, MoralLevel=None):
        self.MoralLevel = MoralLevel

    def __repr__(self):
        return f'<TRoutModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MoralLevel']]) + '>'


class TGenericMovementModuleDescriptor:
    def __init__(self, MaxSpeedInKmph=None, PathfindType=None):
        self.MaxSpeedInKmph = MaxSpeedInKmph
        self.PathfindType = PathfindType

    def __repr__(self):
        return f'<TGenericMovementModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MaxSpeedInKmph', 'PathfindType']]) + '>'


class TLandMovementModuleDescriptor:
    def __init__(self, StartTime=None, VehicleSizeInMeter=None, TempsDemiTour=None, UnitMovingType=None, SpeedBonusFactorOnRoad=None, MaxAccelerationGRU=None, MaxDecelerationGRU=None, RotationStopTime=None, StopTime=None, RotationStartTime=None):
        self.StartTime = StartTime
        self.VehicleSizeInMeter = VehicleSizeInMeter
        self.TempsDemiTour = TempsDemiTour
        self.UnitMovingType = UnitMovingType
        self.SpeedBonusFactorOnRoad = SpeedBonusFactorOnRoad
        self.MaxAccelerationGRU = MaxAccelerationGRU
        self.MaxDecelerationGRU = MaxDecelerationGRU
        self.RotationStopTime = RotationStopTime
        self.StopTime = StopTime
        self.RotationStartTime = RotationStartTime

    def __repr__(self):
        return f'<TLandMovementModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['StartTime', 'VehicleSizeInMeter', 'TempsDemiTour', 'UnitMovingType', 'SpeedBonusFactorOnRoad', 'MaxAccelerationGRU', 'MaxDecelerationGRU', 'RotationStopTime', 'StopTime', 'RotationStartTime']]) + '>'


class TFuelModuleDescriptor:
    def __init__(self, FuelCapacity=None, FuelMoveDuration=None):
        self.FuelCapacity = FuelCapacity
        self.FuelMoveDuration = FuelMoveDuration

    def __repr__(self):
        return f'<TFuelModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['FuelCapacity', 'FuelMoveDuration']]) + '>'


class TemplateUnitMissileCarriage:
    def __init__(self, Connoisseur=None):
        self.Connoisseur = Connoisseur

    def __repr__(self):
        return f'<TemplateUnitMissileCarriage ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Connoisseur']]) + '>'


class TAutomaticBehaviorModuleDescriptor:
    def __init__(self, MaxDistanceForOffensiveReactionGRU=None, MaxDistanceForEngagementGRU=None, SearchedTagsInEngagementTarget=None, CanAssist=None, DistanceToFleeGRU=None, AssistRequestBroadcastRadiusGRU=None):
        self.MaxDistanceForOffensiveReactionGRU = MaxDistanceForOffensiveReactionGRU
        self.MaxDistanceForEngagementGRU = MaxDistanceForEngagementGRU
        self.SearchedTagsInEngagementTarget = SearchedTagsInEngagementTarget
        self.CanAssist = CanAssist
        self.DistanceToFleeGRU = DistanceToFleeGRU
        self.AssistRequestBroadcastRadiusGRU = AssistRequestBroadcastRadiusGRU

    def __repr__(self):
        return f'<TAutomaticBehaviorModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MaxDistanceForOffensiveReactionGRU', 'MaxDistanceForEngagementGRU', 'SearchedTagsInEngagementTarget', 'CanAssist', 'DistanceToFleeGRU', 'AssistRequestBroadcastRadiusGRU']]) + '>'


class TCubeActionModuleDescriptor:
    def __init__(self, CubeActionDescriptor=None):
        self.CubeActionDescriptor = CubeActionDescriptor

    def __repr__(self):
        return f'<TCubeActionModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['CubeActionDescriptor']]) + '>'


class TOrderConfigModuleDescriptor:
    def __init__(self, ValidOrders=None):
        self.ValidOrders = ValidOrders

    def __repr__(self):
        return f'<TOrderConfigModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ValidOrders']]) + '>'


class TStrategicDataModuleDescriptor:
    def __init__(self, UnitAttackValue=None, UnitBonusXpPerLevelValue=None, UnitDefenseValue=None):
        self.UnitAttackValue = UnitAttackValue
        self.UnitBonusXpPerLevelValue = UnitBonusXpPerLevelValue
        self.UnitDefenseValue = UnitDefenseValue

    def __repr__(self):
        return f'<TStrategicDataModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['UnitAttackValue', 'UnitBonusXpPerLevelValue', 'UnitDefenseValue']]) + '>'


class TVisualShootPositionsModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TVisualShootPositionsModuleDescriptor>'


class TTransportableModuleDescriptor:
    def __init__(self, TransportedSoldier=None, TimeToLoad=None, IsTowable=None, NbSeatsOccupied=None, TransportedTexture=None):
        self.TransportedSoldier = TransportedSoldier
        self.TimeToLoad = TimeToLoad
        self.IsTowable = IsTowable
        self.NbSeatsOccupied = NbSeatsOccupied
        self.TransportedTexture = TransportedTexture

    def __repr__(self):
        return f'<TTransportableModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TransportedSoldier', 'TimeToLoad', 'IsTowable', 'NbSeatsOccupied', 'TransportedTexture']]) + '>'


class TCapaciteModuleDescriptor:
    def __init__(self, DefaultSkillList=None):
        self.DefaultSkillList = DefaultSkillList

    def __repr__(self):
        return f'<TCapaciteModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['DefaultSkillList']]) + '>'


class TDeploymentShiftModuleDescriptor:
    def __init__(self, DeploymentShiftGRU=None):
        self.DeploymentShiftGRU = DeploymentShiftGRU

    def __repr__(self):
        return f'<TDeploymentShiftModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['DeploymentShiftGRU']]) + '>'


class TTransporterModuleDescriptor:
    def __init__(self, WreckUnloadSuppressDamageBonus=None, LoadRadiusGRU=None, TransportableTagSet=None, NbSeatsAvailable=None, WreckUnloadPhysicalDamageBonus=None, WreckUnloadStunDamageBonus=None):
        self.WreckUnloadSuppressDamageBonus = WreckUnloadSuppressDamageBonus
        self.LoadRadiusGRU = LoadRadiusGRU
        self.TransportableTagSet = TransportableTagSet
        self.NbSeatsAvailable = NbSeatsAvailable
        self.WreckUnloadPhysicalDamageBonus = WreckUnloadPhysicalDamageBonus
        self.WreckUnloadStunDamageBonus = WreckUnloadStunDamageBonus

    def __repr__(self):
        return f'<TTransporterModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['WreckUnloadSuppressDamageBonus', 'LoadRadiusGRU', 'TransportableTagSet', 'NbSeatsAvailable', 'WreckUnloadPhysicalDamageBonus', 'WreckUnloadStunDamageBonus']]) + '>'


class TCommanderModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TCommanderModuleDescriptor>'


class TZoneInfluenceMapModuleDescriptor:
    def __init__(self, InfluenceStrength=None, IsEnabledByComportementAuto=None, StrengthDecayPerSecond=None, MinimumInfluenceStrength=None, PreventsDecayInZone=None):
        self.InfluenceStrength = InfluenceStrength
        self.IsEnabledByComportementAuto = IsEnabledByComportementAuto
        self.StrengthDecayPerSecond = StrengthDecayPerSecond
        self.MinimumInfluenceStrength = MinimumInfluenceStrength
        self.PreventsDecayInZone = PreventsDecayInZone

    def __repr__(self):
        return f'<TZoneInfluenceMapModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['InfluenceStrength', 'IsEnabledByComportementAuto', 'StrengthDecayPerSecond', 'MinimumInfluenceStrength', 'PreventsDecayInZone']]) + '>'


class TInfluenceScoutModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TInfluenceScoutModuleDescriptor>'


class InfantryApparenceModelModuleDescriptor:
    def __init__(self, Depiction=None):
        self.Depiction = Depiction

    def __repr__(self):
        return f'<InfantryApparenceModelModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Depiction']]) + '>'


class TLinkToDistrictModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TLinkToDistrictModuleDescriptor>'


class TSellModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TSellModuleDescriptor>'


class HelicopterPositionModuleDescriptor:
    def __init__(self, NearGroundFlyingAltitudeGRU=None, LowAltitudeFlyingAltitudeGRU=None):
        self.NearGroundFlyingAltitudeGRU = NearGroundFlyingAltitudeGRU
        self.LowAltitudeFlyingAltitudeGRU = LowAltitudeFlyingAltitudeGRU

    def __repr__(self):
        return f'<HelicopterPositionModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['NearGroundFlyingAltitudeGRU', 'LowAltitudeFlyingAltitudeGRU']]) + '>'


class THelicopterMovementModuleDescriptor:
    def __init__(self, TorqueManoeuvrability=None, UpwardSpeedInKmph=None, MaxInclination=None, Mass=None, CyclicManoeuvrability=None, WorldFloorProxy=None, RotorArea=None, GFactorLimit=None, MaxSpeedInKmph=None):
        self.TorqueManoeuvrability = TorqueManoeuvrability
        self.UpwardSpeedInKmph = UpwardSpeedInKmph
        self.MaxInclination = MaxInclination
        self.Mass = Mass
        self.CyclicManoeuvrability = CyclicManoeuvrability
        self.WorldFloorProxy = WorldFloorProxy
        self.RotorArea = RotorArea
        self.GFactorLimit = GFactorLimit
        self.MaxSpeedInKmph = MaxSpeedInKmph

    def __repr__(self):
        return f'<THelicopterMovementModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TorqueManoeuvrability', 'UpwardSpeedInKmph', 'MaxInclination', 'Mass', 'CyclicManoeuvrability', 'WorldFloorProxy', 'RotorArea', 'GFactorLimit', 'MaxSpeedInKmph']]) + '>'


class TFlareModuleDescriptor_MW:
    def __init__(self, DistanceActivationGRU=None, TimeBetweenFlare=None, MinimalTimeBetweenFlare=None, ProjectileSpeed=None, BonusTimeBetweenFlareByProjectile=None):
        self.DistanceActivationGRU = DistanceActivationGRU
        self.TimeBetweenFlare = TimeBetweenFlare
        self.MinimalTimeBetweenFlare = MinimalTimeBetweenFlare
        self.ProjectileSpeed = ProjectileSpeed
        self.BonusTimeBetweenFlareByProjectile = BonusTimeBetweenFlareByProjectile

    def __repr__(self):
        return f'<TFlareModuleDescriptor_MW ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['DistanceActivationGRU', 'TimeBetweenFlare', 'MinimalTimeBetweenFlare', 'ProjectileSpeed', 'BonusTimeBetweenFlareByProjectile']]) + '>'


class AirplanePositionModuleDescriptor:
    def __init__(self, LowAltitudeFlyingAltitudeGRU=None):
        self.LowAltitudeFlyingAltitudeGRU = LowAltitudeFlyingAltitudeGRU

    def __repr__(self):
        return f'<AirplanePositionModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['LowAltitudeFlyingAltitudeGRU']]) + '>'


class AirplaneMovementDescriptor:
    def __init__(self, AltitudeGRU=None, AgilityRadiusGRU=None, EvacToStartingPoint=None, OrderedAttackStrategies=None, RollAngle=None, RollSpeed=None, SpeedInKmph=None, AltitudeMinGRU=None, PitchAngle=None, EvacAngle=None):
        self.AltitudeGRU = AltitudeGRU
        self.AgilityRadiusGRU = AgilityRadiusGRU
        self.EvacToStartingPoint = EvacToStartingPoint
        self.OrderedAttackStrategies = OrderedAttackStrategies
        self.RollAngle = RollAngle
        self.RollSpeed = RollSpeed
        self.SpeedInKmph = SpeedInKmph
        self.AltitudeMinGRU = AltitudeMinGRU
        self.PitchAngle = PitchAngle
        self.EvacAngle = EvacAngle

    def __repr__(self):
        return f'<AirplaneMovementDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['AltitudeGRU', 'AgilityRadiusGRU', 'EvacToStartingPoint', 'OrderedAttackStrategies', 'RollAngle', 'RollSpeed', 'SpeedInKmph', 'AltitudeMinGRU', 'PitchAngle', 'EvacAngle']]) + '>'


class TAirplaneModuleDescriptor:
    def __init__(self, TravelDuration=None, EvacuationTime=None):
        self.TravelDuration = TravelDuration
        self.EvacuationTime = EvacuationTime

    def __repr__(self):
        return f'<TAirplaneModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TravelDuration', 'EvacuationTime']]) + '>'


class TWeaponManagerModuleDescriptor:
    def __init__(self, Salves=None, AlwaysOrientArmorTowardsThreat=None, TurretDescriptorList=None, SalvoIsMainSalvo=None):
        self.Salves = Salves
        self.AlwaysOrientArmorTowardsThreat = AlwaysOrientArmorTowardsThreat
        self.TurretDescriptorList = TurretDescriptorList
        self.SalvoIsMainSalvo = SalvoIsMainSalvo

    def __repr__(self):
        return f'<TWeaponManagerModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Salves', 'AlwaysOrientArmorTowardsThreat', 'TurretDescriptorList', 'SalvoIsMainSalvo']]) + '>'


class TTurretTwoAxisDescriptor:
    def __init__(self, MountedWeaponDescriptorList=None, OutOfRangeTrackingDuration=None, AngleRotationBasePitch=None, AngleRotationBase=None, AngleRotationMinPitch=None, YulBoneOrdinal=None, AimingPriority=None, AngleRotationMax=None, MasterTurretYulBoneOrdinal=None, TurretIdleBehaviourDescriptor=None, AngleRotationMaxPitch=None, Tag=None, VitesseRotation=None):
        self.MountedWeaponDescriptorList = MountedWeaponDescriptorList
        self.OutOfRangeTrackingDuration = OutOfRangeTrackingDuration
        self.AngleRotationBasePitch = AngleRotationBasePitch
        self.AngleRotationBase = AngleRotationBase
        self.AngleRotationMinPitch = AngleRotationMinPitch
        self.YulBoneOrdinal = YulBoneOrdinal
        self.AimingPriority = AimingPriority
        self.AngleRotationMax = AngleRotationMax
        self.MasterTurretYulBoneOrdinal = MasterTurretYulBoneOrdinal
        self.TurretIdleBehaviourDescriptor = TurretIdleBehaviourDescriptor
        self.AngleRotationMaxPitch = AngleRotationMaxPitch
        self.Tag = Tag
        self.VitesseRotation = VitesseRotation

    def __repr__(self):
        return f'<TTurretTwoAxisDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MountedWeaponDescriptorList', 'OutOfRangeTrackingDuration', 'AngleRotationBasePitch', 'AngleRotationBase', 'AngleRotationMinPitch', 'YulBoneOrdinal', 'AimingPriority', 'AngleRotationMax', 'MasterTurretYulBoneOrdinal', 'TurretIdleBehaviourDescriptor', 'AngleRotationMaxPitch', 'Tag', 'VitesseRotation']]) + '>'


class TMountedWeaponDescriptor:
    def __init__(self, SalvoStockIndex=None, DispersionRadiusOffThickness=None, AmmoConsumption_ForInterface=None, ShowInInterface=None, EffectTag=None, WeaponActiveAndCanShootPropertyName=None, DispersionRadiusOffColor=None, AnimateOnlyOneSoldier=None, DispersionRadiusOnThickness=None, HandheldEquipmentKey=None, Ammunition=None, WeaponIgnoredPropertyName=None, DispersionRadiusOnColor=None, TirContinu=None, WeaponShootDataPropertyName=None, NbWeapons=None, ShowDispersion=None):
        self.SalvoStockIndex = SalvoStockIndex
        self.DispersionRadiusOffThickness = DispersionRadiusOffThickness
        self.AmmoConsumption_ForInterface = AmmoConsumption_ForInterface
        self.ShowInInterface = ShowInInterface
        self.EffectTag = EffectTag
        self.WeaponActiveAndCanShootPropertyName = WeaponActiveAndCanShootPropertyName
        self.DispersionRadiusOffColor = DispersionRadiusOffColor
        self.AnimateOnlyOneSoldier = AnimateOnlyOneSoldier
        self.DispersionRadiusOnThickness = DispersionRadiusOnThickness
        self.HandheldEquipmentKey = HandheldEquipmentKey
        self.Ammunition = Ammunition
        self.WeaponIgnoredPropertyName = WeaponIgnoredPropertyName
        self.DispersionRadiusOnColor = DispersionRadiusOnColor
        self.TirContinu = TirContinu
        self.WeaponShootDataPropertyName = WeaponShootDataPropertyName
        self.NbWeapons = NbWeapons
        self.ShowDispersion = ShowDispersion

    def __repr__(self):
        return f'<TMountedWeaponDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['SalvoStockIndex', 'DispersionRadiusOffThickness', 'AmmoConsumption_ForInterface', 'ShowInInterface', 'EffectTag', 'WeaponActiveAndCanShootPropertyName', 'DispersionRadiusOffColor', 'AnimateOnlyOneSoldier', 'DispersionRadiusOnThickness', 'HandheldEquipmentKey', 'Ammunition', 'WeaponIgnoredPropertyName', 'DispersionRadiusOnColor', 'TirContinu', 'WeaponShootDataPropertyName', 'NbWeapons', 'ShowDispersion']]) + '>'


class TTurretUnitDescriptor:
    def __init__(self, MountedWeaponDescriptorList=None, AngleRotationMinPitch=None, YulBoneOrdinal=None, AimingPriority=None, Tag=None, AngleRotationMaxPitch=None, AngleRotationMax=None):
        self.MountedWeaponDescriptorList = MountedWeaponDescriptorList
        self.AngleRotationMinPitch = AngleRotationMinPitch
        self.YulBoneOrdinal = YulBoneOrdinal
        self.AimingPriority = AimingPriority
        self.Tag = Tag
        self.AngleRotationMaxPitch = AngleRotationMaxPitch
        self.AngleRotationMax = AngleRotationMax

    def __repr__(self):
        return f'<TTurretUnitDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MountedWeaponDescriptorList', 'AngleRotationMinPitch', 'YulBoneOrdinal', 'AimingPriority', 'Tag', 'AngleRotationMaxPitch', 'AngleRotationMax']]) + '>'


class TTurretInfanterieDescriptor:
    def __init__(self, MountedWeaponDescriptorList=None, YulBoneOrdinal=None):
        self.MountedWeaponDescriptorList = MountedWeaponDescriptorList
        self.YulBoneOrdinal = YulBoneOrdinal

    def __repr__(self):
        return f'<TTurretInfanterieDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MountedWeaponDescriptorList', 'YulBoneOrdinal']]) + '>'


class TTurretBombardierDescriptor:
    def __init__(self, MountedWeaponDescriptorList=None, YulBoneOrdinal=None, FlyingSpeedInKmph=None, Tag=None, FlyingAltitudeGRU=None):
        self.MountedWeaponDescriptorList = MountedWeaponDescriptorList
        self.YulBoneOrdinal = YulBoneOrdinal
        self.FlyingSpeedInKmph = FlyingSpeedInKmph
        self.Tag = Tag
        self.FlyingAltitudeGRU = FlyingAltitudeGRU

    def __repr__(self):
        return f'<TTurretBombardierDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MountedWeaponDescriptorList', 'YulBoneOrdinal', 'FlyingSpeedInKmph', 'Tag', 'FlyingAltitudeGRU']]) + '>'


class StrategicAirplanePawnDepictionTemplate:
    def __init__(self, MeshDescriptorPawn=None, MeshSocle=None):
        self.MeshDescriptorPawn = MeshDescriptorPawn
        self.MeshSocle = MeshSocle

    def __repr__(self):
        return f'<StrategicAirplanePawnDepictionTemplate ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MeshDescriptorPawn', 'MeshSocle']]) + '>'


class GhostAerialDepictionTemplate:
    def __init__(self, Selector=None, Alternatives=None):
        self.Selector = Selector
        self.Alternatives = Alternatives

    def __repr__(self):
        return f'<GhostAerialDepictionTemplate ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Selector', 'Alternatives']]) + '>'


class TacticAerialDepictionTemplate:
    def __init__(self, AdditionalTextures=None, Selector=None, CoatingName=None, Alternatives=None, Operators=None, Actions=None, PaleLength=None, PaleCount=None, RotationAxis=None, SousMobile=None):
        self.AdditionalTextures = AdditionalTextures
        self.Selector = Selector
        self.CoatingName = CoatingName
        self.Alternatives = Alternatives
        self.Operators = Operators
        self.Actions = Actions
        self.PaleLength = PaleLength
        self.PaleCount = PaleCount
        self.RotationAxis = RotationAxis
        self.SousMobile = SousMobile

    def __repr__(self):
        return f'<TacticAerialDepictionTemplate ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['AdditionalTextures', 'Selector', 'CoatingName', 'Alternatives', 'Operators', 'Actions', 'PaleLength', 'PaleCount', 'RotationAxis', 'SousMobile']]) + '>'


class DepictionOperator_Rotors:
    def __init__(self, HelixList=None):
        self.HelixList = HelixList

    def __repr__(self):
        return f'<DepictionOperator_Rotors ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['HelixList']]) + '>'


class THelix:
    def __init__(self, BladesBoneName=None, HelixBoneName=None, RotationSpeed=None, Clockwise=None, RotationAxis=None, BlurActionId=None, BladeCount=None):
        self.BladesBoneName = BladesBoneName
        self.HelixBoneName = HelixBoneName
        self.RotationSpeed = RotationSpeed
        self.Clockwise = Clockwise
        self.RotationAxis = RotationAxis
        self.BlurActionId = BlurActionId
        self.BladeCount = BladeCount

    def __repr__(self):
        return f'<THelix ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['BladesBoneName', 'HelixBoneName', 'RotationSpeed', 'Clockwise', 'RotationAxis', 'BlurActionId', 'BladeCount']]) + '>'


class ShowroomAerialDepictionTemplate:
    def __init__(self, MeshDescriptor=None, BoneName=None, RotationAxis=None, RotationInDegree=None):
        self.MeshDescriptor = MeshDescriptor
        self.BoneName = BoneName
        self.RotationAxis = RotationAxis
        self.RotationInDegree = RotationInDegree

    def __repr__(self):
        return f'<ShowroomAerialDepictionTemplate ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MeshDescriptor', 'BoneName', 'RotationAxis', 'RotationInDegree']]) + '>'


class GhostVehicleDepictionTemplate:
    def __init__(self, Selector=None, Alternatives=None):
        self.Selector = Selector
        self.Alternatives = Alternatives

    def __repr__(self):
        return f'<GhostVehicleDepictionTemplate ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Selector', 'Alternatives']]) + '>'


class SubDepiction_ServantLeft:
    def __init__(self, MeshDescriptorHigh=None, MeshDescriptorLow=None):
        self.MeshDescriptorHigh = MeshDescriptorHigh
        self.MeshDescriptorLow = MeshDescriptorLow

    def __repr__(self):
        return f'<SubDepiction_ServantLeft ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MeshDescriptorHigh', 'MeshDescriptorLow']]) + '>'


class SubDepiction_ServantRight:
    def __init__(self, MeshDescriptorHigh=None, MeshDescriptorLow=None):
        self.MeshDescriptorHigh = MeshDescriptorHigh
        self.MeshDescriptorLow = MeshDescriptorLow

    def __repr__(self):
        return f'<SubDepiction_ServantRight ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MeshDescriptorHigh', 'MeshDescriptorLow']]) + '>'


class ShowroomSubDepiction_ServantLeft:
    def __init__(self, MeshDescriptor=None):
        self.MeshDescriptor = MeshDescriptor

    def __repr__(self):
        return f'<ShowroomSubDepiction_ServantLeft ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MeshDescriptor']]) + '>'


class ShowroomSubDepiction_ServantRight:
    def __init__(self, MeshDescriptor=None):
        self.MeshDescriptor = MeshDescriptor

    def __repr__(self):
        return f'<ShowroomSubDepiction_ServantRight ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MeshDescriptor']]) + '>'


class SubDepiction_ATGMServantLeft:
    def __init__(self, MeshDescriptorHigh=None, MeshDescriptorLow=None):
        self.MeshDescriptorHigh = MeshDescriptorHigh
        self.MeshDescriptorLow = MeshDescriptorLow

    def __repr__(self):
        return f'<SubDepiction_ATGMServantLeft ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MeshDescriptorHigh', 'MeshDescriptorLow']]) + '>'


class SubDepiction_ATGMServantRight:
    def __init__(self, MeshDescriptorHigh=None, MeshDescriptorLow=None):
        self.MeshDescriptorHigh = MeshDescriptorHigh
        self.MeshDescriptorLow = MeshDescriptorLow

    def __repr__(self):
        return f'<SubDepiction_ATGMServantRight ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MeshDescriptorHigh', 'MeshDescriptorLow']]) + '>'


class ShowroomSubDepiction_ATGMServantLeft:
    def __init__(self, MeshDescriptor=None):
        self.MeshDescriptor = MeshDescriptor

    def __repr__(self):
        return f'<ShowroomSubDepiction_ATGMServantLeft ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MeshDescriptor']]) + '>'


class ShowroomSubDepiction_ATGMServantRight:
    def __init__(self, MeshDescriptor=None):
        self.MeshDescriptor = MeshDescriptor

    def __repr__(self):
        return f'<ShowroomSubDepiction_ATGMServantRight ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MeshDescriptor']]) + '>'


class SubDepiction_Driver:
    def __init__(self, MeshDescriptorHigh=None, MeshDescriptorLow=None):
        self.MeshDescriptorHigh = MeshDescriptorHigh
        self.MeshDescriptorLow = MeshDescriptorLow

    def __repr__(self):
        return f'<SubDepiction_Driver ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MeshDescriptorHigh', 'MeshDescriptorLow']]) + '>'


class SubDepiction_GunnerRight:
    def __init__(self, MeshDescriptorHigh=None, MeshDescriptorLow=None):
        self.MeshDescriptorHigh = MeshDescriptorHigh
        self.MeshDescriptorLow = MeshDescriptorLow

    def __repr__(self):
        return f'<SubDepiction_GunnerRight ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MeshDescriptorHigh', 'MeshDescriptorLow']]) + '>'


class SubDepiction_GunnerLeft:
    def __init__(self, MeshDescriptorHigh=None, MeshDescriptorLow=None):
        self.MeshDescriptorHigh = MeshDescriptorHigh
        self.MeshDescriptorLow = MeshDescriptorLow

    def __repr__(self):
        return f'<SubDepiction_GunnerLeft ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MeshDescriptorHigh', 'MeshDescriptorLow']]) + '>'


class SubDepiction_ServantWalkOnlyLeft:
    def __init__(self, MeshDescriptorHigh=None, MeshDescriptorLow=None):
        self.MeshDescriptorHigh = MeshDescriptorHigh
        self.MeshDescriptorLow = MeshDescriptorLow

    def __repr__(self):
        return f'<SubDepiction_ServantWalkOnlyLeft ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MeshDescriptorHigh', 'MeshDescriptorLow']]) + '>'


class SubDepiction_GunnerIdleOnlyLeft:
    def __init__(self, MeshDescriptorHigh=None, MeshDescriptorLow=None):
        self.MeshDescriptorHigh = MeshDescriptorHigh
        self.MeshDescriptorLow = MeshDescriptorLow

    def __repr__(self):
        return f'<SubDepiction_GunnerIdleOnlyLeft ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MeshDescriptorHigh', 'MeshDescriptorLow']]) + '>'


class SubDepiction_ServantWalkOnlyRight:
    def __init__(self, MeshDescriptorHigh=None, MeshDescriptorLow=None):
        self.MeshDescriptorHigh = MeshDescriptorHigh
        self.MeshDescriptorLow = MeshDescriptorLow

    def __repr__(self):
        return f'<SubDepiction_ServantWalkOnlyRight ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MeshDescriptorHigh', 'MeshDescriptorLow']]) + '>'


class SubDepiction_GunnerIdleOnlyRight:
    def __init__(self, MeshDescriptorHigh=None, MeshDescriptorLow=None):
        self.MeshDescriptorHigh = MeshDescriptorHigh
        self.MeshDescriptorLow = MeshDescriptorLow

    def __repr__(self):
        return f'<SubDepiction_GunnerIdleOnlyRight ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MeshDescriptorHigh', 'MeshDescriptorLow']]) + '>'


class ShowroomSubDepiction_GunnerLeft:
    def __init__(self, MeshDescriptor=None):
        self.MeshDescriptor = MeshDescriptor

    def __repr__(self):
        return f'<ShowroomSubDepiction_GunnerLeft ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MeshDescriptor']]) + '>'


class ShowroomSubDepiction_GunnerRight:
    def __init__(self, MeshDescriptor=None):
        self.MeshDescriptor = MeshDescriptor

    def __repr__(self):
        return f'<ShowroomSubDepiction_GunnerRight ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MeshDescriptor']]) + '>'


class SubDepiction_GunnerStandingUpIdleOnlyLeft:
    def __init__(self, MeshDescriptorHigh=None, MeshDescriptorLow=None):
        self.MeshDescriptorHigh = MeshDescriptorHigh
        self.MeshDescriptorLow = MeshDescriptorLow

    def __repr__(self):
        return f'<SubDepiction_GunnerStandingUpIdleOnlyLeft ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MeshDescriptorHigh', 'MeshDescriptorLow']]) + '>'


class ShowroomSubDepiction_GunnerStandingUpLeft:
    def __init__(self, MeshDescriptor=None):
        self.MeshDescriptor = MeshDescriptor

    def __repr__(self):
        return f'<ShowroomSubDepiction_GunnerStandingUpLeft ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MeshDescriptor']]) + '>'


class SubDepiction_DriverUndeployed:
    def __init__(self, MeshDescriptorHigh=None, MeshDescriptorLow=None):
        self.MeshDescriptorHigh = MeshDescriptorHigh
        self.MeshDescriptorLow = MeshDescriptorLow

    def __repr__(self):
        return f'<SubDepiction_DriverUndeployed ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MeshDescriptorHigh', 'MeshDescriptorLow']]) + '>'


class SubDepiction_GunnerDeployed:
    def __init__(self, MeshDescriptorHigh=None, MeshDescriptorLow=None):
        self.MeshDescriptorHigh = MeshDescriptorHigh
        self.MeshDescriptorLow = MeshDescriptorLow

    def __repr__(self):
        return f'<SubDepiction_GunnerDeployed ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MeshDescriptorHigh', 'MeshDescriptorLow']]) + '>'


class DepictionOperator_WeaponMissileCarriageFire:
    def __init__(self, FireEffectTag=None, WeaponIndex=None, WeaponShootDataPropertyName=None, Connoisseur=None, NbProj=None):
        self.FireEffectTag = FireEffectTag
        self.WeaponIndex = WeaponIndex
        self.WeaponShootDataPropertyName = WeaponShootDataPropertyName
        self.Connoisseur = Connoisseur
        self.NbProj = NbProj

    def __repr__(self):
        return f'<DepictionOperator_WeaponMissileCarriageFire ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['FireEffectTag', 'WeaponIndex', 'WeaponShootDataPropertyName', 'Connoisseur', 'NbProj']]) + '>'


class TacticVehicleDepictionTemplate:
    def __init__(self, Selector=None, CoatingName=None, Actions=None, Operators=None, SubDepictions=None, Alternatives=None, SubDepictionGenerators=None):
        self.Selector = Selector
        self.CoatingName = CoatingName
        self.Actions = Actions
        self.Operators = Operators
        self.SubDepictions = SubDepictions
        self.Alternatives = Alternatives
        self.SubDepictionGenerators = SubDepictionGenerators

    def __repr__(self):
        return f'<TacticVehicleDepictionTemplate ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Selector', 'CoatingName', 'Actions', 'Operators', 'SubDepictions', 'Alternatives', 'SubDepictionGenerators']]) + '>'


class DepictionOperator_WeaponInstantFire:
    def __init__(self, FireEffectTag=None, WeaponShootDataPropertyName=None, NbProj=None, Anchors=None):
        self.FireEffectTag = FireEffectTag
        self.WeaponShootDataPropertyName = WeaponShootDataPropertyName
        self.NbProj = NbProj
        self.Anchors = Anchors

    def __repr__(self):
        return f'<DepictionOperator_WeaponInstantFire ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['FireEffectTag', 'WeaponShootDataPropertyName', 'NbProj', 'Anchors']]) + '>'


class DepictionOperator_WeaponContinuousFire:
    def __init__(self, FireEffectTag=None, WeaponActiveAndCanShootPropertyName=None, WeaponShootDataPropertyName=None, Anchors=None, NbFX=None):
        self.FireEffectTag = FireEffectTag
        self.WeaponActiveAndCanShootPropertyName = WeaponActiveAndCanShootPropertyName
        self.WeaponShootDataPropertyName = WeaponShootDataPropertyName
        self.Anchors = Anchors
        self.NbFX = NbFX

    def __repr__(self):
        return f'<DepictionOperator_WeaponContinuousFire ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['FireEffectTag', 'WeaponActiveAndCanShootPropertyName', 'WeaponShootDataPropertyName', 'Anchors', 'NbFX']]) + '>'


class TransportedInfantrySubGenerator:
    def __init__(self, Mesh=None):
        self.Mesh = Mesh

    def __repr__(self):
        return f'<TransportedInfantrySubGenerator ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Mesh']]) + '>'


class DepictionOperator_Carousel_Radar:
    def __init__(self, WeaponIgnoredProperties=None, WaitTimeInSeconds=None, RevolutionsPerMinute=None):
        self.WeaponIgnoredProperties = WeaponIgnoredProperties
        self.WaitTimeInSeconds = WaitTimeInSeconds
        self.RevolutionsPerMinute = RevolutionsPerMinute

    def __repr__(self):
        return f'<DepictionOperator_Carousel_Radar ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['WeaponIgnoredProperties', 'WaitTimeInSeconds', 'RevolutionsPerMinute']]) + '>'


class RocketSubDepictionTemplate:
    def __init__(self, RocketCount=None, WeaponIndex=None, RocketMeshDescriptor=None, UnitMeshDescriptor=None, PhysicalProperty=None):
        self.RocketCount = RocketCount
        self.WeaponIndex = WeaponIndex
        self.RocketMeshDescriptor = RocketMeshDescriptor
        self.UnitMeshDescriptor = UnitMeshDescriptor
        self.PhysicalProperty = PhysicalProperty

    def __repr__(self):
        return f'<RocketSubDepictionTemplate ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['RocketCount', 'WeaponIndex', 'RocketMeshDescriptor', 'UnitMeshDescriptor', 'PhysicalProperty']]) + '>'


class DepictionOperator_CarouselWithSpecificAngle_Radar:
    def __init__(self, CoveragePercentage=None, WeaponIgnoredProperties=None, WaitTimeInSeconds=None, RevolutionsPerMinute=None):
        self.CoveragePercentage = CoveragePercentage
        self.WeaponIgnoredProperties = WeaponIgnoredProperties
        self.WaitTimeInSeconds = WaitTimeInSeconds
        self.RevolutionsPerMinute = RevolutionsPerMinute

    def __repr__(self):
        return f'<DepictionOperator_CarouselWithSpecificAngle_Radar ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['CoveragePercentage', 'WeaponIgnoredProperties', 'WaitTimeInSeconds', 'RevolutionsPerMinute']]) + '>'


class StrategicGroundVehiclePawnDepictionTemplate:
    def __init__(self, MeshSocle=None, MeshDescriptorPawn=None, SubDepictionGenerators=None):
        self.MeshSocle = MeshSocle
        self.MeshDescriptorPawn = MeshDescriptorPawn
        self.SubDepictionGenerators = SubDepictionGenerators

    def __repr__(self):
        return f'<StrategicGroundVehiclePawnDepictionTemplate ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MeshSocle', 'MeshDescriptorPawn', 'SubDepictionGenerators']]) + '>'


class StrategicHelicopterPawnDepictionTemplate:
    def __init__(self, MeshDescriptorPawn=None, MeshSocle=None):
        self.MeshDescriptorPawn = MeshDescriptorPawn
        self.MeshSocle = MeshSocle

    def __repr__(self):
        return f'<StrategicHelicopterPawnDepictionTemplate ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MeshDescriptorPawn', 'MeshSocle']]) + '>'


class StrategicInfantryPawnDepictionTemplate:
    def __init__(self, MeshDescriptorPawn=None, MeshSocle=None):
        self.MeshDescriptorPawn = MeshDescriptorPawn
        self.MeshSocle = MeshSocle

    def __repr__(self):
        return f'<StrategicInfantryPawnDepictionTemplate ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MeshDescriptorPawn', 'MeshSocle']]) + '>'


class TacticTowedSubDepictionTemplate:
    def __init__(self, Alternatives=None, InitialPoses=None, MissileAlternatives=None, AllowedUnits=None):
        self.Alternatives = Alternatives
        self.InitialPoses = InitialPoses
        self.MissileAlternatives = MissileAlternatives
        self.AllowedUnits = AllowedUnits

    def __repr__(self):
        return f'<TacticTowedSubDepictionTemplate ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Alternatives', 'InitialPoses', 'MissileAlternatives', 'AllowedUnits']]) + '>'


class TInitialPoseAngle:
    def __init__(self, Angle=None, MeshDescriptor=None):
        self.Angle = Angle
        self.MeshDescriptor = MeshDescriptor

    def __repr__(self):
        return f'<TInitialPoseAngle ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Angle', 'MeshDescriptor']]) + '>'


class TInitialPoseAnimation:
    def __init__(self, MeshDescriptor=None, Animation=None):
        self.MeshDescriptor = MeshDescriptor
        self.Animation = Animation

    def __repr__(self):
        return f'<TInitialPoseAnimation ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MeshDescriptor', 'Animation']]) + '>'


class TemplateInfantryDepictionSquad:
    def __init__(self, SoundOperator=None):
        self.SoundOperator = SoundOperator

    def __repr__(self):
        return f'<TemplateInfantryDepictionSquad ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['SoundOperator']]) + '>'


class TMeshlessDepictionDescriptor:
    def __init__(self, ReferenceMeshForSkeleton=None, SelectorId=None):
        self.ReferenceMeshForSkeleton = ReferenceMeshForSkeleton
        self.SelectorId = SelectorId

    def __repr__(self):
        return f'<TMeshlessDepictionDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ReferenceMeshForSkeleton', 'SelectorId']]) + '>'


class TemplateAllSubWeaponDepiction:
    def __init__(self, Alternatives=None, Operators=None):
        self.Alternatives = Alternatives
        self.Operators = Operators

    def __repr__(self):
        return f'<TemplateAllSubWeaponDepiction ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Alternatives', 'Operators']]) + '>'


class DepictionOperator_WeaponInstantFireInfantry:
    def __init__(self, WeaponShootDataPropertyName=None, FireEffectTag=None):
        self.WeaponShootDataPropertyName = WeaponShootDataPropertyName
        self.FireEffectTag = FireEffectTag

    def __repr__(self):
        return f'<DepictionOperator_WeaponInstantFireInfantry ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['WeaponShootDataPropertyName', 'FireEffectTag']]) + '>'


class TemplateAllSubBackpackWeaponDepiction:
    def __init__(self, Alternatives=None):
        self.Alternatives = Alternatives

    def __repr__(self):
        return f'<TemplateAllSubBackpackWeaponDepiction ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Alternatives']]) + '>'


class TemplateInfantryDepictionFactoryTactic:
    def __init__(self, Selector=None, Operators=None, SubDepictions=None, Alternatives=None):
        self.Selector = Selector
        self.Operators = Operators
        self.SubDepictions = SubDepictions
        self.Alternatives = Alternatives

    def __repr__(self):
        return f'<TemplateInfantryDepictionFactoryTactic ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Selector', 'Operators', 'SubDepictions', 'Alternatives']]) + '>'


class DepictionOperator_SkeletalAnimation2_Default:
    def __init__(self, ConditionalTags=None):
        self.ConditionalTags = ConditionalTags

    def __repr__(self):
        return f'<DepictionOperator_SkeletalAnimation2_Default ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ConditionalTags']]) + '>'


class TemplateInfantryDepictionFactoryGhost:
    def __init__(self, Selector=None, Alternatives=None):
        self.Selector = Selector
        self.Alternatives = Alternatives

    def __repr__(self):
        return f'<TemplateInfantryDepictionFactoryGhost ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Selector', 'Alternatives']]) + '>'


class TemplateWeaponAccessorySubDepiction:
    def __init__(self, MeshDescriptor=None, EnabledValue=None):
        self.MeshDescriptor = MeshDescriptor
        self.EnabledValue = EnabledValue

    def __repr__(self):
        return f'<TemplateWeaponAccessorySubDepiction ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MeshDescriptor', 'EnabledValue']]) + '>'


class TemplateInfantrySelectorTactic:
    def __init__(self, UniqueCount=None, Surrogates=None):
        self.UniqueCount = UniqueCount
        self.Surrogates = Surrogates

    def __repr__(self):
        return f'<TemplateInfantrySelectorTactic ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['UniqueCount', 'Surrogates']]) + '>'


class InfantryFiringHappening:
    def __init__(self, Power=None, WaitBetweenShot=None, Action=None):
        self.Power = Power
        self.WaitBetweenShot = WaitBetweenShot
        self.Action = Action

    def __repr__(self):
        return f'<InfantryFiringHappening ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Power', 'WaitBetweenShot', 'Action']]) + '>'


class InfantryProjectileHappening:
    def __init__(self, Power=None, FluidFriction=None, WithoutPhysics=None, InitialSpeed=None, WaitBetweenShot=None, Action=None):
        self.Power = Power
        self.FluidFriction = FluidFriction
        self.WithoutPhysics = WithoutPhysics
        self.InitialSpeed = InitialSpeed
        self.WaitBetweenShot = WaitBetweenShot
        self.Action = Action

    def __repr__(self):
        return f'<InfantryProjectileHappening ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Power', 'FluidFriction', 'WithoutPhysics', 'InitialSpeed', 'WaitBetweenShot', 'Action']]) + '>'


class TEnumResourceList:
    def __init__(self, Values=None, Alias=None):
        self.Values = Values
        self.Alias = Alias

    def __repr__(self):
        return f'<TEnumResourceList ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Values', 'Alias']]) + '>'


class TCubeActionCapacityButtonInformationsDescriptor:
    def __init__(self, Mapping=None, HoverSound=None, CubeActionFunctionType=None, BackgroundTexture=None, Descriptor=None, HintExtendedToken=None, ButtonTextToken=None, HintTitleToken=None, CubeActionName=None, HintBodyToken=None, HintDico=None, ClickSound=None):
        self.Mapping = Mapping
        self.HoverSound = HoverSound
        self.CubeActionFunctionType = CubeActionFunctionType
        self.BackgroundTexture = BackgroundTexture
        self.Descriptor = Descriptor
        self.HintExtendedToken = HintExtendedToken
        self.ButtonTextToken = ButtonTextToken
        self.HintTitleToken = HintTitleToken
        self.CubeActionName = CubeActionName
        self.HintBodyToken = HintBodyToken
        self.HintDico = HintDico
        self.ClickSound = ClickSound

    def __repr__(self):
        return f'<TCubeActionCapacityButtonInformationsDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Mapping', 'HoverSound', 'CubeActionFunctionType', 'BackgroundTexture', 'Descriptor', 'HintExtendedToken', 'ButtonTextToken', 'HintTitleToken', 'CubeActionName', 'HintBodyToken', 'HintDico', 'ClickSound']]) + '>'


class TCubeActionMenuDescriptor:
    def __init__(self, CubeActionName=None, CubeActionContent=None):
        self.CubeActionName = CubeActionName
        self.CubeActionContent = CubeActionContent

    def __repr__(self):
        return f'<TCubeActionMenuDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['CubeActionName', 'CubeActionContent']]) + '>'


class TStrategicLabelModuleDescriptor:
    def __init__(self, BackgroundTexture=None):
        self.BackgroundTexture = BackgroundTexture

    def __repr__(self):
        return f'<TStrategicLabelModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['BackgroundTexture']]) + '>'


class TDeckModuleDescriptor:
    def __init__(self, PictureForSelection=None, Score=None, RegimentName=None, DeckIdentifier=None, AcceptableTagSet=None, MaxPackCount=None):
        self.PictureForSelection = PictureForSelection
        self.Score = Score
        self.RegimentName = RegimentName
        self.DeckIdentifier = DeckIdentifier
        self.AcceptableTagSet = AcceptableTagSet
        self.MaxPackCount = MaxPackCount

    def __repr__(self):
        return f'<TDeckModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['PictureForSelection', 'Score', 'RegimentName', 'DeckIdentifier', 'AcceptableTagSet', 'MaxPackCount']]) + '>'


class TStrategicBattleModuleDescriptor:
    def __init__(self, HasZoneOfControl=None, BattleRole=None, AirDenyRadiusInAPCase=None, BattleSupportRadiusInAPCase=None, CanBeInitialTarget=None):
        self.HasZoneOfControl = HasZoneOfControl
        self.BattleRole = BattleRole
        self.AirDenyRadiusInAPCase = AirDenyRadiusInAPCase
        self.BattleSupportRadiusInAPCase = BattleSupportRadiusInAPCase
        self.CanBeInitialTarget = CanBeInitialTarget

    def __repr__(self):
        return f'<TStrategicBattleModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['HasZoneOfControl', 'BattleRole', 'AirDenyRadiusInAPCase', 'BattleSupportRadiusInAPCase', 'CanBeInitialTarget']]) + '>'


class TActionPointsModuleDescriptor:
    def __init__(self, NbInitialActionsPointsForProducedPawn=None, InitialActionPoint=None, ActionPointRecoveryPerTurn=None):
        self.NbInitialActionsPointsForProducedPawn = NbInitialActionsPointsForProducedPawn
        self.InitialActionPoint = InitialActionPoint
        self.ActionPointRecoveryPerTurn = ActionPointRecoveryPerTurn

    def __repr__(self):
        return f'<TActionPointsModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['NbInitialActionsPointsForProducedPawn', 'InitialActionPoint', 'ActionPointRecoveryPerTurn']]) + '>'


class StrategicUIModuleDescriptor:
    def __init__(self, ProdMenuTexture=None, NameToken=None):
        self.ProdMenuTexture = ProdMenuTexture
        self.NameToken = NameToken

    def __repr__(self):
        return f'<StrategicUIModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ProdMenuTexture', 'NameToken']]) + '>'


class TStrategicPositionModuleDescriptor:
    def __init__(self, IsAirport=None):
        self.IsAirport = IsAirport

    def __repr__(self):
        return f'<TStrategicPositionModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['IsAirport']]) + '>'


class StrategicFatigueModuleDescriptor:
    def __init__(self, InitialFatigue=None):
        self.InitialFatigue = InitialFatigue

    def __repr__(self):
        return f'<StrategicFatigueModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['InitialFatigue']]) + '>'


class TInfluenceMapModuleDescriptor:
    def __init__(self, InfluenceStrength=None, StrengthDecayPerSecond=None, MinimumInfluenceStrength=None, PreventsDecayInZone=None):
        self.InfluenceStrength = InfluenceStrength
        self.StrengthDecayPerSecond = StrengthDecayPerSecond
        self.MinimumInfluenceStrength = MinimumInfluenceStrength
        self.PreventsDecayInZone = PreventsDecayInZone

    def __repr__(self):
        return f'<TInfluenceMapModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['InfluenceStrength', 'StrengthDecayPerSecond', 'MinimumInfluenceStrength', 'PreventsDecayInZone']]) + '>'


class TStrategicSupplierModuleDescriptor:
    def __init__(self, SupplyActionPoint=None):
        self.SupplyActionPoint = SupplyActionPoint

    def __repr__(self):
        return f'<TStrategicSupplierModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['SupplyActionPoint']]) + '>'


class TStrategicAirportModuleDescriptor:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TStrategicAirportModuleDescriptor>'


class TStrategicMovementModuleDescriptor:
    def __init__(self, SpeedReducerTerrainAPConsumptionModifier=None, ConsumeAPOnMove=None, MaxSpeed=None, RoadAPConsumptionModifier=None, NormalTerrainAPConsumptionModifier=None):
        self.SpeedReducerTerrainAPConsumptionModifier = SpeedReducerTerrainAPConsumptionModifier
        self.ConsumeAPOnMove = ConsumeAPOnMove
        self.MaxSpeed = MaxSpeed
        self.RoadAPConsumptionModifier = RoadAPConsumptionModifier
        self.NormalTerrainAPConsumptionModifier = NormalTerrainAPConsumptionModifier

    def __repr__(self):
        return f'<TStrategicMovementModuleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['SpeedReducerTerrainAPConsumptionModifier', 'ConsumeAPOnMove', 'MaxSpeed', 'RoadAPConsumptionModifier', 'NormalTerrainAPConsumptionModifier']]) + '>'


class TAcknowUnitAction:
    def __init__(self, Values=None):
        self.Values = Values

    def __repr__(self):
        return f'<TAcknowUnitAction ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Values']]) + '>'


class TAcknowUnitContainerDescriptor:
    def __init__(self, Content=None):
        self.Content = Content

    def __repr__(self):
        return f'<TAcknowUnitContainerDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Content']]) + '>'


class TAcknowDescriptor:
    def __init__(self, MotherCountry=None, TypeSpecific=None, Sound=None, Action=None):
        self.MotherCountry = MotherCountry
        self.TypeSpecific = TypeSpecific
        self.Sound = Sound
        self.Action = Action

    def __repr__(self):
        return f'<TAcknowDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MotherCountry', 'TypeSpecific', 'Sound', 'Action']]) + '>'


class Template_UnitAcknow:
    def __init__(self, Identifier=None, Filter=None):
        self.Identifier = Identifier
        self.Filter = Filter

    def __repr__(self):
        return f'<Template_UnitAcknow ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Identifier', 'Filter']]) + '>'


class TAcknowUnitType:
    def __init__(self, Values=None):
        self.Values = Values

    def __repr__(self):
        return f'<TAcknowUnitType ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Values']]) + '>'


class TCosmeticConstantMovementSoundOperatorDesc:
    def __init__(self, OperatorId=None, MaxVolumeSpeed=None, MaxVolume=None, FadeInDuration=None, Sounds=None, MinVolume=None):
        self.OperatorId = OperatorId
        self.MaxVolumeSpeed = MaxVolumeSpeed
        self.MaxVolume = MaxVolume
        self.FadeInDuration = FadeInDuration
        self.Sounds = Sounds
        self.MinVolume = MinVolume

    def __repr__(self):
        return f'<TCosmeticConstantMovementSoundOperatorDesc ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['OperatorId', 'MaxVolumeSpeed', 'MaxVolume', 'FadeInDuration', 'Sounds', 'MinVolume']]) + '>'


class TCosmeticDriveMovementSoundOperatorDesc:
    def __init__(self, OperatorId=None, MaxVolumeSpeed=None, IdleFadeOutDuration=None, IdleSounds=None, IdleDuration=None, IdleFadeInDuration=None, VolumeIdleStop=None, RunSounds=None, StartSounds=None, MaxVolume=None, StopSounds=None, RunFadeOutDuration=None, RunFadeInDuration=None, RunOutPitchVelocity=None, MinVolume=None, RunOutPitchToGo=None):
        self.OperatorId = OperatorId
        self.MaxVolumeSpeed = MaxVolumeSpeed
        self.IdleFadeOutDuration = IdleFadeOutDuration
        self.IdleSounds = IdleSounds
        self.IdleDuration = IdleDuration
        self.IdleFadeInDuration = IdleFadeInDuration
        self.VolumeIdleStop = VolumeIdleStop
        self.RunSounds = RunSounds
        self.StartSounds = StartSounds
        self.MaxVolume = MaxVolume
        self.StopSounds = StopSounds
        self.RunFadeOutDuration = RunFadeOutDuration
        self.RunFadeInDuration = RunFadeInDuration
        self.RunOutPitchVelocity = RunOutPitchVelocity
        self.MinVolume = MinVolume
        self.RunOutPitchToGo = RunOutPitchToGo

    def __repr__(self):
        return f'<TCosmeticDriveMovementSoundOperatorDesc ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['OperatorId', 'MaxVolumeSpeed', 'IdleFadeOutDuration', 'IdleSounds', 'IdleDuration', 'IdleFadeInDuration', 'VolumeIdleStop', 'RunSounds', 'StartSounds', 'MaxVolume', 'StopSounds', 'RunFadeOutDuration', 'RunFadeInDuration', 'RunOutPitchVelocity', 'MinVolume', 'RunOutPitchToGo']]) + '>'


class TCosmeticFlyMovementSoundOperatorDesc:
    def __init__(self, OperatorId=None, MaxVolumeSpeed=None, IdleFadeOutDuration=None, IdleFadeInDuration=None, RunSounds=None, StartSounds=None, MaxVolume=None, StopSounds=None, RunFadeOutDuration=None, RunFadeInDuration=None, RunOutPitchVelocity=None, MinVolume=None, CrashSounds=None, RunOutPitchToGo=None):
        self.OperatorId = OperatorId
        self.MaxVolumeSpeed = MaxVolumeSpeed
        self.IdleFadeOutDuration = IdleFadeOutDuration
        self.IdleFadeInDuration = IdleFadeInDuration
        self.RunSounds = RunSounds
        self.StartSounds = StartSounds
        self.MaxVolume = MaxVolume
        self.StopSounds = StopSounds
        self.RunFadeOutDuration = RunFadeOutDuration
        self.RunFadeInDuration = RunFadeInDuration
        self.RunOutPitchVelocity = RunOutPitchVelocity
        self.MinVolume = MinVolume
        self.CrashSounds = CrashSounds
        self.RunOutPitchToGo = RunOutPitchToGo

    def __repr__(self):
        return f'<TCosmeticFlyMovementSoundOperatorDesc ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['OperatorId', 'MaxVolumeSpeed', 'IdleFadeOutDuration', 'IdleFadeInDuration', 'RunSounds', 'StartSounds', 'MaxVolume', 'StopSounds', 'RunFadeOutDuration', 'RunFadeInDuration', 'RunOutPitchVelocity', 'MinVolume', 'CrashSounds', 'RunOutPitchToGo']]) + '>'


class TCosmeticWalkMovementSoundOperatorDesc:
    def __init__(self, OperatorId=None, MaxVolumeSpeed=None, IdleFadeOutDuration=None, RunSounds=None, StartSounds=None, MaxVolume=None, StopSounds=None, RunFadeOutDuration=None, RunFadeInDuration=None, RunOutPitchVelocity=None, MinVolume=None, IdleSounds=None, RunOutPitchToGo=None):
        self.OperatorId = OperatorId
        self.MaxVolumeSpeed = MaxVolumeSpeed
        self.IdleFadeOutDuration = IdleFadeOutDuration
        self.RunSounds = RunSounds
        self.StartSounds = StartSounds
        self.MaxVolume = MaxVolume
        self.StopSounds = StopSounds
        self.RunFadeOutDuration = RunFadeOutDuration
        self.RunFadeInDuration = RunFadeInDuration
        self.RunOutPitchVelocity = RunOutPitchVelocity
        self.MinVolume = MinVolume
        self.IdleSounds = IdleSounds
        self.RunOutPitchToGo = RunOutPitchToGo

    def __repr__(self):
        return f'<TCosmeticWalkMovementSoundOperatorDesc ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['OperatorId', 'MaxVolumeSpeed', 'IdleFadeOutDuration', 'RunSounds', 'StartSounds', 'MaxVolume', 'StopSounds', 'RunFadeOutDuration', 'RunFadeInDuration', 'RunOutPitchVelocity', 'MinVolume', 'IdleSounds', 'RunOutPitchToGo']]) + '>'


class TSoundSet:
    def __init__(self, Items=None):
        self.Items = Items

    def __repr__(self):
        return f'<TSoundSet ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Items']]) + '>'


class TSoundHappening:
    def __init__(self, Volume=None, SoundDescList=None):
        self.Volume = Volume
        self.SoundDescList = SoundDescList

    def __repr__(self):
        return f'<TSoundHappening ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Volume', 'SoundDescList']]) + '>'


class TCosmeticTurretSoundOperatorDesc:
    def __init__(self, OperatorId=None, StartSound=None, RotateSound=None, StopSound=None, TurretAxisName=None):
        self.OperatorId = OperatorId
        self.StartSound = StartSound
        self.RotateSound = RotateSound
        self.StopSound = StopSound
        self.TurretAxisName = TurretAxisName

    def __repr__(self):
        return f'<TCosmeticTurretSoundOperatorDesc ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['OperatorId', 'StartSound', 'RotateSound', 'StopSound', 'TurretAxisName']]) + '>'


class TUnitSpecialtiesContainer:
    def __init__(self, Descriptors=None):
        self.Descriptors = Descriptors

    def __repr__(self):
        return f'<TUnitSpecialtiesContainer ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Descriptors']]) + '>'


class TUnitSpecialtyDescriptor:
    def __init__(self, SpecialtyHintExtendedToken=None, SpecialtyTextureName=None, SpecialtyHintBodyToken=None, SpecialtyHintTitleToken=None):
        self.SpecialtyHintExtendedToken = SpecialtyHintExtendedToken
        self.SpecialtyTextureName = SpecialtyTextureName
        self.SpecialtyHintBodyToken = SpecialtyHintBodyToken
        self.SpecialtyHintTitleToken = SpecialtyHintTitleToken

    def __repr__(self):
        return f'<TUnitSpecialtyDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['SpecialtyHintExtendedToken', 'SpecialtyTextureName', 'SpecialtyHintBodyToken', 'SpecialtyHintTitleToken']]) + '>'


class TUnitTraitsContainer:
    def __init__(self, Descriptors=None):
        self.Descriptors = Descriptors

    def __repr__(self):
        return f'<TUnitTraitsContainer ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Descriptors']]) + '>'


class TUnitTraitDescriptor:
    def __init__(self, TraitHintTitleToken=None, TraitTextureName=None, TraitHintBodyToken=None):
        self.TraitHintTitleToken = TraitHintTitleToken
        self.TraitTextureName = TraitTextureName
        self.TraitHintBodyToken = TraitHintBodyToken

    def __repr__(self):
        return f'<TUnitTraitDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TraitHintTitleToken', 'TraitTextureName', 'TraitHintBodyToken']]) + '>'


class TWeaponsMinMaxValuesInterfaceHelper:
    def __init__(self, WeaponsMinMaxValues=None, UnitMinMaxValues=None):
        self.WeaponsMinMaxValues = WeaponsMinMaxValues
        self.UnitMinMaxValues = UnitMinMaxValues

    def __repr__(self):
        return f'<TWeaponsMinMaxValuesInterfaceHelper ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['WeaponsMinMaxValues', 'UnitMinMaxValues']]) + '>'


class TWeaponMinMaxValues:
    def __init__(self, SuppressDamages=None, TurretSpeed=None, MaxRangeHAGRU=None, SupplyCost=None, PhysicalDamages=None, MaxRangeTBAGRU=None, SplashDamageRadiusGRU=None, MaxRangeGRU=None, NbShotsBySalvo=None, AccuracyMovement=None, TimeBetweenTwoShots=None, Accuracy=None, Penetration=None, ReloadTime=None, AimTime=None, RateOfFire=None):
        self.SuppressDamages = SuppressDamages
        self.TurretSpeed = TurretSpeed
        self.MaxRangeHAGRU = MaxRangeHAGRU
        self.SupplyCost = SupplyCost
        self.PhysicalDamages = PhysicalDamages
        self.MaxRangeTBAGRU = MaxRangeTBAGRU
        self.SplashDamageRadiusGRU = SplashDamageRadiusGRU
        self.MaxRangeGRU = MaxRangeGRU
        self.NbShotsBySalvo = NbShotsBySalvo
        self.AccuracyMovement = AccuracyMovement
        self.TimeBetweenTwoShots = TimeBetweenTwoShots
        self.Accuracy = Accuracy
        self.Penetration = Penetration
        self.ReloadTime = ReloadTime
        self.AimTime = AimTime
        self.RateOfFire = RateOfFire

    def __repr__(self):
        return f'<TWeaponMinMaxValues ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['SuppressDamages', 'TurretSpeed', 'MaxRangeHAGRU', 'SupplyCost', 'PhysicalDamages', 'MaxRangeTBAGRU', 'SplashDamageRadiusGRU', 'MaxRangeGRU', 'NbShotsBySalvo', 'AccuracyMovement', 'TimeBetweenTwoShots', 'Accuracy', 'Penetration', 'ReloadTime', 'AimTime', 'RateOfFire']]) + '>'


class TMinMaxValue:
    def __init__(self, Max=None, Min=None):
        self.Max = Max
        self.Min = Min

    def __repr__(self):
        return f'<TMinMaxValue ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Max', 'Min']]) + '>'


class TUnitMinMaxValues:
    def __init__(self, Armor=None):
        self.Armor = Armor

    def __repr__(self):
        return f'<TUnitMinMaxValues ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Armor']]) + '>'


class TUIResourceTexture:
    def __init__(self, FileName=None):
        self.FileName = FileName

    def __repr__(self):
        return f'<TUIResourceTexture ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['FileName']]) + '>'


class TResourcePackLoader:
    def __init__(self, Packs=None):
        self.Packs = Packs

    def __repr__(self):
        return f'<TResourcePackLoader ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Packs']]) + '>'


class TResourceDescriptorMeshPack:
    def __init__(self, PackName=None, TransactionFiles=None, UseDecompressedBufferResourceThreshold=None):
        self.PackName = PackName
        self.TransactionFiles = TransactionFiles
        self.UseDecompressedBufferResourceThreshold = UseDecompressedBufferResourceThreshold

    def __repr__(self):
        return f'<TResourceDescriptorMeshPack ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['PackName', 'TransactionFiles', 'UseDecompressedBufferResourceThreshold']]) + '>'


class TResourceDescriptorProxyPack:
    def __init__(self, PackName=None, TransactionFiles=None):
        self.PackName = PackName
        self.TransactionFiles = TransactionFiles

    def __repr__(self):
        return f'<TResourceDescriptorProxyPack ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['PackName', 'TransactionFiles']]) + '>'


class TSoundAndMusicSwitchDescriptor:
    def __init__(self, SoundServiceVolumesDescriptor=None):
        self.SoundServiceVolumesDescriptor = SoundServiceVolumesDescriptor

    def __repr__(self):
        return f'<TSoundAndMusicSwitchDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['SoundServiceVolumesDescriptor']]) + '>'


class Music:
    def __init__(self, FileName=None, Copyrighted=None):
        self.FileName = FileName
        self.Copyrighted = Copyrighted

    def __repr__(self):
        return f'<Music ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['FileName', 'Copyrighted']]) + '>'


class TCurrentSavingVersion:
    def __init__(self, VersionNum=None):
        self.VersionNum = VersionNum

    def __repr__(self):
        return f'<TCurrentSavingVersion ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['VersionNum']]) + '>'


class TTFSCommand_UISymbol:
    def __init__(self, BBMin=None, ShaderDescriptor=None, UseTextColor=None, BBMax=None, TextureToken=None):
        self.BBMin = BBMin
        self.ShaderDescriptor = ShaderDescriptor
        self.UseTextColor = UseTextColor
        self.BBMax = BBMax
        self.TextureToken = TextureToken

    def __repr__(self):
        return f'<TTFSCommand_UISymbol ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['BBMin', 'ShaderDescriptor', 'UseTextColor', 'BBMax', 'TextureToken']]) + '>'


class TemplateTFS_Division:
    def __init__(self, TextureToken=None):
        self.TextureToken = TextureToken

    def __repr__(self):
        return f'<TemplateTFS_Division ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TextureToken']]) + '>'


class TemplateTFS_Flag:
    def __init__(self, TextureToken=None):
        self.TextureToken = TextureToken

    def __repr__(self):
        return f'<TemplateTFS_Flag ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TextureToken']]) + '>'


class TUIHintManagementProperties:
    def __init__(self, AppearAfterDuration=None, DisapearAfterDuration=None, ExtendAfterDuration=None, PointerFollowingProperties=None):
        self.AppearAfterDuration = AppearAfterDuration
        self.DisapearAfterDuration = DisapearAfterDuration
        self.ExtendAfterDuration = ExtendAfterDuration
        self.PointerFollowingProperties = PointerFollowingProperties

    def __repr__(self):
        return f'<TUIHintManagementProperties ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['AppearAfterDuration', 'DisapearAfterDuration', 'ExtendAfterDuration', 'PointerFollowingProperties']]) + '>'


class TPointerFollowingPropertiesRTTI:
    def __init__(self, MagnifiableOffset=None, HorizontalPlacement=None, VerticalPlacement=None, OutOfBorderHorizontalAction=None, OutOfBorderVerticalAction=None):
        self.MagnifiableOffset = MagnifiableOffset
        self.HorizontalPlacement = HorizontalPlacement
        self.VerticalPlacement = VerticalPlacement
        self.OutOfBorderHorizontalAction = OutOfBorderHorizontalAction
        self.OutOfBorderVerticalAction = OutOfBorderVerticalAction

    def __repr__(self):
        return f'<TPointerFollowingPropertiesRTTI ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MagnifiableOffset', 'HorizontalPlacement', 'VerticalPlacement', 'OutOfBorderHorizontalAction', 'OutOfBorderVerticalAction']]) + '>'


class AuraDescriptor:
    def __init__(self, TopRightTexture=None, BottomLeftTexture=None, TopTextureToken=None, LeftTextureToken=None, RightTextureToken=None, BottomTextureToken=None, AuraBorderSize=None, BottomRightTexture=None, TopLeftTexture=None):
        self.TopRightTexture = TopRightTexture
        self.BottomLeftTexture = BottomLeftTexture
        self.TopTextureToken = TopTextureToken
        self.LeftTextureToken = LeftTextureToken
        self.RightTextureToken = RightTextureToken
        self.BottomTextureToken = BottomTextureToken
        self.AuraBorderSize = AuraBorderSize
        self.BottomRightTexture = BottomRightTexture
        self.TopLeftTexture = TopLeftTexture

    def __repr__(self):
        return f'<AuraDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TopRightTexture', 'BottomLeftTexture', 'TopTextureToken', 'LeftTextureToken', 'RightTextureToken', 'BottomTextureToken', 'AuraBorderSize', 'BottomRightTexture', 'TopLeftTexture']]) + '>'


class TGamerPictureFallbacks:
    def __init__(self, DefaultAvatarTexture=None):
        self.DefaultAvatarTexture = DefaultAvatarTexture

    def __repr__(self):
        return f'<TGamerPictureFallbacks ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['DefaultAvatarTexture']]) + '>'


class TResourceTexturePreloadTextureData:
    def __init__(self, FileName=None):
        self.FileName = FileName

    def __repr__(self):
        return f'<TResourceTexturePreloadTextureData ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['FileName']]) + '>'


class TDescriptorPositionEvents:
    def __init__(self, MaxEventCount=None, EventsDurationInSeconds=None, TriggNextEventDurationCeilInSeconds=None, CameraMoverTargetClient=None, World3D=None, SituationAwarenessNextEventCommandName=None, MinAltitudeInMeter=None, MaxAltitudeInMeter=None):
        self.MaxEventCount = MaxEventCount
        self.EventsDurationInSeconds = EventsDurationInSeconds
        self.TriggNextEventDurationCeilInSeconds = TriggNextEventDurationCeilInSeconds
        self.CameraMoverTargetClient = CameraMoverTargetClient
        self.World3D = World3D
        self.SituationAwarenessNextEventCommandName = SituationAwarenessNextEventCommandName
        self.MinAltitudeInMeter = MinAltitudeInMeter
        self.MaxAltitudeInMeter = MaxAltitudeInMeter

    def __repr__(self):
        return f'<TDescriptorPositionEvents ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MaxEventCount', 'EventsDurationInSeconds', 'TriggNextEventDurationCeilInSeconds', 'CameraMoverTargetClient', 'World3D', 'SituationAwarenessNextEventCommandName', 'MinAltitudeInMeter', 'MaxAltitudeInMeter']]) + '>'


class TGroupSelectionReminderResources:
    def __init__(self, UserInputLayer=None, EpsilonTimeForDoubleClic=None, PositionEventManager=None, MergeUnitsMapping=None):
        self.UserInputLayer = UserInputLayer
        self.EpsilonTimeForDoubleClic = EpsilonTimeForDoubleClic
        self.PositionEventManager = PositionEventManager
        self.MergeUnitsMapping = MergeUnitsMapping

    def __repr__(self):
        return f'<TGroupSelectionReminderResources ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['UserInputLayer', 'EpsilonTimeForDoubleClic', 'PositionEventManager', 'MergeUnitsMapping']]) + '>'


class TemplateSoundDescriptor:
    def __init__(self, FileName=None):
        self.FileName = FileName

    def __repr__(self):
        return f'<TemplateSoundDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['FileName']]) + '>'


class TMouseCursorAnimation:
    def __init__(self, AnimationCycleTime=None, TextureList=None, IgnoreContent=None, HotSpotX=None, HotSpotY=None):
        self.AnimationCycleTime = AnimationCycleTime
        self.TextureList = TextureList
        self.IgnoreContent = IgnoreContent
        self.HotSpotX = HotSpotX
        self.HotSpotY = HotSpotY

    def __repr__(self):
        return f'<TMouseCursorAnimation ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['AnimationCycleTime', 'TextureList', 'IgnoreContent', 'HotSpotX', 'HotSpotY']]) + '>'


class TResourceDescriptorTextureAnimation:
    def __init__(self, FileNameList=None):
        self.FileNameList = FileNameList

    def __repr__(self):
        return f'<TResourceDescriptorTextureAnimation ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['FileNameList']]) + '>'


class TSelectionHandlerInGameResources:
    def __init__(self, RenderToolbox=None, DrawingParameters=None, UserInputLayer=None, UserInputLayer_SquareSelection=None, Camera=None, World=None, DebugSelection=None, SceneReferenceForSelection=None, UpdateDynamicValuesCommandName=None, UseStickySelection=None, UseInvertedHotkeysForUniformSelection=None, KeyboardPresetUpdater=None, SquareSelectionActive=None):
        self.RenderToolbox = RenderToolbox
        self.DrawingParameters = DrawingParameters
        self.UserInputLayer = UserInputLayer
        self.UserInputLayer_SquareSelection = UserInputLayer_SquareSelection
        self.Camera = Camera
        self.World = World
        self.DebugSelection = DebugSelection
        self.SceneReferenceForSelection = SceneReferenceForSelection
        self.UpdateDynamicValuesCommandName = UpdateDynamicValuesCommandName
        self.UseStickySelection = UseStickySelection
        self.UseInvertedHotkeysForUniformSelection = UseInvertedHotkeysForUniformSelection
        self.KeyboardPresetUpdater = KeyboardPresetUpdater
        self.SquareSelectionActive = SquareSelectionActive

    def __repr__(self):
        return f'<TSelectionHandlerInGameResources ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['RenderToolbox', 'DrawingParameters', 'UserInputLayer', 'UserInputLayer_SquareSelection', 'Camera', 'World', 'DebugSelection', 'SceneReferenceForSelection', 'UpdateDynamicValuesCommandName', 'UseStickySelection', 'UseInvertedHotkeysForUniformSelection', 'KeyboardPresetUpdater', 'SquareSelectionActive']]) + '>'


class TSmartChipListDescription:
    def __init__(self, ParagraphStyle=None, TextStyle=None, TypefaceToken=None, TextDico=None, TextSize=None, TextFormatScript=None, SmartOrderTextColor=None, SmartGroupTextColor=None, SmartOrderBackgroundColorToken=None, SmartGroupBackgroundColorToken=None, MagnifiableChipSize=None):
        self.ParagraphStyle = ParagraphStyle
        self.TextStyle = TextStyle
        self.TypefaceToken = TypefaceToken
        self.TextDico = TextDico
        self.TextSize = TextSize
        self.TextFormatScript = TextFormatScript
        self.SmartOrderTextColor = SmartOrderTextColor
        self.SmartGroupTextColor = SmartGroupTextColor
        self.SmartOrderBackgroundColorToken = SmartOrderBackgroundColorToken
        self.SmartGroupBackgroundColorToken = SmartGroupBackgroundColorToken
        self.MagnifiableChipSize = MagnifiableChipSize

    def __repr__(self):
        return f'<TSmartChipListDescription ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ParagraphStyle', 'TextStyle', 'TypefaceToken', 'TextDico', 'TextSize', 'TextFormatScript', 'SmartOrderTextColor', 'SmartGroupTextColor', 'SmartOrderBackgroundColorToken', 'SmartGroupBackgroundColorToken', 'MagnifiableChipSize']]) + '>'


class TUICommonLabelResource:
    def __init__(self, Camera=None):
        self.Camera = Camera

    def __repr__(self):
        return f'<TUICommonLabelResource ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Camera']]) + '>'


class LDHintStandardComponentWithPause:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<LDHintStandardComponentWithPause>'


class LDHintStandardComponent:
    def __init__(self, TextureToken=None, TextureMagnifiableWidthHeight=None, HasButtons=None, ComponentFrame=None):
        self.TextureToken = TextureToken
        self.TextureMagnifiableWidthHeight = TextureMagnifiableWidthHeight
        self.HasButtons = HasButtons
        self.ComponentFrame = ComponentFrame

    def __repr__(self):
        return f'<LDHintStandardComponent ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TextureToken', 'TextureMagnifiableWidthHeight', 'HasButtons', 'ComponentFrame']]) + '>'


class PanelRoundedCorner:
    def __init__(self, UniqueName=None, BorderLineColorToken=None, Components=None, RoundedVertexes=None, FitStyle=None, HidePointerEvents=None, ElementName=None, BackgroundBlockColorToken=None, ComponentFrame=None, BorderThicknessToken=None, BorderLocalRenderLayer=None, HasBackground=None, BackgroundLocalRenderLayer=None, Radius=None, HasBorder=None):
        self.UniqueName = UniqueName
        self.BorderLineColorToken = BorderLineColorToken
        self.Components = Components
        self.RoundedVertexes = RoundedVertexes
        self.FitStyle = FitStyle
        self.HidePointerEvents = HidePointerEvents
        self.ElementName = ElementName
        self.BackgroundBlockColorToken = BackgroundBlockColorToken
        self.ComponentFrame = ComponentFrame
        self.BorderThicknessToken = BorderThicknessToken
        self.BorderLocalRenderLayer = BorderLocalRenderLayer
        self.HasBackground = HasBackground
        self.BackgroundLocalRenderLayer = BackgroundLocalRenderLayer
        self.Radius = Radius
        self.HasBorder = HasBorder

    def __repr__(self):
        return f'<PanelRoundedCorner ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['UniqueName', 'BorderLineColorToken', 'Components', 'RoundedVertexes', 'FitStyle', 'HidePointerEvents', 'ElementName', 'BackgroundBlockColorToken', 'ComponentFrame', 'BorderThicknessToken', 'BorderLocalRenderLayer', 'HasBackground', 'BackgroundLocalRenderLayer', 'Radius', 'HasBorder']]) + '>'


class BUCKTextDescriptor:
    def __init__(self, UniqueName=None, ChildFitToContent=None, BorderLineColorToken=None, Components=None, BigLineAction=None, TextToken=None, TextDico=None, HorizontalFitStyle=None, BackgroundBlockColorToken=None, Hint=None, ComponentFrame=None, BorderThicknessToken=None, TextPadding=None, TextFormatScript=None, ParagraphStyle=None, TextStyle=None, Rotation=None, FitStyle=None, TextColor=None, ElementName=None, VerticalFitStyle=None, ClipContent=None, BordersToDraw=None, HasBackground=None, TextSize=None, TypefaceToken=None, HasBorder=None):
        self.UniqueName = UniqueName
        self.ChildFitToContent = ChildFitToContent
        self.BorderLineColorToken = BorderLineColorToken
        self.Components = Components
        self.BigLineAction = BigLineAction
        self.TextToken = TextToken
        self.TextDico = TextDico
        self.HorizontalFitStyle = HorizontalFitStyle
        self.BackgroundBlockColorToken = BackgroundBlockColorToken
        self.Hint = Hint
        self.ComponentFrame = ComponentFrame
        self.BorderThicknessToken = BorderThicknessToken
        self.TextPadding = TextPadding
        self.TextFormatScript = TextFormatScript
        self.ParagraphStyle = ParagraphStyle
        self.TextStyle = TextStyle
        self.Rotation = Rotation
        self.FitStyle = FitStyle
        self.TextColor = TextColor
        self.ElementName = ElementName
        self.VerticalFitStyle = VerticalFitStyle
        self.ClipContent = ClipContent
        self.BordersToDraw = BordersToDraw
        self.HasBackground = HasBackground
        self.TextSize = TextSize
        self.TypefaceToken = TypefaceToken
        self.HasBorder = HasBorder

    def __repr__(self):
        return f'<BUCKTextDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['UniqueName', 'ChildFitToContent', 'BorderLineColorToken', 'Components', 'BigLineAction', 'TextToken', 'TextDico', 'HorizontalFitStyle', 'BackgroundBlockColorToken', 'Hint', 'ComponentFrame', 'BorderThicknessToken', 'TextPadding', 'TextFormatScript', 'ParagraphStyle', 'TextStyle', 'Rotation', 'FitStyle', 'TextColor', 'ElementName', 'VerticalFitStyle', 'ClipContent', 'BordersToDraw', 'HasBackground', 'TextSize', 'TypefaceToken', 'HasBorder']]) + '>'


class TUICommonLDHintResource:
    def __init__(self, ComponentByName=None):
        self.ComponentByName = ComponentByName

    def __repr__(self):
        return f'<TUICommonLDHintResource ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ComponentByName']]) + '>'


class BUCKVideoDescriptor:
    def __init__(self, VideoFrame=None, SoundVolume=None, HasBackground=None, Loop=None, VideoDrawer=None, ElementName=None, BackgroundBlockColorToken=None, ComponentFrame=None):
        self.VideoFrame = VideoFrame
        self.SoundVolume = SoundVolume
        self.HasBackground = HasBackground
        self.Loop = Loop
        self.VideoDrawer = VideoDrawer
        self.ElementName = ElementName
        self.BackgroundBlockColorToken = BackgroundBlockColorToken
        self.ComponentFrame = ComponentFrame

    def __repr__(self):
        return f'<BUCKVideoDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['VideoFrame', 'SoundVolume', 'HasBackground', 'Loop', 'VideoDrawer', 'ElementName', 'BackgroundBlockColorToken', 'ComponentFrame']]) + '>'


class ScenarioOverviewComponent:
    def __init__(self, ElementName=None):
        self.ElementName = ElementName

    def __repr__(self):
        return f'<ScenarioOverviewComponent ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ElementName']]) + '>'


class SpecificModalButton:
    def __init__(self, TextSizeToken=None, ButtonAlignementToFather=None, IsFilled=None, Mapping=None, TextToken=None, ButtonAlignementToAnchor=None, HintableAreaElementName=None, ElementName=None):
        self.TextSizeToken = TextSizeToken
        self.ButtonAlignementToFather = ButtonAlignementToFather
        self.IsFilled = IsFilled
        self.Mapping = Mapping
        self.TextToken = TextToken
        self.ButtonAlignementToAnchor = ButtonAlignementToAnchor
        self.HintableAreaElementName = HintableAreaElementName
        self.ElementName = ElementName

    def __repr__(self):
        return f'<SpecificModalButton ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TextSizeToken', 'ButtonAlignementToFather', 'IsFilled', 'Mapping', 'TextToken', 'ButtonAlignementToAnchor', 'HintableAreaElementName', 'ElementName']]) + '>'


class TEugBMutablePBaseClass:
    def __init__(self, Value=None):
        self.Value = Value

    def __repr__(self):
        return f'<TEugBMutablePBaseClass ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Value']]) + '>'


class TUserInputMapping:
    def __init__(self, MouseEventID=None, KeyboardEventID=None):
        self.MouseEventID = MouseEventID
        self.KeyboardEventID = KeyboardEventID

    def __repr__(self):
        return f'<TUserInputMapping ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MouseEventID', 'KeyboardEventID']]) + '>'


class BUCKTextureDescriptor:
    def __init__(self, ClipTextureToComponent=None, Rotation=None, Components=None, TextureToken=None, ResizeMode=None, TextureColorToken=None, HasBackground=None, HidePointerEvents=None, TextureFrame=None, ElementName=None, TileTextureInComponent=None, BackgroundBlockColorToken=None, TextureDrawer=None, ComponentFrame=None):
        self.ClipTextureToComponent = ClipTextureToComponent
        self.Rotation = Rotation
        self.Components = Components
        self.TextureToken = TextureToken
        self.ResizeMode = ResizeMode
        self.TextureColorToken = TextureColorToken
        self.HasBackground = HasBackground
        self.HidePointerEvents = HidePointerEvents
        self.TextureFrame = TextureFrame
        self.ElementName = ElementName
        self.TileTextureInComponent = TileTextureInComponent
        self.BackgroundBlockColorToken = BackgroundBlockColorToken
        self.TextureDrawer = TextureDrawer
        self.ComponentFrame = ComponentFrame

    def __repr__(self):
        return f'<BUCKTextureDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ClipTextureToComponent', 'Rotation', 'Components', 'TextureToken', 'ResizeMode', 'TextureColorToken', 'HasBackground', 'HidePointerEvents', 'TextureFrame', 'ElementName', 'TileTextureInComponent', 'BackgroundBlockColorToken', 'TextureDrawer', 'ComponentFrame']]) + '>'


class TUISpecificScenarioMapOverviewViewDescriptor:
    def __init__(self, MainComponentDescriptor=None, MainComponentContainerUniqueName=None):
        self.MainComponentDescriptor = MainComponentDescriptor
        self.MainComponentContainerUniqueName = MainComponentContainerUniqueName

    def __repr__(self):
        return f'<TUISpecificScenarioMapOverviewViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentDescriptor', 'MainComponentContainerUniqueName']]) + '>'


class TUISpecificCountryInfos:
    def __init__(self, NameToken=None, Country=None, FlagTexture=None, PawnExpTexture=None):
        self.NameToken = NameToken
        self.Country = Country
        self.FlagTexture = FlagTexture
        self.PawnExpTexture = PawnExpTexture

    def __repr__(self):
        return f'<TUISpecificCountryInfos ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['NameToken', 'Country', 'FlagTexture', 'PawnExpTexture']]) + '>'


class TUISpecificCountriesInfos:
    def __init__(self, CountriesInfos=None):
        self.CountriesInfos = CountriesInfos

    def __repr__(self):
        return f'<TUISpecificCountriesInfos ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['CountriesInfos']]) + '>'


class WarningStandardComponent:
    def __init__(self, BorderLineColorToken=None, TextColor=None, TypefaceToken=None, VerticalOffset=None, BackgroundBlockColorToken=None):
        self.BorderLineColorToken = BorderLineColorToken
        self.TextColor = TextColor
        self.TypefaceToken = TypefaceToken
        self.VerticalOffset = VerticalOffset
        self.BackgroundBlockColorToken = BackgroundBlockColorToken

    def __repr__(self):
        return f'<WarningStandardComponent ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['BorderLineColorToken', 'TextColor', 'TypefaceToken', 'VerticalOffset', 'BackgroundBlockColorToken']]) + '>'


class TEnumAlertMessageType:
    def __init__(self, Values=None):
        self.Values = Values

    def __repr__(self):
        return f'<TEnumAlertMessageType ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Values']]) + '>'


class TDispatchedMessageType:
    def __init__(self, Values=None):
        self.Values = Values

    def __repr__(self):
        return f'<TDispatchedMessageType ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Values']]) + '>'


class TEnumObjectiveMessageType:
    def __init__(self, Values=None):
        self.Values = Values

    def __repr__(self):
        return f'<TEnumObjectiveMessageType ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Values']]) + '>'


class TRTTILength4:
    def __init__(self, Magnifiable=None):
        self.Magnifiable = Magnifiable

    def __repr__(self):
        return f'<TRTTILength4 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Magnifiable']]) + '>'


class HintTitleTextBUCKComponent:
    def __init__(self, ComponentFrame=None, ParagraphStyle=None, HorizontalFitStyle=None, TextPadding=None, TypefaceToken=None, BigLineAction=None, TextDico=None, TextSize=None, TextColor=None):
        self.ComponentFrame = ComponentFrame
        self.ParagraphStyle = ParagraphStyle
        self.HorizontalFitStyle = HorizontalFitStyle
        self.TextPadding = TextPadding
        self.TypefaceToken = TypefaceToken
        self.BigLineAction = BigLineAction
        self.TextDico = TextDico
        self.TextSize = TextSize
        self.TextColor = TextColor

    def __repr__(self):
        return f'<HintTitleTextBUCKComponent ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ComponentFrame', 'ParagraphStyle', 'HorizontalFitStyle', 'TextPadding', 'TypefaceToken', 'BigLineAction', 'TextDico', 'TextSize', 'TextColor']]) + '>'


class HintBodyTextBUCKComponent:
    def __init__(self, ComponentFrame=None, ParagraphStyle=None, TextPadding=None, HorizontalFitStyle=None, TypefaceToken=None, BigLineAction=None, TextDico=None, TextSize=None, TextColor=None):
        self.ComponentFrame = ComponentFrame
        self.ParagraphStyle = ParagraphStyle
        self.TextPadding = TextPadding
        self.HorizontalFitStyle = HorizontalFitStyle
        self.TypefaceToken = TypefaceToken
        self.BigLineAction = BigLineAction
        self.TextDico = TextDico
        self.TextSize = TextSize
        self.TextColor = TextColor

    def __repr__(self):
        return f'<HintBodyTextBUCKComponent ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ComponentFrame', 'ParagraphStyle', 'TextPadding', 'HorizontalFitStyle', 'TypefaceToken', 'BigLineAction', 'TextDico', 'TextSize', 'TextColor']]) + '>'


class TCommandementZoneResources:
    def __init__(self, Camera=None, WorldFloorProxy=None, LabelPositionOffset=None):
        self.Camera = Camera
        self.WorldFloorProxy = WorldFloorProxy
        self.LabelPositionOffset = LabelPositionOffset

    def __repr__(self):
        return f'<TCommandementZoneResources ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Camera', 'WorldFloorProxy', 'LabelPositionOffset']]) + '>'


class TUITacticalGameRulesHelper:
    def __init__(self, TimeStepMessage=None, TimeInMinutesStepList=None, SuddenDeathTokens=None, StandardStepMessages=None, AttackingAllianceStepMessages=None, DefendingAllianceStepMessages=None, TimeToShowStepMessageInSecond=None, ComponentToUseForSuddenDeathMessage=None, ComponentToUseForRemainingTimeMessage=None, ComponentToUseForLocalPlayerAllianceMessage=None, ComponentToUseForOtherAllianceMessage=None, LDHintTextComponentNameToFill=None, LDHintMoralDico=None, LDHintMoralTokenLocalPlayerAlliance=None, LDHintMoralTokenEnemyAlliance=None, LDHintMoralDuration=None, LDHintMoralThreshold=None, LDHintComponentForLocalPlayerAlliance=None, LDHintComponentForEnemyAlliance=None):
        self.TimeStepMessage = TimeStepMessage
        self.TimeInMinutesStepList = TimeInMinutesStepList
        self.SuddenDeathTokens = SuddenDeathTokens
        self.StandardStepMessages = StandardStepMessages
        self.AttackingAllianceStepMessages = AttackingAllianceStepMessages
        self.DefendingAllianceStepMessages = DefendingAllianceStepMessages
        self.TimeToShowStepMessageInSecond = TimeToShowStepMessageInSecond
        self.ComponentToUseForSuddenDeathMessage = ComponentToUseForSuddenDeathMessage
        self.ComponentToUseForRemainingTimeMessage = ComponentToUseForRemainingTimeMessage
        self.ComponentToUseForLocalPlayerAllianceMessage = ComponentToUseForLocalPlayerAllianceMessage
        self.ComponentToUseForOtherAllianceMessage = ComponentToUseForOtherAllianceMessage
        self.LDHintTextComponentNameToFill = LDHintTextComponentNameToFill
        self.LDHintMoralDico = LDHintMoralDico
        self.LDHintMoralTokenLocalPlayerAlliance = LDHintMoralTokenLocalPlayerAlliance
        self.LDHintMoralTokenEnemyAlliance = LDHintMoralTokenEnemyAlliance
        self.LDHintMoralDuration = LDHintMoralDuration
        self.LDHintMoralThreshold = LDHintMoralThreshold
        self.LDHintComponentForLocalPlayerAlliance = LDHintComponentForLocalPlayerAlliance
        self.LDHintComponentForEnemyAlliance = LDHintComponentForEnemyAlliance

    def __repr__(self):
        return f'<TUITacticalGameRulesHelper ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TimeStepMessage', 'TimeInMinutesStepList', 'SuddenDeathTokens', 'StandardStepMessages', 'AttackingAllianceStepMessages', 'DefendingAllianceStepMessages', 'TimeToShowStepMessageInSecond', 'ComponentToUseForSuddenDeathMessage', 'ComponentToUseForRemainingTimeMessage', 'ComponentToUseForLocalPlayerAllianceMessage', 'ComponentToUseForOtherAllianceMessage', 'LDHintTextComponentNameToFill', 'LDHintMoralDico', 'LDHintMoralTokenLocalPlayerAlliance', 'LDHintMoralTokenEnemyAlliance', 'LDHintMoralDuration', 'LDHintMoralThreshold', 'LDHintComponentForLocalPlayerAlliance', 'LDHintComponentForEnemyAlliance']]) + '>'


class TUITacticalGameRulesHelperStepMessages:
    def __init__(self, LocalPlayerAllianceScoreByGameMode=None, OtherAllianceScoreByGameMode=None, AreDecreasingSteps=None):
        self.LocalPlayerAllianceScoreByGameMode = LocalPlayerAllianceScoreByGameMode
        self.OtherAllianceScoreByGameMode = OtherAllianceScoreByGameMode
        self.AreDecreasingSteps = AreDecreasingSteps

    def __repr__(self):
        return f'<TUITacticalGameRulesHelperStepMessages ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['LocalPlayerAllianceScoreByGameMode', 'OtherAllianceScoreByGameMode', 'AreDecreasingSteps']]) + '>'


class TOrderDisplayDrawer:
    def __init__(self, OrderDisplayDrawInfos=None, DefaultOrderDisplayDrawInfo=None, AltitudeMinToDrawDashLine=None, WorldFloorProxy=None):
        self.OrderDisplayDrawInfos = OrderDisplayDrawInfos
        self.DefaultOrderDisplayDrawInfo = DefaultOrderDisplayDrawInfo
        self.AltitudeMinToDrawDashLine = AltitudeMinToDrawDashLine
        self.WorldFloorProxy = WorldFloorProxy

    def __repr__(self):
        return f'<TOrderDisplayDrawer ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['OrderDisplayDrawInfos', 'DefaultOrderDisplayDrawInfo', 'AltitudeMinToDrawDashLine', 'WorldFloorProxy']]) + '>'


class TOrderDisplayDrawInfo:
    def __init__(self, MustDrawCircleStart=None, ColorLineStart=None, ColorCircleDestination=None, AerialDashLineBaseCircleRadius=None, AerialDashLineDrawCircleAtBase=None, ColorLineEnd=None, DisplayWaypoints=None, AerialDashLineDashLength=None, ColorCircleStart=None, CircleStartThickness=None, CircleDestinationRadius=None, MustDrawDashLineForAerialOrderDestination=None, DashLengthInMeters=None, CircleDestinationThickness=None, MaxDistanceBetweenColorsGRU=None, OrderToken=None, LineThickness=None, MustDrawCircle=None, Hatched=None, MustDrawArrow=None, AerialDashLineThickness=None, AerialDashLineBaseCircleThickness=None, ReverseArrow=None, HideNextOrders=None):
        self.MustDrawCircleStart = MustDrawCircleStart
        self.ColorLineStart = ColorLineStart
        self.ColorCircleDestination = ColorCircleDestination
        self.AerialDashLineBaseCircleRadius = AerialDashLineBaseCircleRadius
        self.AerialDashLineDrawCircleAtBase = AerialDashLineDrawCircleAtBase
        self.ColorLineEnd = ColorLineEnd
        self.DisplayWaypoints = DisplayWaypoints
        self.AerialDashLineDashLength = AerialDashLineDashLength
        self.ColorCircleStart = ColorCircleStart
        self.CircleStartThickness = CircleStartThickness
        self.CircleDestinationRadius = CircleDestinationRadius
        self.MustDrawDashLineForAerialOrderDestination = MustDrawDashLineForAerialOrderDestination
        self.DashLengthInMeters = DashLengthInMeters
        self.CircleDestinationThickness = CircleDestinationThickness
        self.MaxDistanceBetweenColorsGRU = MaxDistanceBetweenColorsGRU
        self.OrderToken = OrderToken
        self.LineThickness = LineThickness
        self.MustDrawCircle = MustDrawCircle
        self.Hatched = Hatched
        self.MustDrawArrow = MustDrawArrow
        self.AerialDashLineThickness = AerialDashLineThickness
        self.AerialDashLineBaseCircleThickness = AerialDashLineBaseCircleThickness
        self.ReverseArrow = ReverseArrow
        self.HideNextOrders = HideNextOrders

    def __repr__(self):
        return f'<TOrderDisplayDrawInfo ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MustDrawCircleStart', 'ColorLineStart', 'ColorCircleDestination', 'AerialDashLineBaseCircleRadius', 'AerialDashLineDrawCircleAtBase', 'ColorLineEnd', 'DisplayWaypoints', 'AerialDashLineDashLength', 'ColorCircleStart', 'CircleStartThickness', 'CircleDestinationRadius', 'MustDrawDashLineForAerialOrderDestination', 'DashLengthInMeters', 'CircleDestinationThickness', 'MaxDistanceBetweenColorsGRU', 'OrderToken', 'LineThickness', 'MustDrawCircle', 'Hatched', 'MustDrawArrow', 'AerialDashLineThickness', 'AerialDashLineBaseCircleThickness', 'ReverseArrow', 'HideNextOrders']]) + '>'


class TTacticOrderDisplayResources:
    def __init__(self, Camera=None, OrderDisplayUserInputLayer=None, OrderDisplayDrawer=None, AlwaysShowOrderButtonAlsoShowsSmartOrders=None, StartFadeAlphaAfterTimeInSeconds=None, AlphaFadeDurationInSeconds=None, SubSelectionAlphaFadeMultiplier=None, CameraMoverHelperProxy=None, FadeHeightTransitionStart=None, FadeHeightTransitionEnd=None, InstantOrdersThatNeedFakeFeedback=None):
        self.Camera = Camera
        self.OrderDisplayUserInputLayer = OrderDisplayUserInputLayer
        self.OrderDisplayDrawer = OrderDisplayDrawer
        self.AlwaysShowOrderButtonAlsoShowsSmartOrders = AlwaysShowOrderButtonAlsoShowsSmartOrders
        self.StartFadeAlphaAfterTimeInSeconds = StartFadeAlphaAfterTimeInSeconds
        self.AlphaFadeDurationInSeconds = AlphaFadeDurationInSeconds
        self.SubSelectionAlphaFadeMultiplier = SubSelectionAlphaFadeMultiplier
        self.CameraMoverHelperProxy = CameraMoverHelperProxy
        self.FadeHeightTransitionStart = FadeHeightTransitionStart
        self.FadeHeightTransitionEnd = FadeHeightTransitionEnd
        self.InstantOrdersThatNeedFakeFeedback = InstantOrdersThatNeedFakeFeedback

    def __repr__(self):
        return f'<TTacticOrderDisplayResources ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Camera', 'OrderDisplayUserInputLayer', 'OrderDisplayDrawer', 'AlwaysShowOrderButtonAlsoShowsSmartOrders', 'StartFadeAlphaAfterTimeInSeconds', 'AlphaFadeDurationInSeconds', 'SubSelectionAlphaFadeMultiplier', 'CameraMoverHelperProxy', 'FadeHeightTransitionStart', 'FadeHeightTransitionEnd', 'InstantOrdersThatNeedFakeFeedback']]) + '>'


class TUIFeedbackDispatchedMessageDescriptor:
    def __init__(self, AllowFocusOnEvent=None, MinimapPingAnimType=None, TextFormatter=None, IsActiveForEnemies=None, MinimapPingType=None, MinimapPingDuration=None, MinimapPingAnimStartTime=None, IsActiveForAllies=None, IsActiveOnlyOnSelectedUnits=None, IsActiveForPlayer=None, BaseFilterColorForMinimap=None, AlertMessageType=None, IsActiveForSpectator=None, TimeBeforeRepeat=None, LabelDescriptor=None, UnitAcknow=None, HudSound=None):
        self.AllowFocusOnEvent = AllowFocusOnEvent
        self.MinimapPingAnimType = MinimapPingAnimType
        self.TextFormatter = TextFormatter
        self.IsActiveForEnemies = IsActiveForEnemies
        self.MinimapPingType = MinimapPingType
        self.MinimapPingDuration = MinimapPingDuration
        self.MinimapPingAnimStartTime = MinimapPingAnimStartTime
        self.IsActiveForAllies = IsActiveForAllies
        self.IsActiveOnlyOnSelectedUnits = IsActiveOnlyOnSelectedUnits
        self.IsActiveForPlayer = IsActiveForPlayer
        self.BaseFilterColorForMinimap = BaseFilterColorForMinimap
        self.AlertMessageType = AlertMessageType
        self.IsActiveForSpectator = IsActiveForSpectator
        self.TimeBeforeRepeat = TimeBeforeRepeat
        self.LabelDescriptor = LabelDescriptor
        self.UnitAcknow = UnitAcknow
        self.HudSound = HudSound

    def __repr__(self):
        return f'<TUIFeedbackDispatchedMessageDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['AllowFocusOnEvent', 'MinimapPingAnimType', 'TextFormatter', 'IsActiveForEnemies', 'MinimapPingType', 'MinimapPingDuration', 'MinimapPingAnimStartTime', 'IsActiveForAllies', 'IsActiveOnlyOnSelectedUnits', 'IsActiveForPlayer', 'BaseFilterColorForMinimap', 'AlertMessageType', 'IsActiveForSpectator', 'TimeBeforeRepeat', 'LabelDescriptor', 'UnitAcknow', 'HudSound']]) + '>'


class TFeedback2DLabelDescriptor:
    def __init__(self, FadeOutTime=None, InitialOffset=None, FadeInTime=None, UILayer=None, Camera=None, FinalOffset=None, TotalTime=None, ComponentDescriptor=None):
        self.FadeOutTime = FadeOutTime
        self.InitialOffset = InitialOffset
        self.FadeInTime = FadeInTime
        self.UILayer = UILayer
        self.Camera = Camera
        self.FinalOffset = FinalOffset
        self.TotalTime = TotalTime
        self.ComponentDescriptor = ComponentDescriptor

    def __repr__(self):
        return f'<TFeedback2DLabelDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['FadeOutTime', 'InitialOffset', 'FadeInTime', 'UILayer', 'Camera', 'FinalOffset', 'TotalTime', 'ComponentDescriptor']]) + '>'


class TUIFeedbackTextFormatterWithToken:
    def __init__(self, Dico=None, Token=None):
        self.Dico = Dico
        self.Token = Token

    def __repr__(self):
        return f'<TUIFeedbackTextFormatterWithToken ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Dico', 'Token']]) + '>'


class TUIFeedbackTextFormatterUseOptionalParamAsToken:
    def __init__(self, Dico=None):
        self.Dico = Dico

    def __repr__(self):
        return f'<TUIFeedbackTextFormatterUseOptionalParamAsToken ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Dico']]) + '>'


class TUISpecificInGameFeedbackMessageManagerDescriptor:
    def __init__(self, MessagesByType=None, Minimap_TimeBetweenPings=None):
        self.MessagesByType = MessagesByType
        self.Minimap_TimeBetweenPings = Minimap_TimeBetweenPings

    def __repr__(self):
        return f'<TUISpecificInGameFeedbackMessageManagerDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MessagesByType', 'Minimap_TimeBetweenPings']]) + '>'


class TInGameCorrectedShotFeedbackRessources:
    def __init__(self, Color=None, BorderThickness=None):
        self.Color = Color
        self.BorderThickness = BorderThickness

    def __repr__(self):
        return f'<TInGameCorrectedShotFeedbackRessources ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Color', 'BorderThickness']]) + '>'


class TUICommonExperienceTexturesResources:
    def __init__(self, ExpTextures=None):
        self.ExpTextures = ExpTextures

    def __repr__(self):
        return f'<TUICommonExperienceTexturesResources ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ExpTextures']]) + '>'


class FlareCustomEditableText:
    def __init__(self, IsFromStrategic=None):
        self.IsFromStrategic = IsFromStrategic

    def __repr__(self):
        return f'<FlareCustomEditableText ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['IsFromStrategic']]) + '>'


class FlareButtonNeedHelp:
    def __init__(self, IsFromStrategic=None):
        self.IsFromStrategic = IsFromStrategic

    def __repr__(self):
        return f'<FlareButtonNeedHelp ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['IsFromStrategic']]) + '>'


class FlareButtonStrategyAttack:
    def __init__(self, IsFromStrategic=None):
        self.IsFromStrategic = IsFromStrategic

    def __repr__(self):
        return f'<FlareButtonStrategyAttack ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['IsFromStrategic']]) + '>'


class FlareButtonStrategyDefend:
    def __init__(self, IsFromStrategic=None):
        self.IsFromStrategic = IsFromStrategic

    def __repr__(self):
        return f'<FlareButtonStrategyDefend ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['IsFromStrategic']]) + '>'


class FlareButtonSupport:
    def __init__(self, IsFromStrategic=None):
        self.IsFromStrategic = IsFromStrategic

    def __repr__(self):
        return f'<FlareButtonSupport ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['IsFromStrategic']]) + '>'


class FlareButtonEnemySpotted:
    def __init__(self, IsFromStrategic=None):
        self.IsFromStrategic = IsFromStrategic

    def __repr__(self):
        return f'<FlareButtonEnemySpotted ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['IsFromStrategic']]) + '>'


class FlareButtonCustom:
    def __init__(self, IsFromStrategic=None):
        self.IsFromStrategic = IsFromStrategic

    def __repr__(self):
        return f'<FlareButtonCustom ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['IsFromStrategic']]) + '>'


class TUIInGameFlarePanelViewDescriptor:
    def __init__(self, MainComponentContainerUniqueName=None, MainComponentDescriptor=None):
        self.MainComponentContainerUniqueName = MainComponentContainerUniqueName
        self.MainComponentDescriptor = MainComponentDescriptor

    def __repr__(self):
        return f'<TUIInGameFlarePanelViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentContainerUniqueName', 'MainComponentDescriptor']]) + '>'


class TUISpecificInGameReplayResource:
    def __init__(self, HideUIKeyInterceptor=None, HideRenderLayers=None, VideoModeValue=None, Component=None, ComponentWaitingForModeObs=None):
        self.HideUIKeyInterceptor = HideUIKeyInterceptor
        self.HideRenderLayers = HideRenderLayers
        self.VideoModeValue = VideoModeValue
        self.Component = Component
        self.ComponentWaitingForModeObs = ComponentWaitingForModeObs

    def __repr__(self):
        return f'<TUISpecificInGameReplayResource ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['HideUIKeyInterceptor', 'HideRenderLayers', 'VideoModeValue', 'Component', 'ComponentWaitingForModeObs']]) + '>'


class BUCKGaugeDescriptor:
    def __init__(self, DurationForGaugeFullChange=None, BorderLineColorToken=None, GraduationColorToken=None, Components=None, GaugeMax=None, GaugeValueMinSize=None, GraduationStep=None, ElementName=None, GaugeComponentNames=None, BackgroundBlockColorToken=None, ComponentFrame=None, BorderThicknessToken=None, GraduationThicknessToken=None, GridAlign=None, HasBackground=None, HasBorder=None):
        self.DurationForGaugeFullChange = DurationForGaugeFullChange
        self.BorderLineColorToken = BorderLineColorToken
        self.GraduationColorToken = GraduationColorToken
        self.Components = Components
        self.GaugeMax = GaugeMax
        self.GaugeValueMinSize = GaugeValueMinSize
        self.GraduationStep = GraduationStep
        self.ElementName = ElementName
        self.GaugeComponentNames = GaugeComponentNames
        self.BackgroundBlockColorToken = BackgroundBlockColorToken
        self.ComponentFrame = ComponentFrame
        self.BorderThicknessToken = BorderThicknessToken
        self.GraduationThicknessToken = GraduationThicknessToken
        self.GridAlign = GridAlign
        self.HasBackground = HasBackground
        self.HasBorder = HasBorder

    def __repr__(self):
        return f'<BUCKGaugeDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['DurationForGaugeFullChange', 'BorderLineColorToken', 'GraduationColorToken', 'Components', 'GaugeMax', 'GaugeValueMinSize', 'GraduationStep', 'ElementName', 'GaugeComponentNames', 'BackgroundBlockColorToken', 'ComponentFrame', 'BorderThicknessToken', 'GraduationThicknessToken', 'GridAlign', 'HasBackground', 'HasBorder']]) + '>'


class BUCKGaugeValueDescriptor:
    def __init__(self, BorderThicknessToken=None, BorderLineColorToken=None, Components=None, HasBackground=None, ElementName=None, HasBorder=None, BackgroundBlockColorToken=None, ComponentFrame=None):
        self.BorderThicknessToken = BorderThicknessToken
        self.BorderLineColorToken = BorderLineColorToken
        self.Components = Components
        self.HasBackground = HasBackground
        self.ElementName = ElementName
        self.HasBorder = HasBorder
        self.BackgroundBlockColorToken = BackgroundBlockColorToken
        self.ComponentFrame = ComponentFrame

    def __repr__(self):
        return f'<BUCKGaugeValueDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['BorderThicknessToken', 'BorderLineColorToken', 'Components', 'HasBackground', 'ElementName', 'HasBorder', 'BackgroundBlockColorToken', 'ComponentFrame']]) + '>'


class TUISpecificInGameHUDResource:
    def __init__(self, MinimapResources=None, HUDReplayResource=None, HUDAlertPanelDescriptor=None, CameraMoverTargetClient=None, PerformanceAlertViewDescriptor=None, ShowUnitInfosMapping=None, TurnOffWeaponsMapping=None, DisplayAllOrdersMapping=None, OrderDisplayResources=None, SelectionPanelDescriptor=None, SelectionWeaponPanelDescriptor=None, SelectionRoeDescriptor=None, MiniMapInfoViewDescriptor=None, ShortcutsForSelectionViewDescriptor=None, PhasePanelElementNames=None):
        self.MinimapResources = MinimapResources
        self.HUDReplayResource = HUDReplayResource
        self.HUDAlertPanelDescriptor = HUDAlertPanelDescriptor
        self.CameraMoverTargetClient = CameraMoverTargetClient
        self.PerformanceAlertViewDescriptor = PerformanceAlertViewDescriptor
        self.ShowUnitInfosMapping = ShowUnitInfosMapping
        self.TurnOffWeaponsMapping = TurnOffWeaponsMapping
        self.DisplayAllOrdersMapping = DisplayAllOrdersMapping
        self.OrderDisplayResources = OrderDisplayResources
        self.SelectionPanelDescriptor = SelectionPanelDescriptor
        self.SelectionWeaponPanelDescriptor = SelectionWeaponPanelDescriptor
        self.SelectionRoeDescriptor = SelectionRoeDescriptor
        self.MiniMapInfoViewDescriptor = MiniMapInfoViewDescriptor
        self.ShortcutsForSelectionViewDescriptor = ShortcutsForSelectionViewDescriptor
        self.PhasePanelElementNames = PhasePanelElementNames

    def __repr__(self):
        return f'<TUISpecificInGameHUDResource ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MinimapResources', 'HUDReplayResource', 'HUDAlertPanelDescriptor', 'CameraMoverTargetClient', 'PerformanceAlertViewDescriptor', 'ShowUnitInfosMapping', 'TurnOffWeaponsMapping', 'DisplayAllOrdersMapping', 'OrderDisplayResources', 'SelectionPanelDescriptor', 'SelectionWeaponPanelDescriptor', 'SelectionRoeDescriptor', 'MiniMapInfoViewDescriptor', 'ShortcutsForSelectionViewDescriptor', 'PhasePanelElementNames']]) + '>'


class LDHintInfoIngameScore:
    def __init__(self, FeedbackType=None):
        self.FeedbackType = FeedbackType

    def __repr__(self):
        return f'<LDHintInfoIngameScore ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['FeedbackType']]) + '>'


class SuperHint:
    def __init__(self, alignementGauche=None, challenge=None):
        self.alignementGauche = alignementGauche
        self.challenge = challenge

    def __repr__(self):
        return f'<SuperHint ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['alignementGauche', 'challenge']]) + '>'


class LDHint_cutscene_10:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<LDHint_cutscene_10>'


class CutscenePanoramique:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<CutscenePanoramique>'


class Component_1Video_1Text:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<Component_1Video_1Text>'


class Component_1Texture_1Text:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<Component_1Texture_1Text>'


class Component_1Texture_1Text_Portrait:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<Component_1Texture_1Text_Portrait>'


class Component_1Texture_1Text_TextureLeft:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<Component_1Texture_1Text_TextureLeft>'


class Component_Operation_1Texture_1Text:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<Component_Operation_1Texture_1Text>'


class Component_1Text_hint:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<Component_1Text_hint>'


class Component_1Text:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<Component_1Text>'


class Component_1Text_FullScreen:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<Component_1Text_FullScreen>'


class Component_1_Texture_1Text_FullScreen:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<Component_1_Texture_1Text_FullScreen>'


class TitreChallenge:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TitreChallenge>'


class TUICommonLDVideoViewDescriptor:
    def __init__(self, MainComponentContainerUniqueName=None, ShowSubtitles=None, VideoLoadingPriority=None, Components=None, MainComponentDescriptor=None, SkipVideoOption=None):
        self.MainComponentContainerUniqueName = MainComponentContainerUniqueName
        self.ShowSubtitles = ShowSubtitles
        self.VideoLoadingPriority = VideoLoadingPriority
        self.Components = Components
        self.MainComponentDescriptor = MainComponentDescriptor
        self.SkipVideoOption = SkipVideoOption

    def __repr__(self):
        return f'<TUICommonLDVideoViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentContainerUniqueName', 'ShowSubtitles', 'VideoLoadingPriority', 'Components', 'MainComponentDescriptor', 'SkipVideoOption']]) + '>'


class TMinimapPingType:
    def __init__(self, Values=None):
        self.Values = Values

    def __repr__(self):
        return f'<TMinimapPingType ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Values']]) + '>'


class TMinimapPingAnimType:
    def __init__(self, Values=None):
        self.Values = Values

    def __repr__(self):
        return f'<TMinimapPingAnimType ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Values']]) + '>'


class TUISpecificBUCKMinimapDescriptor:
    def __init__(self, ElementName=None, ComponentFrame=None, UniformDrawer=None, IsClippable=None):
        self.ElementName = ElementName
        self.ComponentFrame = ComponentFrame
        self.UniformDrawer = UniformDrawer
        self.IsClippable = IsClippable

    def __repr__(self):
        return f'<TUISpecificBUCKMinimapDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ElementName', 'ComponentFrame', 'UniformDrawer', 'IsClippable']]) + '>'


class TUISpecificInGameMinimapResources:
    def __init__(self, WorldFloorProxy=None, CameraMoverTargetClient=None, CameraMoverHelperProxy=None, CameraAngleTexture=None, UniformAntiAliasedDrawer=None, BackgroundDrawer=None, TextureForPingType=None, UnitAppearingColor=None, UnitSelectedColor=None, UnitTakingDamageColor=None, CameraTrapezoidOriginColor=None, ScaleUnitInsideMinimap=None, ScalePingInsideMinimap=None, CommandZoneBorderWidth=None, SortOrderList=None, SortOrderInsideLayer=None, EventDuration=None, Camera=None, SeuilRotateCameraInDegree=None, DistrictColor=None):
        self.WorldFloorProxy = WorldFloorProxy
        self.CameraMoverTargetClient = CameraMoverTargetClient
        self.CameraMoverHelperProxy = CameraMoverHelperProxy
        self.CameraAngleTexture = CameraAngleTexture
        self.UniformAntiAliasedDrawer = UniformAntiAliasedDrawer
        self.BackgroundDrawer = BackgroundDrawer
        self.TextureForPingType = TextureForPingType
        self.UnitAppearingColor = UnitAppearingColor
        self.UnitSelectedColor = UnitSelectedColor
        self.UnitTakingDamageColor = UnitTakingDamageColor
        self.CameraTrapezoidOriginColor = CameraTrapezoidOriginColor
        self.ScaleUnitInsideMinimap = ScaleUnitInsideMinimap
        self.ScalePingInsideMinimap = ScalePingInsideMinimap
        self.CommandZoneBorderWidth = CommandZoneBorderWidth
        self.SortOrderList = SortOrderList
        self.SortOrderInsideLayer = SortOrderInsideLayer
        self.EventDuration = EventDuration
        self.Camera = Camera
        self.SeuilRotateCameraInDegree = SeuilRotateCameraInDegree
        self.DistrictColor = DistrictColor

    def __repr__(self):
        return f'<TUISpecificInGameMinimapResources ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['WorldFloorProxy', 'CameraMoverTargetClient', 'CameraMoverHelperProxy', 'CameraAngleTexture', 'UniformAntiAliasedDrawer', 'BackgroundDrawer', 'TextureForPingType', 'UnitAppearingColor', 'UnitSelectedColor', 'UnitTakingDamageColor', 'CameraTrapezoidOriginColor', 'ScaleUnitInsideMinimap', 'ScalePingInsideMinimap', 'CommandZoneBorderWidth', 'SortOrderList', 'SortOrderInsideLayer', 'EventDuration', 'Camera', 'SeuilRotateCameraInDegree', 'DistrictColor']]) + '>'


class TUISpecificInGameOptionsResources:
    def __init__(self, ShowUnitName=None, IconsToShow=None, LabelSize=None, StrategicLabelSize=None, MinimalistTargetCursorDisplay=None, MinimapDisplay=None, AutoCreateSmartGroup=None, HudSize=None, ProdMenuBehavior=None, LabelTacticAggregationType=None, DisplayAutoDeploy=None, CurrentComparator=None):
        self.ShowUnitName = ShowUnitName
        self.IconsToShow = IconsToShow
        self.LabelSize = LabelSize
        self.StrategicLabelSize = StrategicLabelSize
        self.MinimalistTargetCursorDisplay = MinimalistTargetCursorDisplay
        self.MinimapDisplay = MinimapDisplay
        self.AutoCreateSmartGroup = AutoCreateSmartGroup
        self.HudSize = HudSize
        self.ProdMenuBehavior = ProdMenuBehavior
        self.LabelTacticAggregationType = LabelTacticAggregationType
        self.DisplayAutoDeploy = DisplayAutoDeploy
        self.CurrentComparator = CurrentComparator

    def __repr__(self):
        return f'<TUISpecificInGameOptionsResources ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ShowUnitName', 'IconsToShow', 'LabelSize', 'StrategicLabelSize', 'MinimalistTargetCursorDisplay', 'MinimapDisplay', 'AutoCreateSmartGroup', 'HudSize', 'ProdMenuBehavior', 'LabelTacticAggregationType', 'DisplayAutoDeploy', 'CurrentComparator']]) + '>'


class BUCKSpecificHintableArea:
    def __init__(self, HintBodyToken=None, HintExtendedToken=None, ElementName=None, HintTitleToken=None, DicoToken=None):
        self.HintBodyToken = HintBodyToken
        self.HintExtendedToken = HintExtendedToken
        self.ElementName = ElementName
        self.HintTitleToken = HintTitleToken
        self.DicoToken = DicoToken

    def __repr__(self):
        return f'<BUCKSpecificHintableArea ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['HintBodyToken', 'HintExtendedToken', 'ElementName', 'HintTitleToken', 'DicoToken']]) + '>'


class TUIPathDescriptor:
    def __init__(self, Color=None, RenderLayerSelector=None, OpacityControlByFloat=None, Material=None, ArrowWidth=None, SizeMultiplierHelper=None, ArrowLength=None, Width=None, PlaqueSurLeSol=None):
        self.Color = Color
        self.RenderLayerSelector = RenderLayerSelector
        self.OpacityControlByFloat = OpacityControlByFloat
        self.Material = Material
        self.ArrowWidth = ArrowWidth
        self.SizeMultiplierHelper = SizeMultiplierHelper
        self.ArrowLength = ArrowLength
        self.Width = Width
        self.PlaqueSurLeSol = PlaqueSurLeSol

    def __repr__(self):
        return f'<TUIPathDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Color', 'RenderLayerSelector', 'OpacityControlByFloat', 'Material', 'ArrowWidth', 'SizeMultiplierHelper', 'ArrowLength', 'Width', 'PlaqueSurLeSol']]) + '>'


class TRenderLayerSelector:
    def __init__(self, RenderLayerName=None):
        self.RenderLayerName = RenderLayerName

    def __repr__(self):
        return f'<TRenderLayerSelector ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['RenderLayerName']]) + '>'


class TReinforcementResource:
    def __init__(self, LandReinforcementArrowDescriptor=None, AerialReinforcementArrowDescriptor=None):
        self.LandReinforcementArrowDescriptor = LandReinforcementArrowDescriptor
        self.AerialReinforcementArrowDescriptor = AerialReinforcementArrowDescriptor

    def __repr__(self):
        return f'<TReinforcementResource ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['LandReinforcementArrowDescriptor', 'AerialReinforcementArrowDescriptor']]) + '>'


class TUISpecificInGameResources:
    def __init__(self, Handler=None, UILayer=None, UILayerLDHint=None, CommonResources=None, MainStyleGuides=None, UnitReticleDescriptor=None, LabelRackForAggregationDescriptor=None, ViewDescriptors=None, MainContainerResource=None, ShortcutUserInputLayer=None, LDScriptUserInputLayer=None, CommonHUDResources=None, HUDResource=None, LabelResource=None, FlareLabelResources=None, PlayerMissionLabelResources=None, GabaritResources=None, UnitLabelResource=None, OutmapFeedbackResource=None, FeedbackLineOfSightResource=None, WarningPanelResources=None, LabelsOnMapResources=None, ScriptedLabelResources=None, FeedbackManagerDescriptor=None, GameRulesHelper=None, CorrectedShotRessources=None, ReinforcementResource=None, SelectionHandlerInGameResources=None, GroupSelectionReminderResources=None, PositionEvents=None, MousePolicyManagerResources=None, OptionManager=None, CommanderResources=None, HelperVisibility=None, CommandementZoneResources=None):
        self.Handler = Handler
        self.UILayer = UILayer
        self.UILayerLDHint = UILayerLDHint
        self.CommonResources = CommonResources
        self.MainStyleGuides = MainStyleGuides
        self.UnitReticleDescriptor = UnitReticleDescriptor
        self.LabelRackForAggregationDescriptor = LabelRackForAggregationDescriptor
        self.ViewDescriptors = ViewDescriptors
        self.MainContainerResource = MainContainerResource
        self.ShortcutUserInputLayer = ShortcutUserInputLayer
        self.LDScriptUserInputLayer = LDScriptUserInputLayer
        self.CommonHUDResources = CommonHUDResources
        self.HUDResource = HUDResource
        self.LabelResource = LabelResource
        self.FlareLabelResources = FlareLabelResources
        self.PlayerMissionLabelResources = PlayerMissionLabelResources
        self.GabaritResources = GabaritResources
        self.UnitLabelResource = UnitLabelResource
        self.OutmapFeedbackResource = OutmapFeedbackResource
        self.FeedbackLineOfSightResource = FeedbackLineOfSightResource
        self.WarningPanelResources = WarningPanelResources
        self.LabelsOnMapResources = LabelsOnMapResources
        self.ScriptedLabelResources = ScriptedLabelResources
        self.FeedbackManagerDescriptor = FeedbackManagerDescriptor
        self.GameRulesHelper = GameRulesHelper
        self.CorrectedShotRessources = CorrectedShotRessources
        self.ReinforcementResource = ReinforcementResource
        self.SelectionHandlerInGameResources = SelectionHandlerInGameResources
        self.GroupSelectionReminderResources = GroupSelectionReminderResources
        self.PositionEvents = PositionEvents
        self.MousePolicyManagerResources = MousePolicyManagerResources
        self.OptionManager = OptionManager
        self.CommanderResources = CommanderResources
        self.HelperVisibility = HelperVisibility
        self.CommandementZoneResources = CommandementZoneResources

    def __repr__(self):
        return f'<TUISpecificInGameResources ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Handler', 'UILayer', 'UILayerLDHint', 'CommonResources', 'MainStyleGuides', 'UnitReticleDescriptor', 'LabelRackForAggregationDescriptor', 'ViewDescriptors', 'MainContainerResource', 'ShortcutUserInputLayer', 'LDScriptUserInputLayer', 'CommonHUDResources', 'HUDResource', 'LabelResource', 'FlareLabelResources', 'PlayerMissionLabelResources', 'GabaritResources', 'UnitLabelResource', 'OutmapFeedbackResource', 'FeedbackLineOfSightResource', 'WarningPanelResources', 'LabelsOnMapResources', 'ScriptedLabelResources', 'FeedbackManagerDescriptor', 'GameRulesHelper', 'CorrectedShotRessources', 'ReinforcementResource', 'SelectionHandlerInGameResources', 'GroupSelectionReminderResources', 'PositionEvents', 'MousePolicyManagerResources', 'OptionManager', 'CommanderResources', 'HelperVisibility', 'CommandementZoneResources']]) + '>'


class UISpecificIngameChatViewDescriptor:
    def __init__(self, PanelColorStyle=None, ButtonColorStyle=None):
        self.PanelColorStyle = PanelColorStyle
        self.ButtonColorStyle = ButtonColorStyle

    def __repr__(self):
        return f'<UISpecificIngameChatViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['PanelColorStyle', 'ButtonColorStyle']]) + '>'


class UISpecificUnitInfoPanelViewDescriptor:
    def __init__(self, MainComponentContainerUniqueName=None, IsShowRoom=None):
        self.MainComponentContainerUniqueName = MainComponentContainerUniqueName
        self.IsShowRoom = IsShowRoom

    def __repr__(self):
        return f'<UISpecificUnitInfoPanelViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentContainerUniqueName', 'IsShowRoom']]) + '>'


class UISpecificSkirmishProductionMenuViewDescriptor:
    def __init__(self, IsFromStrategic=None):
        self.IsFromStrategic = IsFromStrategic

    def __repr__(self):
        return f'<UISpecificSkirmishProductionMenuViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['IsFromStrategic']]) + '>'


class UISpecificSmartGroupSelectionPanelViewDescriptor:
    def __init__(self, MainComponentContainerUniqueName=None):
        self.MainComponentContainerUniqueName = MainComponentContainerUniqueName

    def __repr__(self):
        return f'<UISpecificSmartGroupSelectionPanelViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentContainerUniqueName']]) + '>'


class TUICommonMainContainerResource:
    def __init__(self, ForegroundComponents=None, SafeBoxSize=None, SafeBoxMin=None, ContentRefSize=None):
        self.ForegroundComponents = ForegroundComponents
        self.SafeBoxSize = SafeBoxSize
        self.SafeBoxMin = SafeBoxMin
        self.ContentRefSize = ContentRefSize

    def __repr__(self):
        return f'<TUICommonMainContainerResource ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ForegroundComponents', 'SafeBoxSize', 'SafeBoxMin', 'ContentRefSize']]) + '>'


class TUISpecificInGameUnitLabelResources:
    def __init__(self, UILayer=None, UI3DLayer=None, Camera=None, CameraMoverHelperProxy=None, OpacityControlByFloat=None, FadeFactorForShaderParameter=None, LabelInAggregatMagnifiableBox=None, LabelMagnifiableBox=None, MagnifiableOffsetCenter=None, MagnifiableOffsetAggregatCenter=None, NbMaxAggregatedUnits=None, GhostLabelVersionTransparency=None, GhostLabelDeploymentVersionTransparency=None, UI3DTransformation=None, DamageTypeNameToFeedbackType=None, SmartOrderLabelTokens=None, TerrainTypeToTexture=None, AimingDefaultColor=None, AimingWhileMovingColor=None, ReloadingDefaultColor=None, ReloadingWhileMovingColor=None):
        self.UILayer = UILayer
        self.UI3DLayer = UI3DLayer
        self.Camera = Camera
        self.CameraMoverHelperProxy = CameraMoverHelperProxy
        self.OpacityControlByFloat = OpacityControlByFloat
        self.FadeFactorForShaderParameter = FadeFactorForShaderParameter
        self.LabelInAggregatMagnifiableBox = LabelInAggregatMagnifiableBox
        self.LabelMagnifiableBox = LabelMagnifiableBox
        self.MagnifiableOffsetCenter = MagnifiableOffsetCenter
        self.MagnifiableOffsetAggregatCenter = MagnifiableOffsetAggregatCenter
        self.NbMaxAggregatedUnits = NbMaxAggregatedUnits
        self.GhostLabelVersionTransparency = GhostLabelVersionTransparency
        self.GhostLabelDeploymentVersionTransparency = GhostLabelDeploymentVersionTransparency
        self.UI3DTransformation = UI3DTransformation
        self.DamageTypeNameToFeedbackType = DamageTypeNameToFeedbackType
        self.SmartOrderLabelTokens = SmartOrderLabelTokens
        self.TerrainTypeToTexture = TerrainTypeToTexture
        self.AimingDefaultColor = AimingDefaultColor
        self.AimingWhileMovingColor = AimingWhileMovingColor
        self.ReloadingDefaultColor = ReloadingDefaultColor
        self.ReloadingWhileMovingColor = ReloadingWhileMovingColor

    def __repr__(self):
        return f'<TUISpecificInGameUnitLabelResources ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['UILayer', 'UI3DLayer', 'Camera', 'CameraMoverHelperProxy', 'OpacityControlByFloat', 'FadeFactorForShaderParameter', 'LabelInAggregatMagnifiableBox', 'LabelMagnifiableBox', 'MagnifiableOffsetCenter', 'MagnifiableOffsetAggregatCenter', 'NbMaxAggregatedUnits', 'GhostLabelVersionTransparency', 'GhostLabelDeploymentVersionTransparency', 'UI3DTransformation', 'DamageTypeNameToFeedbackType', 'SmartOrderLabelTokens', 'TerrainTypeToTexture', 'AimingDefaultColor', 'AimingWhileMovingColor', 'ReloadingDefaultColor', 'ReloadingWhileMovingColor']]) + '>'


class TModernWarfareLabelTransformation:
    def __init__(self, Scene2D=None, RefResolution=None, Camera=None):
        self.Scene2D = Scene2D
        self.RefResolution = RefResolution
        self.Camera = Camera

    def __repr__(self):
        return f'<TModernWarfareLabelTransformation ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Scene2D', 'RefResolution', 'Camera']]) + '>'


class TUICommonWarningPanelResource:
    def __init__(self, FadeOutDuration=None, LifeAnimDurationForTemporary=None, FadeInDuration=None, ComponentByName=None):
        self.FadeOutDuration = FadeOutDuration
        self.LifeAnimDurationForTemporary = LifeAnimDurationForTemporary
        self.FadeInDuration = FadeInDuration
        self.ComponentByName = ComponentByName

    def __repr__(self):
        return f'<TUICommonWarningPanelResource ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['FadeOutDuration', 'LifeAnimDurationForTemporary', 'FadeInDuration', 'ComponentByName']]) + '>'


class TUISpecificOutmapFeedbackResources:
    def __init__(self, Camera=None, VitesseDeRotation=None, EcartementEntreCerclesExterieurs=None, EpaisseurDesTraitsExterieurs=None, TailleRelativeDeLaZoneRemplie=None, CouleurExterieure=None, EcartementEntreCerclesInterieurs=None, EpaisseurDesTraitsInterieurs=None, PositionAnneauInterieur=None, CouleurInterieure=None, EpaisseurCroix=None, LongueurCroix=None, CouleurCroix=None, CouleurAPortee=None, CouleurAPorteeInterieur=None, CouleurHorsDePortee=None, CouleurHorsDePorteeInterieur=None, CouleurDuFlash=None, CouleurDuFlashInterieur=None, DureeDuFadeOutAuTir=None, DureeDuFlashDeValidation=None, EpaisseurTraitStrike=None, CouleurDuTexte=None, CouleurDeLaBordure=None, DistanceApparition=None, DistanceDisparition=None, OffsetDuTexte=None, DescripteurDuPanel=None, DescripteurDuMessage=None, UILayer=None):
        self.Camera = Camera
        self.VitesseDeRotation = VitesseDeRotation
        self.EcartementEntreCerclesExterieurs = EcartementEntreCerclesExterieurs
        self.EpaisseurDesTraitsExterieurs = EpaisseurDesTraitsExterieurs
        self.TailleRelativeDeLaZoneRemplie = TailleRelativeDeLaZoneRemplie
        self.CouleurExterieure = CouleurExterieure
        self.EcartementEntreCerclesInterieurs = EcartementEntreCerclesInterieurs
        self.EpaisseurDesTraitsInterieurs = EpaisseurDesTraitsInterieurs
        self.PositionAnneauInterieur = PositionAnneauInterieur
        self.CouleurInterieure = CouleurInterieure
        self.EpaisseurCroix = EpaisseurCroix
        self.LongueurCroix = LongueurCroix
        self.CouleurCroix = CouleurCroix
        self.CouleurAPortee = CouleurAPortee
        self.CouleurAPorteeInterieur = CouleurAPorteeInterieur
        self.CouleurHorsDePortee = CouleurHorsDePortee
        self.CouleurHorsDePorteeInterieur = CouleurHorsDePorteeInterieur
        self.CouleurDuFlash = CouleurDuFlash
        self.CouleurDuFlashInterieur = CouleurDuFlashInterieur
        self.DureeDuFadeOutAuTir = DureeDuFadeOutAuTir
        self.DureeDuFlashDeValidation = DureeDuFlashDeValidation
        self.EpaisseurTraitStrike = EpaisseurTraitStrike
        self.CouleurDuTexte = CouleurDuTexte
        self.CouleurDeLaBordure = CouleurDeLaBordure
        self.DistanceApparition = DistanceApparition
        self.DistanceDisparition = DistanceDisparition
        self.OffsetDuTexte = OffsetDuTexte
        self.DescripteurDuPanel = DescripteurDuPanel
        self.DescripteurDuMessage = DescripteurDuMessage
        self.UILayer = UILayer

    def __repr__(self):
        return f'<TUISpecificOutmapFeedbackResources ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Camera', 'VitesseDeRotation', 'EcartementEntreCerclesExterieurs', 'EpaisseurDesTraitsExterieurs', 'TailleRelativeDeLaZoneRemplie', 'CouleurExterieure', 'EcartementEntreCerclesInterieurs', 'EpaisseurDesTraitsInterieurs', 'PositionAnneauInterieur', 'CouleurInterieure', 'EpaisseurCroix', 'LongueurCroix', 'CouleurCroix', 'CouleurAPortee', 'CouleurAPorteeInterieur', 'CouleurHorsDePortee', 'CouleurHorsDePorteeInterieur', 'CouleurDuFlash', 'CouleurDuFlashInterieur', 'DureeDuFadeOutAuTir', 'DureeDuFlashDeValidation', 'EpaisseurTraitStrike', 'CouleurDuTexte', 'CouleurDeLaBordure', 'DistanceApparition', 'DistanceDisparition', 'OffsetDuTexte', 'DescripteurDuPanel', 'DescripteurDuMessage', 'UILayer']]) + '>'


class BUCKGradientDescriptor:
    def __init__(self, TransitionColor1=None, Transition0=None, Transition1=None, IsRelative=None, IsVertical=None, Transition3=None, ElementName=None, Transition2=None, TransitionColor0=None, ComponentFrame=None):
        self.TransitionColor1 = TransitionColor1
        self.Transition0 = Transition0
        self.Transition1 = Transition1
        self.IsRelative = IsRelative
        self.IsVertical = IsVertical
        self.Transition3 = Transition3
        self.ElementName = ElementName
        self.Transition2 = Transition2
        self.TransitionColor0 = TransitionColor0
        self.ComponentFrame = ComponentFrame

    def __repr__(self):
        return f'<BUCKGradientDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TransitionColor1', 'Transition0', 'Transition1', 'IsRelative', 'IsVertical', 'Transition3', 'ElementName', 'Transition2', 'TransitionColor0', 'ComponentFrame']]) + '>'


class TUISpecificCommandZoneLabelViewDescriptor:
    def __init__(self, MainComponentDescriptor=None, MainComponentContainerUniqueName=None, UI3DLayer=None, VisibilityRange=None, FadeDuration=None, OpacityControlByFloat=None, TokenFormatCommandPointsByCombatRule=None):
        self.MainComponentDescriptor = MainComponentDescriptor
        self.MainComponentContainerUniqueName = MainComponentContainerUniqueName
        self.UI3DLayer = UI3DLayer
        self.VisibilityRange = VisibilityRange
        self.FadeDuration = FadeDuration
        self.OpacityControlByFloat = OpacityControlByFloat
        self.TokenFormatCommandPointsByCombatRule = TokenFormatCommandPointsByCombatRule

    def __repr__(self):
        return f'<TUISpecificCommandZoneLabelViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentDescriptor', 'MainComponentContainerUniqueName', 'UI3DLayer', 'VisibilityRange', 'FadeDuration', 'OpacityControlByFloat', 'TokenFormatCommandPointsByCombatRule']]) + '>'


class BUCKButtonDescriptor:
    def __init__(self, UniqueName=None, LeftClickSound=None, Grayed=None, ChildFitToContent=None, Components=None, Mapping=None, DefaultToggleValue=None, CannotDeselect=None, FitStyle=None, HidePointerEvents=None, ElementName=None, MaskEvents=None, BackgroundBlockColorToken=None, ComponentFrame=None, ForceEvents=None, HasBackground=None, IsTogglable=None, RadioButtonManager=None, HasBorder=None):
        self.UniqueName = UniqueName
        self.LeftClickSound = LeftClickSound
        self.Grayed = Grayed
        self.ChildFitToContent = ChildFitToContent
        self.Components = Components
        self.Mapping = Mapping
        self.DefaultToggleValue = DefaultToggleValue
        self.CannotDeselect = CannotDeselect
        self.FitStyle = FitStyle
        self.HidePointerEvents = HidePointerEvents
        self.ElementName = ElementName
        self.MaskEvents = MaskEvents
        self.BackgroundBlockColorToken = BackgroundBlockColorToken
        self.ComponentFrame = ComponentFrame
        self.ForceEvents = ForceEvents
        self.HasBackground = HasBackground
        self.IsTogglable = IsTogglable
        self.RadioButtonManager = RadioButtonManager
        self.HasBorder = HasBorder

    def __repr__(self):
        return f'<BUCKButtonDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['UniqueName', 'LeftClickSound', 'Grayed', 'ChildFitToContent', 'Components', 'Mapping', 'DefaultToggleValue', 'CannotDeselect', 'FitStyle', 'HidePointerEvents', 'ElementName', 'MaskEvents', 'BackgroundBlockColorToken', 'ComponentFrame', 'ForceEvents', 'HasBackground', 'IsTogglable', 'RadioButtonManager', 'HasBorder']]) + '>'


class TUISpecificHUDAlertPanelViewDescriptor:
    def __init__(self, MainComponentDescriptor=None, MainComponentContainerUniqueName=None, AlertLineDescriptor=None, EmptyLineDescriptor=None, MinimapMagnifiableSize=None, AlertLineHeight=None, LineDisplayDuration=None, MessageList=None):
        self.MainComponentDescriptor = MainComponentDescriptor
        self.MainComponentContainerUniqueName = MainComponentContainerUniqueName
        self.AlertLineDescriptor = AlertLineDescriptor
        self.EmptyLineDescriptor = EmptyLineDescriptor
        self.MinimapMagnifiableSize = MinimapMagnifiableSize
        self.AlertLineHeight = AlertLineHeight
        self.LineDisplayDuration = LineDisplayDuration
        self.MessageList = MessageList

    def __repr__(self):
        return f'<TUISpecificHUDAlertPanelViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentDescriptor', 'MainComponentContainerUniqueName', 'AlertLineDescriptor', 'EmptyLineDescriptor', 'MinimapMagnifiableSize', 'AlertLineHeight', 'LineDisplayDuration', 'MessageList']]) + '>'


class BUCKSpecificScrollingContainerDescriptor:
    def __init__(self, ExternalScrollbar=None, ScrollBarBackgroundToken=None, VerticalScrollbarComponentFrame=None, Components=None, ScrollBarElevatorBackgroundToken=None, HasBackground=None, HasVerticalScrollbar=None, FitStyle=None, FitToMaximumSize=None, ElementName=None, BackgroundBlockColorToken=None, ScrollStepSize=None, ComponentFrame=None):
        self.ExternalScrollbar = ExternalScrollbar
        self.ScrollBarBackgroundToken = ScrollBarBackgroundToken
        self.VerticalScrollbarComponentFrame = VerticalScrollbarComponentFrame
        self.Components = Components
        self.ScrollBarElevatorBackgroundToken = ScrollBarElevatorBackgroundToken
        self.HasBackground = HasBackground
        self.HasVerticalScrollbar = HasVerticalScrollbar
        self.FitStyle = FitStyle
        self.FitToMaximumSize = FitToMaximumSize
        self.ElementName = ElementName
        self.BackgroundBlockColorToken = BackgroundBlockColorToken
        self.ScrollStepSize = ScrollStepSize
        self.ComponentFrame = ComponentFrame

    def __repr__(self):
        return f'<BUCKSpecificScrollingContainerDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ExternalScrollbar', 'ScrollBarBackgroundToken', 'VerticalScrollbarComponentFrame', 'Components', 'ScrollBarElevatorBackgroundToken', 'HasBackground', 'HasVerticalScrollbar', 'FitStyle', 'FitToMaximumSize', 'ElementName', 'BackgroundBlockColorToken', 'ScrollStepSize', 'ComponentFrame']]) + '>'


class TRTTILength2:
    def __init__(self, Magnifiable=None):
        self.Magnifiable = Magnifiable

    def __repr__(self):
        return f'<TRTTILength2 ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Magnifiable']]) + '>'


class TUISpecificHUDMultiSelectionPanelViewDescriptor:
    def __init__(self, MainComponentDescriptor=None, MainComponentContainerUniqueName=None, MultiSelectionHorizontalListDescriptor=None, UnitLabelResources=None, NbUnitsByLine=None, LabelMagnifier=None):
        self.MainComponentDescriptor = MainComponentDescriptor
        self.MainComponentContainerUniqueName = MainComponentContainerUniqueName
        self.MultiSelectionHorizontalListDescriptor = MultiSelectionHorizontalListDescriptor
        self.UnitLabelResources = UnitLabelResources
        self.NbUnitsByLine = NbUnitsByLine
        self.LabelMagnifier = LabelMagnifier

    def __repr__(self):
        return f'<TUISpecificHUDMultiSelectionPanelViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentDescriptor', 'MainComponentContainerUniqueName', 'MultiSelectionHorizontalListDescriptor', 'UnitLabelResources', 'NbUnitsByLine', 'LabelMagnifier']]) + '>'


class TBUCKRadioButtonManager:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<TBUCKRadioButtonManager>'


class HUDButton:
    def __init__(self, BorderLineColorToken=None, Mapping=None, BackgroundTexture=None, CannotDeselect=None, ElementName=None, ComponentFrame=None, HintExtendedToken=None, BorderThickness=None, HintTitleToken=None, BackgroundColorToken=None, HasBackground=None, HintBodyToken=None, IsTogglable=None, HintDico=None, RadioButtonManager=None, BackgroundTextureFrameProperty=None, HasBorder=None):
        self.BorderLineColorToken = BorderLineColorToken
        self.Mapping = Mapping
        self.BackgroundTexture = BackgroundTexture
        self.CannotDeselect = CannotDeselect
        self.ElementName = ElementName
        self.ComponentFrame = ComponentFrame
        self.HintExtendedToken = HintExtendedToken
        self.BorderThickness = BorderThickness
        self.HintTitleToken = HintTitleToken
        self.BackgroundColorToken = BackgroundColorToken
        self.HasBackground = HasBackground
        self.HintBodyToken = HintBodyToken
        self.IsTogglable = IsTogglable
        self.HintDico = HintDico
        self.RadioButtonManager = RadioButtonManager
        self.BackgroundTextureFrameProperty = BackgroundTextureFrameProperty
        self.HasBorder = HasBorder

    def __repr__(self):
        return f'<HUDButton ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['BorderLineColorToken', 'Mapping', 'BackgroundTexture', 'CannotDeselect', 'ElementName', 'ComponentFrame', 'HintExtendedToken', 'BorderThickness', 'HintTitleToken', 'BackgroundColorToken', 'HasBackground', 'HintBodyToken', 'IsTogglable', 'HintDico', 'RadioButtonManager', 'BackgroundTextureFrameProperty', 'HasBorder']]) + '>'


class TUISpecificInGameHUDTimePanelViewDescriptor:
    def __init__(self, GameSpeedInfos=None, MainComponentDescriptor=None, MainComponentContainerUniqueName=None):
        self.GameSpeedInfos = GameSpeedInfos
        self.MainComponentDescriptor = MainComponentDescriptor
        self.MainComponentContainerUniqueName = MainComponentContainerUniqueName

    def __repr__(self):
        return f'<TUISpecificInGameHUDTimePanelViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['GameSpeedInfos', 'MainComponentDescriptor', 'MainComponentContainerUniqueName']]) + '>'


class TUIGameSpeedDescriptor:
    def __init__(self, GameSpeedValue=None, GameSpeedToken=None):
        self.GameSpeedValue = GameSpeedValue
        self.GameSpeedToken = GameSpeedToken

    def __repr__(self):
        return f'<TUIGameSpeedDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['GameSpeedValue', 'GameSpeedToken']]) + '>'


class TUISpecificIdleUnitViewDescriptor:
    def __init__(self, MainComponentContainerUniqueName=None, MainComponentDescriptor=None):
        self.MainComponentContainerUniqueName = MainComponentContainerUniqueName
        self.MainComponentDescriptor = MainComponentDescriptor

    def __repr__(self):
        return f'<TUISpecificIdleUnitViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentContainerUniqueName', 'MainComponentDescriptor']]) + '>'


class BUCKSpecificButton:
    def __init__(self, LeftClickSound=None, BorderLineColorToken=None, Components=None, TextParagraphStyle=None, TextToken=None, RoundedVertexes=None, HasText=None, TextDico=None, BigBorderBackgroundColorToken=None, BackgroundBlockColorToken=None, ButtonAlignementToFather=None, RoundedCorner=None, TextElementName=None, ButtonMagnifiableWidthHeight=None, TextTypefaceToken=None, RadioButtonManager=None, HasBackgroundTexture=None, Mapping=None, HintableAreaComponent=None, BackgroundTexture=None, ButtonAlignementToAnchor=None, HidePointerEvents=None, OverrideTextElementName=None, ElementName=None, ButtonRelativeWidthHeight=None, PanelRoundedCorner_BackgroundBlockColorToken=None, TextColorToken=None, TextSizeToken=None, IsTogglable=None, PanelRoundedCorner_BorderLineColorToken=None, HasBorder=None):
        self.LeftClickSound = LeftClickSound
        self.BorderLineColorToken = BorderLineColorToken
        self.Components = Components
        self.TextParagraphStyle = TextParagraphStyle
        self.TextToken = TextToken
        self.RoundedVertexes = RoundedVertexes
        self.HasText = HasText
        self.TextDico = TextDico
        self.BigBorderBackgroundColorToken = BigBorderBackgroundColorToken
        self.BackgroundBlockColorToken = BackgroundBlockColorToken
        self.ButtonAlignementToFather = ButtonAlignementToFather
        self.RoundedCorner = RoundedCorner
        self.TextElementName = TextElementName
        self.ButtonMagnifiableWidthHeight = ButtonMagnifiableWidthHeight
        self.TextTypefaceToken = TextTypefaceToken
        self.RadioButtonManager = RadioButtonManager
        self.HasBackgroundTexture = HasBackgroundTexture
        self.Mapping = Mapping
        self.HintableAreaComponent = HintableAreaComponent
        self.BackgroundTexture = BackgroundTexture
        self.ButtonAlignementToAnchor = ButtonAlignementToAnchor
        self.HidePointerEvents = HidePointerEvents
        self.OverrideTextElementName = OverrideTextElementName
        self.ElementName = ElementName
        self.ButtonRelativeWidthHeight = ButtonRelativeWidthHeight
        self.PanelRoundedCorner_BackgroundBlockColorToken = PanelRoundedCorner_BackgroundBlockColorToken
        self.TextColorToken = TextColorToken
        self.TextSizeToken = TextSizeToken
        self.IsTogglable = IsTogglable
        self.PanelRoundedCorner_BorderLineColorToken = PanelRoundedCorner_BorderLineColorToken
        self.HasBorder = HasBorder

    def __repr__(self):
        return f'<BUCKSpecificButton ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['LeftClickSound', 'BorderLineColorToken', 'Components', 'TextParagraphStyle', 'TextToken', 'RoundedVertexes', 'HasText', 'TextDico', 'BigBorderBackgroundColorToken', 'BackgroundBlockColorToken', 'ButtonAlignementToFather', 'RoundedCorner', 'TextElementName', 'ButtonMagnifiableWidthHeight', 'TextTypefaceToken', 'RadioButtonManager', 'HasBackgroundTexture', 'Mapping', 'HintableAreaComponent', 'BackgroundTexture', 'ButtonAlignementToAnchor', 'HidePointerEvents', 'OverrideTextElementName', 'ElementName', 'ButtonRelativeWidthHeight', 'PanelRoundedCorner_BackgroundBlockColorToken', 'TextColorToken', 'TextSizeToken', 'IsTogglable', 'PanelRoundedCorner_BorderLineColorToken', 'HasBorder']]) + '>'


class TUISpecificPlayerMissionLabelResources:
    def __init__(self, Layer=None, PlayerMissionLabelMagnificationMultiplier=None, PlayerMissionUserInputLayer=None, FadeTime=None, PlayerMissionLabelDescriptor=None, PlayerMissionLabelTransformation=None):
        self.Layer = Layer
        self.PlayerMissionLabelMagnificationMultiplier = PlayerMissionLabelMagnificationMultiplier
        self.PlayerMissionUserInputLayer = PlayerMissionUserInputLayer
        self.FadeTime = FadeTime
        self.PlayerMissionLabelDescriptor = PlayerMissionLabelDescriptor
        self.PlayerMissionLabelTransformation = PlayerMissionLabelTransformation

    def __repr__(self):
        return f'<TUISpecificPlayerMissionLabelResources ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Layer', 'PlayerMissionLabelMagnificationMultiplier', 'PlayerMissionUserInputLayer', 'FadeTime', 'PlayerMissionLabelDescriptor', 'PlayerMissionLabelTransformation']]) + '>'


class PlayerMissionLabelDescriptor:
    def __init__(self, TextToken=None, IconTextureToken=None, IconSize=None):
        self.TextToken = TextToken
        self.IconTextureToken = IconTextureToken
        self.IconSize = IconSize

    def __repr__(self):
        return f'<PlayerMissionLabelDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TextToken', 'IconTextureToken', 'IconSize']]) + '>'


class TLabelTransformPreTranslateFaceCamFakePerspective:
    def __init__(self, Scene2D=None, ConstnessFactor=None, Camera=None, ScalePerAltitudeConstReso=None):
        self.Scene2D = Scene2D
        self.ConstnessFactor = ConstnessFactor
        self.Camera = Camera
        self.ScalePerAltitudeConstReso = ScalePerAltitudeConstReso

    def __repr__(self):
        return f'<TLabelTransformPreTranslateFaceCamFakePerspective ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Scene2D', 'ConstnessFactor', 'Camera', 'ScalePerAltitudeConstReso']]) + '>'


class TLabelRackDescriptor:
    def __init__(self, ComponentFrame=None, RowAlignementToFather=None, RowAlignementToAnchor=None, OneLabelMagnifiableWidthHeight=None, DistrictComponent=None):
        self.ComponentFrame = ComponentFrame
        self.RowAlignementToFather = RowAlignementToFather
        self.RowAlignementToAnchor = RowAlignementToAnchor
        self.OneLabelMagnifiableWidthHeight = OneLabelMagnifiableWidthHeight
        self.DistrictComponent = DistrictComponent

    def __repr__(self):
        return f'<TLabelRackDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ComponentFrame', 'RowAlignementToFather', 'RowAlignementToAnchor', 'OneLabelMagnifiableWidthHeight', 'DistrictComponent']]) + '>'


class TUISpecificInGameLabelRackDescriptor:
    def __init__(self, MainComponentDescriptor=None, UnitLabelResources=None):
        self.MainComponentDescriptor = MainComponentDescriptor
        self.UnitLabelResources = UnitLabelResources

    def __repr__(self):
        return f'<TUISpecificInGameLabelRackDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentDescriptor', 'UnitLabelResources']]) + '>'


class TUISpecificMiniMapInfoViewDescriptor:
    def __init__(self, MainComponentDescriptor=None, MainComponentContainerUniqueName=None):
        self.MainComponentDescriptor = MainComponentDescriptor
        self.MainComponentContainerUniqueName = MainComponentContainerUniqueName

    def __repr__(self):
        return f'<TUISpecificMiniMapInfoViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentDescriptor', 'MainComponentContainerUniqueName']]) + '>'


class BUCKSpecificOffMapButton:
    def __init__(self, ElementName=None, ButtonWidthHeight=None, HeightCoefficientToRemoveFromInteriorButtonWidth=None, MainBackgroundColorToken=None, BorderLineColorToken=None, Components=None):
        self.ElementName = ElementName
        self.ButtonWidthHeight = ButtonWidthHeight
        self.HeightCoefficientToRemoveFromInteriorButtonWidth = HeightCoefficientToRemoveFromInteriorButtonWidth
        self.MainBackgroundColorToken = MainBackgroundColorToken
        self.BorderLineColorToken = BorderLineColorToken
        self.Components = Components

    def __repr__(self):
        return f'<BUCKSpecificOffMapButton ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ElementName', 'ButtonWidthHeight', 'HeightCoefficientToRemoveFromInteriorButtonWidth', 'MainBackgroundColorToken', 'BorderLineColorToken', 'Components']]) + '>'


class TUISpecificOffMapAirplaneViewDescriptor:
    def __init__(self, MainComponentDescriptor=None, MainComponentContainerUniqueName=None, ExperienceTextureTokens=None):
        self.MainComponentDescriptor = MainComponentDescriptor
        self.MainComponentContainerUniqueName = MainComponentContainerUniqueName
        self.ExperienceTextureTokens = ExperienceTextureTokens

    def __repr__(self):
        return f'<TUISpecificOffMapAirplaneViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentDescriptor', 'MainComponentContainerUniqueName', 'ExperienceTextureTokens']]) + '>'


class TBUCKButtonDescriptor:
    def __init__(self, ElementName=None, ComponentFrame=None, RadioButtonManager=None, IsTogglable=None, Components=None):
        self.ElementName = ElementName
        self.ComponentFrame = ComponentFrame
        self.RadioButtonManager = RadioButtonManager
        self.IsTogglable = IsTogglable
        self.Components = Components

    def __repr__(self):
        return f'<TBUCKButtonDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ElementName', 'ComponentFrame', 'RadioButtonManager', 'IsTogglable', 'Components']]) + '>'


class BUCKRackDescriptor:
    def __init__(self, BladeDescriptor=None, UniqueName=None, Axis=None, FirstMargin=None, HidePointerEvents=None, ElementName=None, AssumeChildrenAreFixedSize=None, BackgroundBlockColorToken=None, ComponentFrame=None, BreadthComputationMode=None, ForegroundComponents=None, InterItemMargin=None, BackgroundComponents=None, HasBackground=None, LastMargin=None):
        self.BladeDescriptor = BladeDescriptor
        self.UniqueName = UniqueName
        self.Axis = Axis
        self.FirstMargin = FirstMargin
        self.HidePointerEvents = HidePointerEvents
        self.ElementName = ElementName
        self.AssumeChildrenAreFixedSize = AssumeChildrenAreFixedSize
        self.BackgroundBlockColorToken = BackgroundBlockColorToken
        self.ComponentFrame = ComponentFrame
        self.BreadthComputationMode = BreadthComputationMode
        self.ForegroundComponents = ForegroundComponents
        self.InterItemMargin = InterItemMargin
        self.BackgroundComponents = BackgroundComponents
        self.HasBackground = HasBackground
        self.LastMargin = LastMargin

    def __repr__(self):
        return f'<BUCKRackDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['BladeDescriptor', 'UniqueName', 'Axis', 'FirstMargin', 'HidePointerEvents', 'ElementName', 'AssumeChildrenAreFixedSize', 'BackgroundBlockColorToken', 'ComponentFrame', 'BreadthComputationMode', 'ForegroundComponents', 'InterItemMargin', 'BackgroundComponents', 'HasBackground', 'LastMargin']]) + '>'


class TUISpecificReinforcementLabelViewDescriptor:
    def __init__(self, MainComponentDescriptor=None, MainComponentContainerUniqueName=None, UI3DLayer=None, VisibilityRange=None, FadeDuration=None, OpacityControlByFloat=None, ReinforcementTokens=None):
        self.MainComponentDescriptor = MainComponentDescriptor
        self.MainComponentContainerUniqueName = MainComponentContainerUniqueName
        self.UI3DLayer = UI3DLayer
        self.VisibilityRange = VisibilityRange
        self.FadeDuration = FadeDuration
        self.OpacityControlByFloat = OpacityControlByFloat
        self.ReinforcementTokens = ReinforcementTokens

    def __repr__(self):
        return f'<TUISpecificReinforcementLabelViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentDescriptor', 'MainComponentContainerUniqueName', 'UI3DLayer', 'VisibilityRange', 'FadeDuration', 'OpacityControlByFloat', 'ReinforcementTokens']]) + '>'


class TNameAndUnitCountDescription:
    def __init__(self, NbUnitsBackgroundColor=None, NbUnitsTextColor=None, UnitNameHPadding=None, UnitInfoTextSize=None, UnitNameTextStyle=None, UnitNumberHPadding=None, NbUnitsTextStyle=None, TextFormatScript=None, HideBackground=None, UnitInfoVPadding=None, TypefaceToken=None, ParagraphStyle=None):
        self.NbUnitsBackgroundColor = NbUnitsBackgroundColor
        self.NbUnitsTextColor = NbUnitsTextColor
        self.UnitNameHPadding = UnitNameHPadding
        self.UnitInfoTextSize = UnitInfoTextSize
        self.UnitNameTextStyle = UnitNameTextStyle
        self.UnitNumberHPadding = UnitNumberHPadding
        self.NbUnitsTextStyle = NbUnitsTextStyle
        self.TextFormatScript = TextFormatScript
        self.HideBackground = HideBackground
        self.UnitInfoVPadding = UnitInfoVPadding
        self.TypefaceToken = TypefaceToken
        self.ParagraphStyle = ParagraphStyle

    def __repr__(self):
        return f'<TNameAndUnitCountDescription ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['NbUnitsBackgroundColor', 'NbUnitsTextColor', 'UnitNameHPadding', 'UnitInfoTextSize', 'UnitNameTextStyle', 'UnitNumberHPadding', 'NbUnitsTextStyle', 'TextFormatScript', 'HideBackground', 'UnitInfoVPadding', 'TypefaceToken', 'ParagraphStyle']]) + '>'


class TLeavingDistrictChronoDescription:
    def __init__(self, ChronoDrawer=None, ChronoTexture=None, ChronoBackgroundColor=None, ChronoForegroundColor=None):
        self.ChronoDrawer = ChronoDrawer
        self.ChronoTexture = ChronoTexture
        self.ChronoBackgroundColor = ChronoBackgroundColor
        self.ChronoForegroundColor = ChronoForegroundColor

    def __repr__(self):
        return f'<TLeavingDistrictChronoDescription ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ChronoDrawer', 'ChronoTexture', 'ChronoBackgroundColor', 'ChronoForegroundColor']]) + '>'


class TBUCKSpecificLabelUnitIconDescriptor:
    def __init__(self, ElementName=None, ComponentFrame=None, ChildFitToContent=None, LocalRenderLayer=None, TextureDrawer=None, UniformDrawer=None, HasBorder=None, BorderThicknessToken=None, BorderLineColorToken=None, HasBackground=None, MoraleAndHPGaugesDescription=None, SmartChipDescription=None):
        self.ElementName = ElementName
        self.ComponentFrame = ComponentFrame
        self.ChildFitToContent = ChildFitToContent
        self.LocalRenderLayer = LocalRenderLayer
        self.TextureDrawer = TextureDrawer
        self.UniformDrawer = UniformDrawer
        self.HasBorder = HasBorder
        self.BorderThicknessToken = BorderThicknessToken
        self.BorderLineColorToken = BorderLineColorToken
        self.HasBackground = HasBackground
        self.MoraleAndHPGaugesDescription = MoraleAndHPGaugesDescription
        self.SmartChipDescription = SmartChipDescription

    def __repr__(self):
        return f'<TBUCKSpecificLabelUnitIconDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ElementName', 'ComponentFrame', 'ChildFitToContent', 'LocalRenderLayer', 'TextureDrawer', 'UniformDrawer', 'HasBorder', 'BorderThicknessToken', 'BorderLineColorToken', 'HasBackground', 'MoraleAndHPGaugesDescription', 'SmartChipDescription']]) + '>'


class TBUCKSpecificLabelUpperListDescriptor:
    def __init__(self, ElementName=None, ComponentFrame=None, NameAndUnitCountDescription=None, IsClippable=None, HasBackground=None, ChildFitToContent=None, BackgroundLocalRenderLayer=None, LocalRenderLayer=None, UniformDrawer=None, TextureDrawer=None, EvacuationIconTextureName=None, EvacuationIconMagnifiableSize=None, ReloadIconMagnifiableSize=None, ReloadIconDrawer=None, ReloadIconChronoTexture=None, ReloadIconTextureToken=None, ReloadIconChronoBackgroundColor=None, ReloadIconChronoForegroundColor=None, PlayerNameTextStyle=None, PlayerNameTextColor=None, PlayerNameTypefaceToken=None, PlayerNameTextSize=None, PlayerNamePadding=None):
        self.ElementName = ElementName
        self.ComponentFrame = ComponentFrame
        self.NameAndUnitCountDescription = NameAndUnitCountDescription
        self.IsClippable = IsClippable
        self.HasBackground = HasBackground
        self.ChildFitToContent = ChildFitToContent
        self.BackgroundLocalRenderLayer = BackgroundLocalRenderLayer
        self.LocalRenderLayer = LocalRenderLayer
        self.UniformDrawer = UniformDrawer
        self.TextureDrawer = TextureDrawer
        self.EvacuationIconTextureName = EvacuationIconTextureName
        self.EvacuationIconMagnifiableSize = EvacuationIconMagnifiableSize
        self.ReloadIconMagnifiableSize = ReloadIconMagnifiableSize
        self.ReloadIconDrawer = ReloadIconDrawer
        self.ReloadIconChronoTexture = ReloadIconChronoTexture
        self.ReloadIconTextureToken = ReloadIconTextureToken
        self.ReloadIconChronoBackgroundColor = ReloadIconChronoBackgroundColor
        self.ReloadIconChronoForegroundColor = ReloadIconChronoForegroundColor
        self.PlayerNameTextStyle = PlayerNameTextStyle
        self.PlayerNameTextColor = PlayerNameTextColor
        self.PlayerNameTypefaceToken = PlayerNameTypefaceToken
        self.PlayerNameTextSize = PlayerNameTextSize
        self.PlayerNamePadding = PlayerNamePadding

    def __repr__(self):
        return f'<TBUCKSpecificLabelUpperListDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ElementName', 'ComponentFrame', 'NameAndUnitCountDescription', 'IsClippable', 'HasBackground', 'ChildFitToContent', 'BackgroundLocalRenderLayer', 'LocalRenderLayer', 'UniformDrawer', 'TextureDrawer', 'EvacuationIconTextureName', 'EvacuationIconMagnifiableSize', 'ReloadIconMagnifiableSize', 'ReloadIconDrawer', 'ReloadIconChronoTexture', 'ReloadIconTextureToken', 'ReloadIconChronoBackgroundColor', 'ReloadIconChronoForegroundColor', 'PlayerNameTextStyle', 'PlayerNameTextColor', 'PlayerNameTypefaceToken', 'PlayerNameTextSize', 'PlayerNamePadding']]) + '>'


class TCarriedUnitLabelDescriptor:
    def __init__(self, ElementName=None, ComponentFrame=None, NameAndUnitCountDescription=None, HasBackground=None, IsClippable=None, BackgroundLocalRenderLayer=None, LocalRenderLayer=None, UniformDrawer=None):
        self.ElementName = ElementName
        self.ComponentFrame = ComponentFrame
        self.NameAndUnitCountDescription = NameAndUnitCountDescription
        self.HasBackground = HasBackground
        self.IsClippable = IsClippable
        self.BackgroundLocalRenderLayer = BackgroundLocalRenderLayer
        self.LocalRenderLayer = LocalRenderLayer
        self.UniformDrawer = UniformDrawer

    def __repr__(self):
        return f'<TCarriedUnitLabelDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ElementName', 'ComponentFrame', 'NameAndUnitCountDescription', 'HasBackground', 'IsClippable', 'BackgroundLocalRenderLayer', 'LocalRenderLayer', 'UniformDrawer']]) + '>'


class BUCKListElementSpacer:
    def __init__(self, Magnifiable=None):
        self.Magnifiable = Magnifiable

    def __repr__(self):
        return f'<BUCKListElementSpacer ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Magnifiable']]) + '>'


class BUCKLocalLayerContainerDescriptor:
    def __init__(self, FitStyle=None, ElementName=None, Components=None, NbLayersToLock=None, ComponentFrame=None):
        self.FitStyle = FitStyle
        self.ElementName = ElementName
        self.Components = Components
        self.NbLayersToLock = NbLayersToLock
        self.ComponentFrame = ComponentFrame

    def __repr__(self):
        return f'<BUCKLocalLayerContainerDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['FitStyle', 'ElementName', 'Components', 'NbLayersToLock', 'ComponentFrame']]) + '>'


class TUISpecificInGameUnitLabelViewForMultiSelectionDescriptor:
    def __init__(self, MainComponentDescriptor=None, ExperienceTexturesResources=None, AnimConcealedBlinkDuration=None, AnimPanickedBlinkDuration=None, AnimShakenPauseTime=None, AnimShakenBlinkDuration=None, AnimShakenNbBlinks=None, SuppressAnimAlphaMinimum=None, ConcealedAnimAlphaMinimum=None, NormalBackgroundTexture=None, CarriedUnitIconUnknown=None):
        self.MainComponentDescriptor = MainComponentDescriptor
        self.ExperienceTexturesResources = ExperienceTexturesResources
        self.AnimConcealedBlinkDuration = AnimConcealedBlinkDuration
        self.AnimPanickedBlinkDuration = AnimPanickedBlinkDuration
        self.AnimShakenPauseTime = AnimShakenPauseTime
        self.AnimShakenBlinkDuration = AnimShakenBlinkDuration
        self.AnimShakenNbBlinks = AnimShakenNbBlinks
        self.SuppressAnimAlphaMinimum = SuppressAnimAlphaMinimum
        self.ConcealedAnimAlphaMinimum = ConcealedAnimAlphaMinimum
        self.NormalBackgroundTexture = NormalBackgroundTexture
        self.CarriedUnitIconUnknown = CarriedUnitIconUnknown

    def __repr__(self):
        return f'<TUISpecificInGameUnitLabelViewForMultiSelectionDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentDescriptor', 'ExperienceTexturesResources', 'AnimConcealedBlinkDuration', 'AnimPanickedBlinkDuration', 'AnimShakenPauseTime', 'AnimShakenBlinkDuration', 'AnimShakenNbBlinks', 'SuppressAnimAlphaMinimum', 'ConcealedAnimAlphaMinimum', 'NormalBackgroundTexture', 'CarriedUnitIconUnknown']]) + '>'


class CurrentUnitLabelUpperList:
    def __init__(self, ChildFitToContent=None):
        self.ChildFitToContent = ChildFitToContent

    def __repr__(self):
        return f'<CurrentUnitLabelUpperList ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ChildFitToContent']]) + '>'


class CarriedUnitNameList:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<CarriedUnitNameList>'


class TSmartChipListDescriptor:
    def __init__(self, UniformDrawer=None, ElementName=None, Description=None, AlignementToFather=None, AlignementToAnchor=None, LocalRenderLayer=None):
        self.UniformDrawer = UniformDrawer
        self.ElementName = ElementName
        self.Description = Description
        self.AlignementToFather = AlignementToFather
        self.AlignementToAnchor = AlignementToAnchor
        self.LocalRenderLayer = LocalRenderLayer

    def __repr__(self):
        return f'<TSmartChipListDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['UniformDrawer', 'ElementName', 'Description', 'AlignementToFather', 'AlignementToAnchor', 'LocalRenderLayer']]) + '>'


class LabelFeedbackIcons:
    def __init__(self, ComponentFrame=None):
        self.ComponentFrame = ComponentFrame

    def __repr__(self):
        return f'<LabelFeedbackIcons ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ComponentFrame']]) + '>'


class TMoraleGaugeDescriptor:
    def __init__(self, ElementName=None, Description=None, LocalRenderLayer=None, UniformDrawer=None, AlignementToFather=None, AlignementToAnchor=None):
        self.ElementName = ElementName
        self.Description = Description
        self.LocalRenderLayer = LocalRenderLayer
        self.UniformDrawer = UniformDrawer
        self.AlignementToFather = AlignementToFather
        self.AlignementToAnchor = AlignementToAnchor

    def __repr__(self):
        return f'<TMoraleGaugeDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ElementName', 'Description', 'LocalRenderLayer', 'UniformDrawer', 'AlignementToFather', 'AlignementToAnchor']]) + '>'


class UISpecificInGameUnitLabelViewDescriptor:
    def __init__(self, MainComponentDescriptor=None):
        self.MainComponentDescriptor = MainComponentDescriptor

    def __repr__(self):
        return f'<UISpecificInGameUnitLabelViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentDescriptor']]) + '>'


class WeaponInformation:
    def __init__(self, IsSelection=None):
        self.IsSelection = IsSelection

    def __repr__(self):
        return f'<WeaponInformation ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['IsSelection']]) + '>'


class TVisibilityRangeContainer:
    def __init__(self, AltitudeMax=None, ItemList=None):
        self.AltitudeMax = AltitudeMax
        self.ItemList = ItemList

    def __repr__(self):
        return f'<TVisibilityRangeContainer ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['AltitudeMax', 'ItemList']]) + '>'


class TVisibilityRange:
    def __init__(self, AltitudeMax=None, AltitudeMin=None):
        self.AltitudeMax = AltitudeMax
        self.AltitudeMin = AltitudeMin

    def __repr__(self):
        return f'<TVisibilityRange ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['AltitudeMax', 'AltitudeMin']]) + '>'


class TSimpleHelperVisibility:
    def __init__(self, RangeList=None, Camera=None, WorldFloorProxy=None):
        self.RangeList = RangeList
        self.Camera = Camera
        self.WorldFloorProxy = WorldFloorProxy

    def __repr__(self):
        return f'<TSimpleHelperVisibility ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['RangeList', 'Camera', 'WorldFloorProxy']]) + '>'


class TUIGameDifficultyListConfiguration:
    def __init__(self, GameDifficultyConfigs=None):
        self.GameDifficultyConfigs = GameDifficultyConfigs

    def __repr__(self):
        return f'<TUIGameDifficultyListConfiguration ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['GameDifficultyConfigs']]) + '>'


class TUIGameDifficultyConfigurationRTTI:
    def __init__(self, Texture=None, Name=None, DescriptionByMissionType=None):
        self.Texture = Texture
        self.Name = Name
        self.DescriptionByMissionType = DescriptionByMissionType

    def __repr__(self):
        return f'<TUIGameDifficultyConfigurationRTTI ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Texture', 'Name', 'DescriptionByMissionType']]) + '>'


class TUISpecificOutGameActionScreensContainerResource:
    def __init__(self, UILayerContainer=None, UILayerEventBlocker=None, ContainerDescriptor=None, DummyComponent=None):
        self.UILayerContainer = UILayerContainer
        self.UILayerEventBlocker = UILayerEventBlocker
        self.ContainerDescriptor = ContainerDescriptor
        self.DummyComponent = DummyComponent

    def __repr__(self):
        return f'<TUISpecificOutGameActionScreensContainerResource ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['UILayerContainer', 'UILayerEventBlocker', 'ContainerDescriptor', 'DummyComponent']]) + '>'


class TUISpecificOutGameCutSceneResources:
    def __init__(self, UILayer=None, MainContainer=None):
        self.UILayer = UILayer
        self.MainContainer = MainContainer

    def __repr__(self):
        return f'<TUISpecificOutGameCutSceneResources ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['UILayer', 'MainContainer']]) + '>'


class TUISpecificOutGameHUBContainerResource:
    def __init__(self, ContentRefSize=None, SafeBoxMin=None, SafeBoxSize=None, ScreenMinY=None, ScreenMaxY=None, EventInterceptorLayer=None, ForegroundContent=None):
        self.ContentRefSize = ContentRefSize
        self.SafeBoxMin = SafeBoxMin
        self.SafeBoxSize = SafeBoxSize
        self.ScreenMinY = ScreenMinY
        self.ScreenMaxY = ScreenMaxY
        self.EventInterceptorLayer = EventInterceptorLayer
        self.ForegroundContent = ForegroundContent

    def __repr__(self):
        return f'<TUISpecificOutGameHUBContainerResource ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ContentRefSize', 'SafeBoxMin', 'SafeBoxSize', 'ScreenMinY', 'ScreenMaxY', 'EventInterceptorLayer', 'ForegroundContent']]) + '>'


class BUCKTextureAnimationDescriptor:
    def __init__(self, ComponentFrame=None, AnimDuration=None, AlphaAnimDuration=None, IsCyclic=None, TextureList=None):
        self.ComponentFrame = ComponentFrame
        self.AnimDuration = AnimDuration
        self.AlphaAnimDuration = AlphaAnimDuration
        self.IsCyclic = IsCyclic
        self.TextureList = TextureList

    def __repr__(self):
        return f'<BUCKTextureAnimationDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ComponentFrame', 'AnimDuration', 'AlphaAnimDuration', 'IsCyclic', 'TextureList']]) + '>'


class TUISpecificOutGameLoadingPanelResource:
    def __init__(self, LoadingText=None, UserInputLayer=None, EditorHints=None, DevHints=None, CommonHints=None, LoadingComponents=None):
        self.LoadingText = LoadingText
        self.UserInputLayer = UserInputLayer
        self.EditorHints = EditorHints
        self.DevHints = DevHints
        self.CommonHints = CommonHints
        self.LoadingComponents = LoadingComponents

    def __repr__(self):
        return f'<TUISpecificOutGameLoadingPanelResource ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['LoadingText', 'UserInputLayer', 'EditorHints', 'DevHints', 'CommonHints', 'LoadingComponents']]) + '>'


class BUCKTypingTextDescriptor:
    def __init__(self, BigLineAction=None, TextToken=None, AnimDuration=None, TextColor=None, AnimTextInSec=None, ElementName=None, TextDico=None, HorizontalFitStyle=None, VerticalFitStyle=None, ComponentFrame=None, TextSize=None, TypefaceToken=None, ParagraphStyle=None, TextStyle=None):
        self.BigLineAction = BigLineAction
        self.TextToken = TextToken
        self.AnimDuration = AnimDuration
        self.TextColor = TextColor
        self.AnimTextInSec = AnimTextInSec
        self.ElementName = ElementName
        self.TextDico = TextDico
        self.HorizontalFitStyle = HorizontalFitStyle
        self.VerticalFitStyle = VerticalFitStyle
        self.ComponentFrame = ComponentFrame
        self.TextSize = TextSize
        self.TypefaceToken = TypefaceToken
        self.ParagraphStyle = ParagraphStyle
        self.TextStyle = TextStyle

    def __repr__(self):
        return f'<BUCKTypingTextDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['BigLineAction', 'TextToken', 'AnimDuration', 'TextColor', 'AnimTextInSec', 'ElementName', 'TextDico', 'HorizontalFitStyle', 'VerticalFitStyle', 'ComponentFrame', 'TextSize', 'TypefaceToken', 'ParagraphStyle', 'TextStyle']]) + '>'


class BUCKRandomVideoContainerDescriptor:
    def __init__(self, ElementName=None, ComponentFrame=None, VideoDescriptor=None, PossibleVideos=None):
        self.ElementName = ElementName
        self.ComponentFrame = ComponentFrame
        self.VideoDescriptor = VideoDescriptor
        self.PossibleVideos = PossibleVideos

    def __repr__(self):
        return f'<BUCKRandomVideoContainerDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ElementName', 'ComponentFrame', 'VideoDescriptor', 'PossibleVideos']]) + '>'


class TUIResourceVideo:
    def __init__(self, DicoVideo=None, VideoFile=None):
        self.DicoVideo = DicoVideo
        self.VideoFile = VideoFile

    def __repr__(self):
        return f'<TUIResourceVideo ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['DicoVideo', 'VideoFile']]) + '>'


class SpecificModalWindow:
    def __init__(self, UniqueName=None, ContentMagnifiableWidthHeight=None, ElementsList=None, TitleToken=None, ButtonList=None):
        self.UniqueName = UniqueName
        self.ContentMagnifiableWidthHeight = ContentMagnifiableWidthHeight
        self.ElementsList = ElementsList
        self.TitleToken = TitleToken
        self.ButtonList = ButtonList

    def __repr__(self):
        return f'<SpecificModalWindow ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['UniqueName', 'ContentMagnifiableWidthHeight', 'ElementsList', 'TitleToken', 'ButtonList']]) + '>'


class SpecificModaleWindowFrame:
    def __init__(self, UniqueName=None, ContentRelativeWidthHeight=None, ContentMagnifiableWidthHeight=None, LastMargin=None, ContentComponents=None, FirstMargin=None, TitleToken=None, ButtonList=None, ComponentFrame=None):
        self.UniqueName = UniqueName
        self.ContentRelativeWidthHeight = ContentRelativeWidthHeight
        self.ContentMagnifiableWidthHeight = ContentMagnifiableWidthHeight
        self.LastMargin = LastMargin
        self.ContentComponents = ContentComponents
        self.FirstMargin = FirstMargin
        self.TitleToken = TitleToken
        self.ButtonList = ButtonList
        self.ComponentFrame = ComponentFrame

    def __repr__(self):
        return f'<SpecificModaleWindowFrame ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['UniqueName', 'ContentRelativeWidthHeight', 'ContentMagnifiableWidthHeight', 'LastMargin', 'ContentComponents', 'FirstMargin', 'TitleToken', 'ButtonList', 'ComponentFrame']]) + '>'


class BUCKEditableTextInputFieldDescriptor:
    def __init__(self, ElementName=None, ComponentFrame=None):
        self.ElementName = ElementName
        self.ComponentFrame = ComponentFrame

    def __repr__(self):
        return f'<BUCKEditableTextInputFieldDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ElementName', 'ComponentFrame']]) + '>'


class TUISpecificOutGameModaleResource:
    def __init__(self, ErrorText=None, ModaleContentWidth=None, ModaleWindow=None, ModaleText=None, ModaleButtonList=None, ModaleButton=None, ModaleConfirmButton=None, ModaleCancelButton=None, ModaleEditableText=None, ModaleWindowResourceForPrivacyPolicy=None, ModaleWindowResourceForOutdatedMods=None, ModaleRename=None, ModaleWindowResourceForMissingDLCs=None, ModaleButtonResourceForMissingDLCs=None, ModaleConfirmButtonResourceForMissingDLCs=None, ModaleCancelButtonResourceForMissingDLCs=None):
        self.ErrorText = ErrorText
        self.ModaleContentWidth = ModaleContentWidth
        self.ModaleWindow = ModaleWindow
        self.ModaleText = ModaleText
        self.ModaleButtonList = ModaleButtonList
        self.ModaleButton = ModaleButton
        self.ModaleConfirmButton = ModaleConfirmButton
        self.ModaleCancelButton = ModaleCancelButton
        self.ModaleEditableText = ModaleEditableText
        self.ModaleWindowResourceForPrivacyPolicy = ModaleWindowResourceForPrivacyPolicy
        self.ModaleWindowResourceForOutdatedMods = ModaleWindowResourceForOutdatedMods
        self.ModaleRename = ModaleRename
        self.ModaleWindowResourceForMissingDLCs = ModaleWindowResourceForMissingDLCs
        self.ModaleButtonResourceForMissingDLCs = ModaleButtonResourceForMissingDLCs
        self.ModaleConfirmButtonResourceForMissingDLCs = ModaleConfirmButtonResourceForMissingDLCs
        self.ModaleCancelButtonResourceForMissingDLCs = ModaleCancelButtonResourceForMissingDLCs

    def __repr__(self):
        return f'<TUISpecificOutGameModaleResource ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ErrorText', 'ModaleContentWidth', 'ModaleWindow', 'ModaleText', 'ModaleButtonList', 'ModaleButton', 'ModaleConfirmButton', 'ModaleCancelButton', 'ModaleEditableText', 'ModaleWindowResourceForPrivacyPolicy', 'ModaleWindowResourceForOutdatedMods', 'ModaleRename', 'ModaleWindowResourceForMissingDLCs', 'ModaleButtonResourceForMissingDLCs', 'ModaleConfirmButtonResourceForMissingDLCs', 'ModaleCancelButtonResourceForMissingDLCs']]) + '>'


class SpecificModalText:
    def __init__(self, TextToken=None, ElementName=None):
        self.TextToken = TextToken
        self.ElementName = ElementName

    def __repr__(self):
        return f'<SpecificModalText ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TextToken', 'ElementName']]) + '>'


class TUISpecificOutGamePlayerPropertyResource:
    def __init__(self, DefaultAvatar=None, UnknownAvatar=None, IAAvatar=None):
        self.DefaultAvatar = DefaultAvatar
        self.UnknownAvatar = UnknownAvatar
        self.IAAvatar = IAAvatar

    def __repr__(self):
        return f'<TUISpecificOutGamePlayerPropertyResource ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['DefaultAvatar', 'UnknownAvatar', 'IAAvatar']]) + '>'


class TUISpecificOutGameResources:
    def __init__(self, Handler=None, UILayer=None, DragAndDropUILayer=None, WarningUILayer=None, CommonResources=None, OptionManager=None, MainStyleGuides=None, HUBContainerResource=None, ActionScreensContainerResource=None, UserInputBinder=None, UIOffscreenSceneFactory=None, LevelUpAnimResource=None, WaitAnimResource=None, LoadingResource=None, LoginResource=None, EscapePanelResources=None, MainPanelWidth=None, MainPanelContentWidth=None, UISpecificDivisionSelectionViewDescriptor=None, CreditsResource=None, PlayerPropertyResource=None, NicknameChangeResource=None, ModaleResource=None, NotificationPanelResource=None, WarningPanelResources=None, ModCenterResources=None, ModResources=None, PingDisplayResources=None, TutorialGuideDescriptor=None, HostPanelResources=None, AutoMatchGameSearchContent=None, VersionTextContent=None, CampaignSoloResource=None, LevelUpContent=None, GameModeResources=None, CombatRuleResources=None, CutSceneResources=None, CountDownSound=None, GameFoundSound=None, ProfileClickSound=None, ViewDescriptors=None):
        self.Handler = Handler
        self.UILayer = UILayer
        self.DragAndDropUILayer = DragAndDropUILayer
        self.WarningUILayer = WarningUILayer
        self.CommonResources = CommonResources
        self.OptionManager = OptionManager
        self.MainStyleGuides = MainStyleGuides
        self.HUBContainerResource = HUBContainerResource
        self.ActionScreensContainerResource = ActionScreensContainerResource
        self.UserInputBinder = UserInputBinder
        self.UIOffscreenSceneFactory = UIOffscreenSceneFactory
        self.LevelUpAnimResource = LevelUpAnimResource
        self.WaitAnimResource = WaitAnimResource
        self.LoadingResource = LoadingResource
        self.LoginResource = LoginResource
        self.EscapePanelResources = EscapePanelResources
        self.MainPanelWidth = MainPanelWidth
        self.MainPanelContentWidth = MainPanelContentWidth
        self.UISpecificDivisionSelectionViewDescriptor = UISpecificDivisionSelectionViewDescriptor
        self.CreditsResource = CreditsResource
        self.PlayerPropertyResource = PlayerPropertyResource
        self.NicknameChangeResource = NicknameChangeResource
        self.ModaleResource = ModaleResource
        self.NotificationPanelResource = NotificationPanelResource
        self.WarningPanelResources = WarningPanelResources
        self.ModCenterResources = ModCenterResources
        self.ModResources = ModResources
        self.PingDisplayResources = PingDisplayResources
        self.TutorialGuideDescriptor = TutorialGuideDescriptor
        self.HostPanelResources = HostPanelResources
        self.AutoMatchGameSearchContent = AutoMatchGameSearchContent
        self.VersionTextContent = VersionTextContent
        self.CampaignSoloResource = CampaignSoloResource
        self.LevelUpContent = LevelUpContent
        self.GameModeResources = GameModeResources
        self.CombatRuleResources = CombatRuleResources
        self.CutSceneResources = CutSceneResources
        self.CountDownSound = CountDownSound
        self.GameFoundSound = GameFoundSound
        self.ProfileClickSound = ProfileClickSound
        self.ViewDescriptors = ViewDescriptors

    def __repr__(self):
        return f'<TUISpecificOutGameResources ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Handler', 'UILayer', 'DragAndDropUILayer', 'WarningUILayer', 'CommonResources', 'OptionManager', 'MainStyleGuides', 'HUBContainerResource', 'ActionScreensContainerResource', 'UserInputBinder', 'UIOffscreenSceneFactory', 'LevelUpAnimResource', 'WaitAnimResource', 'LoadingResource', 'LoginResource', 'EscapePanelResources', 'MainPanelWidth', 'MainPanelContentWidth', 'UISpecificDivisionSelectionViewDescriptor', 'CreditsResource', 'PlayerPropertyResource', 'NicknameChangeResource', 'ModaleResource', 'NotificationPanelResource', 'WarningPanelResources', 'ModCenterResources', 'ModResources', 'PingDisplayResources', 'TutorialGuideDescriptor', 'HostPanelResources', 'AutoMatchGameSearchContent', 'VersionTextContent', 'CampaignSoloResource', 'LevelUpContent', 'GameModeResources', 'CombatRuleResources', 'CutSceneResources', 'CountDownSound', 'GameFoundSound', 'ProfileClickSound', 'ViewDescriptors']]) + '>'


class UISpecificOutGameFriendListViewDescriptor:
    def __init__(self, ComponentContainerUniqueName=None, IsSubView=None):
        self.ComponentContainerUniqueName = ComponentContainerUniqueName
        self.IsSubView = IsSubView

    def __repr__(self):
        return f'<UISpecificOutGameFriendListViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ComponentContainerUniqueName', 'IsSubView']]) + '>'


class UISpecificScenarioViewDescriptor:
    def __init__(self, IsSubView=None, ComponentContainerUniqueName=None, GameType=None):
        self.IsSubView = IsSubView
        self.ComponentContainerUniqueName = ComponentContainerUniqueName
        self.GameType = GameType

    def __repr__(self):
        return f'<UISpecificScenarioViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['IsSubView', 'ComponentContainerUniqueName', 'GameType']]) + '>'


class UISpecificSaveLoadPanelViewDescriptor:
    def __init__(self, ComponentContainerUniqueName=None):
        self.ComponentContainerUniqueName = ComponentContainerUniqueName

    def __repr__(self):
        return f'<UISpecificSaveLoadPanelViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ComponentContainerUniqueName']]) + '>'


class UISpecificLeaderboardViewDescriptor:
    def __init__(self, ComponentContainerUniqueName=None):
        self.ComponentContainerUniqueName = ComponentContainerUniqueName

    def __repr__(self):
        return f'<UISpecificLeaderboardViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ComponentContainerUniqueName']]) + '>'


class UISpecificOutGameCreateAccountViewDescriptor:
    def __init__(self, IsAutologinAccount=None):
        self.IsAutologinAccount = IsAutologinAccount

    def __repr__(self):
        return f'<UISpecificOutGameCreateAccountViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['IsAutologinAccount']]) + '>'


class TVideoTextureDico:
    def __init__(self, FileName=None):
        self.FileName = FileName

    def __repr__(self):
        return f'<TVideoTextureDico ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['FileName']]) + '>'


class LoginTvContainer:
    def __init__(self, ElementName=None, Components=None):
        self.ElementName = ElementName
        self.Components = Components

    def __repr__(self):
        return f'<LoginTvContainer ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ElementName', 'Components']]) + '>'


class AnimatedWaitingComponent:
    def __init__(self, ComponentFrame=None):
        self.ComponentFrame = ComponentFrame

    def __repr__(self):
        return f'<AnimatedWaitingComponent ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ComponentFrame']]) + '>'


class TUISpecificConnectingPanelViewDescriptor:
    def __init__(self, MainComponentDescriptor=None, MainComponentContainerUniqueName=None):
        self.MainComponentDescriptor = MainComponentDescriptor
        self.MainComponentContainerUniqueName = MainComponentContainerUniqueName

    def __repr__(self):
        return f'<TUISpecificConnectingPanelViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentDescriptor', 'MainComponentContainerUniqueName']]) + '>'


class TUISpecificConnectionStateViewDescriptor:
    def __init__(self, MainComponentDescriptor=None, MainComponentContainerUniqueName=None, OnlineToken=None, OfflineToken=None):
        self.MainComponentDescriptor = MainComponentDescriptor
        self.MainComponentContainerUniqueName = MainComponentContainerUniqueName
        self.OnlineToken = OnlineToken
        self.OfflineToken = OfflineToken

    def __repr__(self):
        return f'<TUISpecificConnectionStateViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentDescriptor', 'MainComponentContainerUniqueName', 'OnlineToken', 'OfflineToken']]) + '>'


class MenuActionButton:
    def __init__(self, HintExtendedToken=None, HintTitleToken=None, TextToken=None, HintBodyToken=None, ElementName=None):
        self.HintExtendedToken = HintExtendedToken
        self.HintTitleToken = HintTitleToken
        self.TextToken = TextToken
        self.HintBodyToken = HintBodyToken
        self.ElementName = ElementName

    def __repr__(self):
        return f'<MenuActionButton ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['HintExtendedToken', 'HintTitleToken', 'TextToken', 'HintBodyToken', 'ElementName']]) + '>'


class BUCKSpecificDivisionBriefMainComponentDescriptor:
    def __init__(self, AlignementToAnchor=None, AlignementToFather=None, IsTogglable=None, CannotDeselect=None, RadioButtonManager=None, HasBattlegroup=None):
        self.AlignementToAnchor = AlignementToAnchor
        self.AlignementToFather = AlignementToFather
        self.IsTogglable = IsTogglable
        self.CannotDeselect = CannotDeselect
        self.RadioButtonManager = RadioButtonManager
        self.HasBattlegroup = HasBattlegroup

    def __repr__(self):
        return f'<BUCKSpecificDivisionBriefMainComponentDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['AlignementToAnchor', 'AlignementToFather', 'IsTogglable', 'CannotDeselect', 'RadioButtonManager', 'HasBattlegroup']]) + '>'


class EcranGaucheTextEditable:
    def __init__(self, TokenTitle=None, ElementName=None, IsPassword=None):
        self.TokenTitle = TokenTitle
        self.ElementName = ElementName
        self.IsPassword = IsPassword

    def __repr__(self):
        return f'<EcranGaucheTextEditable ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TokenTitle', 'ElementName', 'IsPassword']]) + '>'


class LoginScreenMainButton:
    def __init__(self, ButtonAlignementToFather=None, ButtonMagnifiableWidthHeight=None, Mapping=None, TextToken=None, ButtonMagnifiableOffset=None, ButtonAlignementToAnchor=None, ElementName=None):
        self.ButtonAlignementToFather = ButtonAlignementToFather
        self.ButtonMagnifiableWidthHeight = ButtonMagnifiableWidthHeight
        self.Mapping = Mapping
        self.TextToken = TextToken
        self.ButtonMagnifiableOffset = ButtonMagnifiableOffset
        self.ButtonAlignementToAnchor = ButtonAlignementToAnchor
        self.ElementName = ElementName

    def __repr__(self):
        return f'<LoginScreenMainButton ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ButtonAlignementToFather', 'ButtonMagnifiableWidthHeight', 'Mapping', 'TextToken', 'ButtonMagnifiableOffset', 'ButtonAlignementToAnchor', 'ElementName']]) + '>'


class TUISpecificLinkAccountViewDescriptor:
    def __init__(self, MainComponentDescriptor=None, MainComponentContainerUniqueName=None):
        self.MainComponentDescriptor = MainComponentDescriptor
        self.MainComponentContainerUniqueName = MainComponentContainerUniqueName

    def __repr__(self):
        return f'<TUISpecificLinkAccountViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentDescriptor', 'MainComponentContainerUniqueName']]) + '>'


class TUISpecificMultiLobbyShortcutsViewDescriptor:
    def __init__(self, MainComponentDescriptor=None, MainComponentContainerUniqueName=None, LobbysToDisplay=None):
        self.MainComponentDescriptor = MainComponentDescriptor
        self.MainComponentContainerUniqueName = MainComponentContainerUniqueName
        self.LobbysToDisplay = LobbysToDisplay

    def __repr__(self):
        return f'<TUISpecificMultiLobbyShortcutsViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentDescriptor', 'MainComponentContainerUniqueName', 'LobbysToDisplay']]) + '>'


class TLobbyNDFDescriptor:
    def __init__(self, NameToDisplay=None, CombatRule=None, InitMoney=None, UseAutofill=None, NumberOfPlayers=None):
        self.NameToDisplay = NameToDisplay
        self.CombatRule = CombatRule
        self.InitMoney = InitMoney
        self.UseAutofill = UseAutofill
        self.NumberOfPlayers = NumberOfPlayers

    def __repr__(self):
        return f'<TLobbyNDFDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['NameToDisplay', 'CombatRule', 'InitMoney', 'UseAutofill', 'NumberOfPlayers']]) + '>'


class OutGameOneChannelHeaderAndChannelListDescriptor:
    def __init__(self, ChannelListElementName=None, ShrinkButtonElementName=None, TitleElementName=None, TitleToken=None):
        self.ChannelListElementName = ChannelListElementName
        self.ShrinkButtonElementName = ShrinkButtonElementName
        self.TitleElementName = TitleElementName
        self.TitleToken = TitleToken

    def __repr__(self):
        return f'<OutGameOneChannelHeaderAndChannelListDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ChannelListElementName', 'ShrinkButtonElementName', 'TitleElementName', 'TitleToken']]) + '>'


class BUCKSpecificEditableTextDescriptor:
    def __init__(self, ElementName=None, HidePointerEvents=None, ComponentFrame=None, HasBackground=None, BackgroundBlockColorToken=None, ClippingContainerFrameProperty=None, TextSizeToken=None, TypefaceToken=None, Flags=None, MaxChars=None, TextStyle=None, HintComponentName=None, HintComponentDescriptor=None):
        self.ElementName = ElementName
        self.HidePointerEvents = HidePointerEvents
        self.ComponentFrame = ComponentFrame
        self.HasBackground = HasBackground
        self.BackgroundBlockColorToken = BackgroundBlockColorToken
        self.ClippingContainerFrameProperty = ClippingContainerFrameProperty
        self.TextSizeToken = TextSizeToken
        self.TypefaceToken = TypefaceToken
        self.Flags = Flags
        self.MaxChars = MaxChars
        self.TextStyle = TextStyle
        self.HintComponentName = HintComponentName
        self.HintComponentDescriptor = HintComponentDescriptor

    def __repr__(self):
        return f'<BUCKSpecificEditableTextDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ElementName', 'HidePointerEvents', 'ComponentFrame', 'HasBackground', 'BackgroundBlockColorToken', 'ClippingContainerFrameProperty', 'TextSizeToken', 'TypefaceToken', 'Flags', 'MaxChars', 'TextStyle', 'HintComponentName', 'HintComponentDescriptor']]) + '>'


class TUISpecificOutGameChatMessageListViewDescriptor:
    def __init__(self, MainComponentDescriptor=None, MainComponentContainerUniqueName=None, MaxNameSizeInChat=None):
        self.MainComponentDescriptor = MainComponentDescriptor
        self.MainComponentContainerUniqueName = MainComponentContainerUniqueName
        self.MaxNameSizeInChat = MaxNameSizeInChat

    def __repr__(self):
        return f'<TUISpecificOutGameChatMessageListViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentDescriptor', 'MainComponentContainerUniqueName', 'MaxNameSizeInChat']]) + '>'


class TUISpecificOutGameChatMessageViewDescriptor:
    def __init__(self, MainComponentDescriptor=None, MainComponentContainerUniqueName=None, BackgroundTextColorByMessageType=None, TextColorByMessageType=None):
        self.MainComponentDescriptor = MainComponentDescriptor
        self.MainComponentContainerUniqueName = MainComponentContainerUniqueName
        self.BackgroundTextColorByMessageType = BackgroundTextColorByMessageType
        self.TextColorByMessageType = TextColorByMessageType

    def __repr__(self):
        return f'<TUISpecificOutGameChatMessageViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentDescriptor', 'MainComponentContainerUniqueName', 'BackgroundTextColorByMessageType', 'TextColorByMessageType']]) + '>'


class TUISpecificOutGameChatOneChannelViewDescriptor:
    def __init__(self, MainComponentDescriptor=None, MainComponentContainerUniqueName=None):
        self.MainComponentDescriptor = MainComponentDescriptor
        self.MainComponentContainerUniqueName = MainComponentContainerUniqueName

    def __repr__(self):
        return f'<TUISpecificOutGameChatOneChannelViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentDescriptor', 'MainComponentContainerUniqueName']]) + '>'


class TUISpecificOutGameFriendModaleViewDescriptor:
    def __init__(self, MainComponentDescriptor=None, MainComponentContainerUniqueName=None):
        self.MainComponentDescriptor = MainComponentDescriptor
        self.MainComponentContainerUniqueName = MainComponentContainerUniqueName

    def __repr__(self):
        return f'<TUISpecificOutGameFriendModaleViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentDescriptor', 'MainComponentContainerUniqueName']]) + '>'


class BUCKSpecificAvatarDescriptor:
    def __init__(self, ElementName=None, TextureToken=None, ComponentFrame=None):
        self.ElementName = ElementName
        self.TextureToken = TextureToken
        self.ComponentFrame = ComponentFrame

    def __repr__(self):
        return f'<BUCKSpecificAvatarDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ElementName', 'TextureToken', 'ComponentFrame']]) + '>'


class TUIOutgameFriendLineViewDescriptor:
    def __init__(self, MainComponentDescriptor=None, MainComponentContainerUniqueName=None):
        self.MainComponentDescriptor = MainComponentDescriptor
        self.MainComponentContainerUniqueName = MainComponentContainerUniqueName

    def __repr__(self):
        return f'<TUIOutgameFriendLineViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentDescriptor', 'MainComponentContainerUniqueName']]) + '>'


class TUISpecificOutGameLobbyPlayerListViewDescriptor:
    def __init__(self, MainComponentDescriptor=None, MainComponentContainerUniqueName=None, AlliesToken=None, AxisToken=None):
        self.MainComponentDescriptor = MainComponentDescriptor
        self.MainComponentContainerUniqueName = MainComponentContainerUniqueName
        self.AlliesToken = AlliesToken
        self.AxisToken = AxisToken

    def __repr__(self):
        return f'<TUISpecificOutGameLobbyPlayerListViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentDescriptor', 'MainComponentContainerUniqueName', 'AlliesToken', 'AxisToken']]) + '>'


class TUISpecificOutGameMotdViewDescriptor:
    def __init__(self, MainComponentDescriptor=None, MainComponentContainerUniqueName=None):
        self.MainComponentDescriptor = MainComponentDescriptor
        self.MainComponentContainerUniqueName = MainComponentContainerUniqueName

    def __repr__(self):
        return f'<TUISpecificOutGameMotdViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentDescriptor', 'MainComponentContainerUniqueName']]) + '>'


class MainBackButtonContainer:
    def __init__(self, ButtonDefaultToken=None, BackMapping=None):
        self.ButtonDefaultToken = ButtonDefaultToken
        self.BackMapping = BackMapping

    def __repr__(self):
        return f'<MainBackButtonContainer ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ButtonDefaultToken', 'BackMapping']]) + '>'


class BUCKSpecificSliderDescriptor:
    def __init__(self, MaskEvents=None):
        self.MaskEvents = MaskEvents

    def __repr__(self):
        return f'<BUCKSpecificSliderDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MaskEvents']]) + '>'


class BUCKSpecificDropdownDescriptor:
    def __init__(self, BorderLineColorToken=None, Components=None, ItemsTextPadding=None, ShowArrow=None, HidePointerEvents=None, HasBorder=None, ElementName=None, ItemComponents=None, ComponentFrame=None, FloatingListMagnifiableWidth=None, MainTextColorToken=None, AlignFloatingPanelRight=None, OpenSound=None, ArrowTextureColorToken=None, ItemMagnifiableHeight=None, ItemsTextColorToken=None):
        self.BorderLineColorToken = BorderLineColorToken
        self.Components = Components
        self.ItemsTextPadding = ItemsTextPadding
        self.ShowArrow = ShowArrow
        self.HidePointerEvents = HidePointerEvents
        self.HasBorder = HasBorder
        self.ElementName = ElementName
        self.ItemComponents = ItemComponents
        self.ComponentFrame = ComponentFrame
        self.FloatingListMagnifiableWidth = FloatingListMagnifiableWidth
        self.MainTextColorToken = MainTextColorToken
        self.AlignFloatingPanelRight = AlignFloatingPanelRight
        self.OpenSound = OpenSound
        self.ArrowTextureColorToken = ArrowTextureColorToken
        self.ItemMagnifiableHeight = ItemMagnifiableHeight
        self.ItemsTextColorToken = ItemsTextColorToken

    def __repr__(self):
        return f'<BUCKSpecificDropdownDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['BorderLineColorToken', 'Components', 'ItemsTextPadding', 'ShowArrow', 'HidePointerEvents', 'HasBorder', 'ElementName', 'ItemComponents', 'ComponentFrame', 'FloatingListMagnifiableWidth', 'MainTextColorToken', 'AlignFloatingPanelRight', 'OpenSound', 'ArrowTextureColorToken', 'ItemMagnifiableHeight', 'ItemsTextColorToken']]) + '>'


class WindowFrame:
    def __init__(self, ContentRelativeWidthHeight=None, ButtonList=None, TitleToken=None, ContentExtendWeight=None, AdditionalComponents=None):
        self.ContentRelativeWidthHeight = ContentRelativeWidthHeight
        self.ButtonList = ButtonList
        self.TitleToken = TitleToken
        self.ContentExtendWeight = ContentExtendWeight
        self.AdditionalComponents = AdditionalComponents

    def __repr__(self):
        return f'<WindowFrame ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ContentRelativeWidthHeight', 'ButtonList', 'TitleToken', 'ContentExtendWeight', 'AdditionalComponents']]) + '>'


class BUCKStateUpdaterDescriptor:
    def __init__(self, ComponentFrame=None, Components=None):
        self.ComponentFrame = ComponentFrame
        self.Components = Components

    def __repr__(self):
        return f'<BUCKStateUpdaterDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ComponentFrame', 'Components']]) + '>'


class SpecificModalEditableText:
    def __init__(self, HasText=None, Flags=None, EditableTextElementName=None, TextToken=None):
        self.HasText = HasText
        self.Flags = Flags
        self.EditableTextElementName = EditableTextElementName
        self.TextToken = TextToken

    def __repr__(self):
        return f'<SpecificModalEditableText ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['HasText', 'Flags', 'EditableTextElementName', 'TextToken']]) + '>'


class TUISpecificOutGameShowInviteCodeModaleViewDescriptor:
    def __init__(self, MainComponentDescriptor=None, MainComponentContainerUniqueName=None):
        self.MainComponentDescriptor = MainComponentDescriptor
        self.MainComponentContainerUniqueName = MainComponentContainerUniqueName

    def __repr__(self):
        return f'<TUISpecificOutGameShowInviteCodeModaleViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentDescriptor', 'MainComponentContainerUniqueName']]) + '>'


class ThumbnailSoloDescriptor:
    def __init__(self, LeftClickSound=None, ForceEvents=None, TextToken=None, ElementName=None):
        self.LeftClickSound = LeftClickSound
        self.ForceEvents = ForceEvents
        self.TextToken = TextToken
        self.ElementName = ElementName

    def __repr__(self):
        return f'<ThumbnailSoloDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['LeftClickSound', 'ForceEvents', 'TextToken', 'ElementName']]) + '>'


class TUISpecificOutGameStrategicLobbyPlayerViewDescriptor:
    def __init__(self, MainComponentDescriptor=None, MainComponentContainerUniqueName=None, DefaultIAName=None):
        self.MainComponentDescriptor = MainComponentDescriptor
        self.MainComponentContainerUniqueName = MainComponentContainerUniqueName
        self.DefaultIAName = DefaultIAName

    def __repr__(self):
        return f'<TUISpecificOutGameStrategicLobbyPlayerViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentDescriptor', 'MainComponentContainerUniqueName', 'DefaultIAName']]) + '>'


class SoloNavigationButton:
    def __init__(self, TextSizeToken=None, HintExtendedToken=None, ButtonMagnifiableWidthHeight=None, Mapping=None, HintTitleToken=None, IsEmphasized=None, TextToken=None, HintBodyToken=None, HintableAreaElementName=None, ElementName=None):
        self.TextSizeToken = TextSizeToken
        self.HintExtendedToken = HintExtendedToken
        self.ButtonMagnifiableWidthHeight = ButtonMagnifiableWidthHeight
        self.Mapping = Mapping
        self.HintTitleToken = HintTitleToken
        self.IsEmphasized = IsEmphasized
        self.TextToken = TextToken
        self.HintBodyToken = HintBodyToken
        self.HintableAreaElementName = HintableAreaElementName
        self.ElementName = ElementName

    def __repr__(self):
        return f'<SoloNavigationButton ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TextSizeToken', 'HintExtendedToken', 'ButtonMagnifiableWidthHeight', 'Mapping', 'HintTitleToken', 'IsEmphasized', 'TextToken', 'HintBodyToken', 'HintableAreaElementName', 'ElementName']]) + '>'


class BUCKPerspectiveWarpOffscreenContainerDescriptor:
    def __init__(self, ElementName=None, DistortTextureDrawer=None, PointerEventsToAllow=None, MagnifiableTopLeftOffset=None, MagnifiableTopRightOffset=None, MagnifiableBottomLeftOffset=None, MagnifiableBottomRightOffset=None, ComponentFrame=None, Components=None):
        self.ElementName = ElementName
        self.DistortTextureDrawer = DistortTextureDrawer
        self.PointerEventsToAllow = PointerEventsToAllow
        self.MagnifiableTopLeftOffset = MagnifiableTopLeftOffset
        self.MagnifiableTopRightOffset = MagnifiableTopRightOffset
        self.MagnifiableBottomLeftOffset = MagnifiableBottomLeftOffset
        self.MagnifiableBottomRightOffset = MagnifiableBottomRightOffset
        self.ComponentFrame = ComponentFrame
        self.Components = Components

    def __repr__(self):
        return f'<BUCKPerspectiveWarpOffscreenContainerDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ElementName', 'DistortTextureDrawer', 'PointerEventsToAllow', 'MagnifiableTopLeftOffset', 'MagnifiableTopRightOffset', 'MagnifiableBottomLeftOffset', 'MagnifiableBottomRightOffset', 'ComponentFrame', 'Components']]) + '>'


class BUCKMultiListContentElementDescriptor:
    def __init__(self, FitStyle=None, ElementName=None, Components=None, ComponentFrame=None):
        self.FitStyle = FitStyle
        self.ElementName = ElementName
        self.Components = Components
        self.ComponentFrame = ComponentFrame

    def __repr__(self):
        return f'<BUCKMultiListContentElementDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['FitStyle', 'ElementName', 'Components', 'ComponentFrame']]) + '>'


class TUISpecificOutGameSoloCampaignResources:
    def __init__(self, ChapterDescriptions=None):
        self.ChapterDescriptions = ChapterDescriptions

    def __repr__(self):
        return f'<TUISpecificOutGameSoloCampaignResources ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ChapterDescriptions']]) + '>'


class BUCKSpecificCheckBoxDescriptor:
    def __init__(self, ElementName=None, ComponentFrame=None):
        self.ElementName = ElementName
        self.ComponentFrame = ComponentFrame

    def __repr__(self):
        return f'<BUCKSpecificCheckBoxDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ElementName', 'ComponentFrame']]) + '>'


class TUISpecificOutGameCreditsResource:
    def __init__(self, Credits=None, ScrollStep=None, DelayAtBottomBeforeGoingUp=None, DelayAtTopBeforeGoingDown=None, ShouldGoUpWhenBottomReached=None, ScrollStepUp=None, ShouldTeleportToTop=None):
        self.Credits = Credits
        self.ScrollStep = ScrollStep
        self.DelayAtBottomBeforeGoingUp = DelayAtBottomBeforeGoingUp
        self.DelayAtTopBeforeGoingDown = DelayAtTopBeforeGoingDown
        self.ShouldGoUpWhenBottomReached = ShouldGoUpWhenBottomReached
        self.ScrollStepUp = ScrollStepUp
        self.ShouldTeleportToTop = ShouldTeleportToTop

    def __repr__(self):
        return f'<TUISpecificOutGameCreditsResource ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Credits', 'ScrollStep', 'DelayAtBottomBeforeGoingUp', 'DelayAtTopBeforeGoingDown', 'ShouldGoUpWhenBottomReached', 'ScrollStepUp', 'ShouldTeleportToTop']]) + '>'


class ConfirmButton:
    def __init__(self, BorderLineColorToken=None, Components=None, Mapping=None, TextToken=None, HintableAreaComponent=None, ButtonAlignementToAnchor=None, ElementName=None, BackgroundBlockColorToken=None, TextColorToken=None, TextSizeToken=None, BorderThicknessToken=None, ButtonAlignementToFather=None, ButtonMagnifiableWidthHeight=None, TextTypefaceToken=None, HasBackground=None, TextStyle=None):
        self.BorderLineColorToken = BorderLineColorToken
        self.Components = Components
        self.Mapping = Mapping
        self.TextToken = TextToken
        self.HintableAreaComponent = HintableAreaComponent
        self.ButtonAlignementToAnchor = ButtonAlignementToAnchor
        self.ElementName = ElementName
        self.BackgroundBlockColorToken = BackgroundBlockColorToken
        self.TextColorToken = TextColorToken
        self.TextSizeToken = TextSizeToken
        self.BorderThicknessToken = BorderThicknessToken
        self.ButtonAlignementToFather = ButtonAlignementToFather
        self.ButtonMagnifiableWidthHeight = ButtonMagnifiableWidthHeight
        self.TextTypefaceToken = TextTypefaceToken
        self.HasBackground = HasBackground
        self.TextStyle = TextStyle

    def __repr__(self):
        return f'<ConfirmButton ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['BorderLineColorToken', 'Components', 'Mapping', 'TextToken', 'HintableAreaComponent', 'ButtonAlignementToAnchor', 'ElementName', 'BackgroundBlockColorToken', 'TextColorToken', 'TextSizeToken', 'BorderThicknessToken', 'ButtonAlignementToFather', 'ButtonMagnifiableWidthHeight', 'TextTypefaceToken', 'HasBackground', 'TextStyle']]) + '>'


class BUCKTranslationAnimatedContainerDescriptor:
    def __init__(self, ElementName=None, ButtonNameForTrigger=None, FramePropertyBeforeAnimation=None, AnimationTotalDuration=None, FramePropertyAfterAnimation=None, Components=None):
        self.ElementName = ElementName
        self.ButtonNameForTrigger = ButtonNameForTrigger
        self.FramePropertyBeforeAnimation = FramePropertyBeforeAnimation
        self.AnimationTotalDuration = AnimationTotalDuration
        self.FramePropertyAfterAnimation = FramePropertyAfterAnimation
        self.Components = Components

    def __repr__(self):
        return f'<BUCKTranslationAnimatedContainerDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ElementName', 'ButtonNameForTrigger', 'FramePropertyBeforeAnimation', 'AnimationTotalDuration', 'FramePropertyAfterAnimation', 'Components']]) + '>'


class TUISpecificOutGameEscapePanelResources:
    def __init__(self, EscapePanelMenu=None, EscapePanelContinueButton=None, EscapePanelRestartButton=None, EscapePanelHelpButton=None, EscapePanelSaveButton=None, EscapePanelLoadButton=None, EscapePanelOptionsButton=None, EscapePanelTutorialGuideButton=None, EscapePanelSurrenderOrQuitButton=None):
        self.EscapePanelMenu = EscapePanelMenu
        self.EscapePanelContinueButton = EscapePanelContinueButton
        self.EscapePanelRestartButton = EscapePanelRestartButton
        self.EscapePanelHelpButton = EscapePanelHelpButton
        self.EscapePanelSaveButton = EscapePanelSaveButton
        self.EscapePanelLoadButton = EscapePanelLoadButton
        self.EscapePanelOptionsButton = EscapePanelOptionsButton
        self.EscapePanelTutorialGuideButton = EscapePanelTutorialGuideButton
        self.EscapePanelSurrenderOrQuitButton = EscapePanelSurrenderOrQuitButton

    def __repr__(self):
        return f'<TUISpecificOutGameEscapePanelResources ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['EscapePanelMenu', 'EscapePanelContinueButton', 'EscapePanelRestartButton', 'EscapePanelHelpButton', 'EscapePanelSaveButton', 'EscapePanelLoadButton', 'EscapePanelOptionsButton', 'EscapePanelTutorialGuideButton', 'EscapePanelSurrenderOrQuitButton']]) + '>'


class TUISpecificOutGameHostPanelResources:
    def __init__(self, ModalWindowHost=None, ContentDescriptor=None):
        self.ModalWindowHost = ModalWindowHost
        self.ContentDescriptor = ContentDescriptor

    def __repr__(self):
        return f'<TUISpecificOutGameHostPanelResources ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ModalWindowHost', 'ContentDescriptor']]) + '>'


class TUISpecificOutGameLoginResource:
    def __init__(self, Login=None, Password=None, SavePassword=None, ErrorText=None, ErrorConnectionModalDescriptor=None, ChangePasswordModalDescriptor=None):
        self.Login = Login
        self.Password = Password
        self.SavePassword = SavePassword
        self.ErrorText = ErrorText
        self.ErrorConnectionModalDescriptor = ErrorConnectionModalDescriptor
        self.ChangePasswordModalDescriptor = ChangePasswordModalDescriptor

    def __repr__(self):
        return f'<TUISpecificOutGameLoginResource ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Login', 'Password', 'SavePassword', 'ErrorText', 'ErrorConnectionModalDescriptor', 'ChangePasswordModalDescriptor']]) + '>'


class StandardButton:
    def __init__(self, TextToken=None, ElementName=None):
        self.TextToken = TextToken
        self.ElementName = ElementName

    def __repr__(self):
        return f'<StandardButton ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TextToken', 'ElementName']]) + '>'


class CancelButton:
    def __init__(self, ButtonAlignementToFather=None, ButtonAlignementToAnchor=None, ButtonMagnifiableWidthHeight=None, ElementName=None, Mapping=None, TextToken=None):
        self.ButtonAlignementToFather = ButtonAlignementToFather
        self.ButtonAlignementToAnchor = ButtonAlignementToAnchor
        self.ButtonMagnifiableWidthHeight = ButtonMagnifiableWidthHeight
        self.ElementName = ElementName
        self.Mapping = Mapping
        self.TextToken = TextToken

    def __repr__(self):
        return f'<CancelButton ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ButtonAlignementToFather', 'ButtonAlignementToAnchor', 'ButtonMagnifiableWidthHeight', 'ElementName', 'Mapping', 'TextToken']]) + '>'


class TUISpecificOutGameNicknameChangeResource:
    def __init__(self, NicknameChangePanel=None):
        self.NicknameChangePanel = NicknameChangePanel

    def __repr__(self):
        return f'<TUISpecificOutGameNicknameChangeResource ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['NicknameChangePanel']]) + '>'


class TUISpecificShowRoomResources:
    def __init__(self, Handler=None, UILayer=None, UILayerAboveBlur=None, UILayerLDHint=None, CommonResources=None, InGameResourcesHandler=None, OutGameResourcesHandler=None, MousePointerMaskLayer=None, MainStyleGuides=None, ViewDescriptors=None, GroupSelectionReminderResources=None, LabelResource=None, MainContainerResource=None, MousePolicyManagerResources=None, WarningPanelResources=None, WarnOnMultiplayerDeckNotFilled=None, SelectionHandlerInGameResources=None, MagnifierMultiplier=None, DummyComponentForBlur=None, CountriesToShow=None, AllianceToCountriesToShow=None, SpecificHidingViewDescriptor=None, DeckCreatorViewHelperDescriptor=None, CameraMoverManager=None, ShortcutUserInputLayer=None, LDScriptUserInputLayer=None):
        self.Handler = Handler
        self.UILayer = UILayer
        self.UILayerAboveBlur = UILayerAboveBlur
        self.UILayerLDHint = UILayerLDHint
        self.CommonResources = CommonResources
        self.InGameResourcesHandler = InGameResourcesHandler
        self.OutGameResourcesHandler = OutGameResourcesHandler
        self.MousePointerMaskLayer = MousePointerMaskLayer
        self.MainStyleGuides = MainStyleGuides
        self.ViewDescriptors = ViewDescriptors
        self.GroupSelectionReminderResources = GroupSelectionReminderResources
        self.LabelResource = LabelResource
        self.MainContainerResource = MainContainerResource
        self.MousePolicyManagerResources = MousePolicyManagerResources
        self.WarningPanelResources = WarningPanelResources
        self.WarnOnMultiplayerDeckNotFilled = WarnOnMultiplayerDeckNotFilled
        self.SelectionHandlerInGameResources = SelectionHandlerInGameResources
        self.MagnifierMultiplier = MagnifierMultiplier
        self.DummyComponentForBlur = DummyComponentForBlur
        self.CountriesToShow = CountriesToShow
        self.AllianceToCountriesToShow = AllianceToCountriesToShow
        self.SpecificHidingViewDescriptor = SpecificHidingViewDescriptor
        self.DeckCreatorViewHelperDescriptor = DeckCreatorViewHelperDescriptor
        self.CameraMoverManager = CameraMoverManager
        self.ShortcutUserInputLayer = ShortcutUserInputLayer
        self.LDScriptUserInputLayer = LDScriptUserInputLayer

    def __repr__(self):
        return f'<TUISpecificShowRoomResources ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Handler', 'UILayer', 'UILayerAboveBlur', 'UILayerLDHint', 'CommonResources', 'InGameResourcesHandler', 'OutGameResourcesHandler', 'MousePointerMaskLayer', 'MainStyleGuides', 'ViewDescriptors', 'GroupSelectionReminderResources', 'LabelResource', 'MainContainerResource', 'MousePolicyManagerResources', 'WarningPanelResources', 'WarnOnMultiplayerDeckNotFilled', 'SelectionHandlerInGameResources', 'MagnifierMultiplier', 'DummyComponentForBlur', 'CountriesToShow', 'AllianceToCountriesToShow', 'SpecificHidingViewDescriptor', 'DeckCreatorViewHelperDescriptor', 'CameraMoverManager', 'ShortcutUserInputLayer', 'LDScriptUserInputLayer']]) + '>'


class UISpecificShowRoomGroupsDeckCreatorScreenViewDescriptor:
    def __init__(self, IsForChallenge=None, ChallengeDescriptionType=None, ChallengeMoreDescriptionType=None):
        self.IsForChallenge = IsForChallenge
        self.ChallengeDescriptionType = ChallengeDescriptionType
        self.ChallengeMoreDescriptionType = ChallengeMoreDescriptionType

    def __repr__(self):
        return f'<UISpecificShowRoomGroupsDeckCreatorScreenViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['IsForChallenge', 'ChallengeDescriptionType', 'ChallengeMoreDescriptionType']]) + '>'


class TUISpecificHidingViewDescriptor:
    def __init__(self, MainComponentDescriptor=None, MainComponentContainerUniqueName=None, FadedAnimation=None):
        self.MainComponentDescriptor = MainComponentDescriptor
        self.MainComponentContainerUniqueName = MainComponentContainerUniqueName
        self.FadedAnimation = FadedAnimation

    def __repr__(self):
        return f'<TUISpecificHidingViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentDescriptor', 'MainComponentContainerUniqueName', 'FadedAnimation']]) + '>'


class TUIAnimFactorRTTI:
    def __init__(self, ParamsAnim=None, AnimDuration=None, Modificator=None):
        self.ParamsAnim = ParamsAnim
        self.AnimDuration = AnimDuration
        self.Modificator = Modificator

    def __repr__(self):
        return f'<TUIAnimFactorRTTI ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ParamsAnim', 'AnimDuration', 'Modificator']]) + '>'


class BUCKEditableTextDescriptor:
    def __init__(self, ElementName=None, ComponentFrame=None, ClippingContainerFrameProperty=None, Flags=None, SelectionColorToken=None, TypefaceToken=None, TextColorToken=None, TextSizeToken=None, MaxChars=None):
        self.ElementName = ElementName
        self.ComponentFrame = ComponentFrame
        self.ClippingContainerFrameProperty = ClippingContainerFrameProperty
        self.Flags = Flags
        self.SelectionColorToken = SelectionColorToken
        self.TypefaceToken = TypefaceToken
        self.TextColorToken = TextColorToken
        self.TextSizeToken = TextSizeToken
        self.MaxChars = MaxChars

    def __repr__(self):
        return f'<BUCKEditableTextDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ElementName', 'ComponentFrame', 'ClippingContainerFrameProperty', 'Flags', 'SelectionColorToken', 'TypefaceToken', 'TextColorToken', 'TextSizeToken', 'MaxChars']]) + '>'


class HintInGameBUCKComponent:
    def __init__(self, BackgroundBlockColorToken=None, BorderLineColorToken=None):
        self.BackgroundBlockColorToken = BackgroundBlockColorToken
        self.BorderLineColorToken = BorderLineColorToken

    def __repr__(self):
        return f'<HintInGameBUCKComponent ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['BackgroundBlockColorToken', 'BorderLineColorToken']]) + '>'


class TStrategicBattleResources:
    def __init__(self, CantFightGhostColors=None, CantMoveGhostColors=None, BattlePlanningSupportInBattleGroupStyleDescriptor=None, BattlePlanningSupportNotInBattleGroupStyleDescriptor=None, BattlePlanningPawnInBattleGroupStyleDescriptor=None, BattlePlanningPotentialAttackerPawnStyleDescriptor=None, FightingSupportPawnStyleDescriptor=None, FightingFighterPawnStyleDescriptor=None, PotentialAttackersAnimDuration=None, MinAlphaForPotentialAttackers=None, MaxAlphaForPotentialAttackers=None):
        self.CantFightGhostColors = CantFightGhostColors
        self.CantMoveGhostColors = CantMoveGhostColors
        self.BattlePlanningSupportInBattleGroupStyleDescriptor = BattlePlanningSupportInBattleGroupStyleDescriptor
        self.BattlePlanningSupportNotInBattleGroupStyleDescriptor = BattlePlanningSupportNotInBattleGroupStyleDescriptor
        self.BattlePlanningPawnInBattleGroupStyleDescriptor = BattlePlanningPawnInBattleGroupStyleDescriptor
        self.BattlePlanningPotentialAttackerPawnStyleDescriptor = BattlePlanningPotentialAttackerPawnStyleDescriptor
        self.FightingSupportPawnStyleDescriptor = FightingSupportPawnStyleDescriptor
        self.FightingFighterPawnStyleDescriptor = FightingFighterPawnStyleDescriptor
        self.PotentialAttackersAnimDuration = PotentialAttackersAnimDuration
        self.MinAlphaForPotentialAttackers = MinAlphaForPotentialAttackers
        self.MaxAlphaForPotentialAttackers = MaxAlphaForPotentialAttackers

    def __repr__(self):
        return f'<TStrategicBattleResources ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['CantFightGhostColors', 'CantMoveGhostColors', 'BattlePlanningSupportInBattleGroupStyleDescriptor', 'BattlePlanningSupportNotInBattleGroupStyleDescriptor', 'BattlePlanningPawnInBattleGroupStyleDescriptor', 'BattlePlanningPotentialAttackerPawnStyleDescriptor', 'FightingSupportPawnStyleDescriptor', 'FightingFighterPawnStyleDescriptor', 'PotentialAttackersAnimDuration', 'MinAlphaForPotentialAttackers', 'MaxAlphaForPotentialAttackers']]) + '>'


class TGhostColors:
    def __init__(self, GhostAlphas=None, GhostBlends=None, GhostColor=None):
        self.GhostAlphas = GhostAlphas
        self.GhostBlends = GhostBlends
        self.GhostColor = GhostColor

    def __repr__(self):
        return f'<TGhostColors ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['GhostAlphas', 'GhostBlends', 'GhostColor']]) + '>'


class TLineFeedbackStyleDescriptor:
    def __init__(self, ParabolicArrowHeight=None, Border=None, Hatched=None, UnselectedStyle=None, SelectedStyle=None):
        self.ParabolicArrowHeight = ParabolicArrowHeight
        self.Border = Border
        self.Hatched = Hatched
        self.UnselectedStyle = UnselectedStyle
        self.SelectedStyle = SelectedStyle

    def __repr__(self):
        return f'<TLineFeedbackStyleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ParabolicArrowHeight', 'Border', 'Hatched', 'UnselectedStyle', 'SelectedStyle']]) + '>'


class TArrowFeedbackStyleDescriptor:
    def __init__(self, ArrowLineEndWidth=None, ArrowTipLength=None, UnselectedStyle=None, SelectedStyle=None, ArrowLineStartWidth=None, ArrowTipWidth=None):
        self.ArrowLineEndWidth = ArrowLineEndWidth
        self.ArrowTipLength = ArrowTipLength
        self.UnselectedStyle = UnselectedStyle
        self.SelectedStyle = SelectedStyle
        self.ArrowLineStartWidth = ArrowLineStartWidth
        self.ArrowTipWidth = ArrowTipWidth

    def __repr__(self):
        return f'<TArrowFeedbackStyleDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ArrowLineEndWidth', 'ArrowTipLength', 'UnselectedStyle', 'SelectedStyle', 'ArrowLineStartWidth', 'ArrowTipWidth']]) + '>'


class BUCKTreeViewDescriptor:
    def __init__(self, ElementName=None, ComponentFrame=None, LineMainComponentExtendWeight=None, TreeViewLineComponentDescriptor=None, TreeViewLineButtonDescriptor=None):
        self.ElementName = ElementName
        self.ComponentFrame = ComponentFrame
        self.LineMainComponentExtendWeight = LineMainComponentExtendWeight
        self.TreeViewLineComponentDescriptor = TreeViewLineComponentDescriptor
        self.TreeViewLineButtonDescriptor = TreeViewLineButtonDescriptor

    def __repr__(self):
        return f'<BUCKTreeViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ElementName', 'ComponentFrame', 'LineMainComponentExtendWeight', 'TreeViewLineComponentDescriptor', 'TreeViewLineButtonDescriptor']]) + '>'


class TreeLineButton:
    def __init__(self, LeftClickSound=None):
        self.LeftClickSound = LeftClickSound

    def __repr__(self):
        return f'<TreeLineButton ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['LeftClickSound']]) + '>'


class TUISpecificStrategicBattleOrderSubPanelViewDescriptor:
    def __init__(self, MainComponentDescriptor=None, PawnLineViewDescriptor=None, CompanyLineViewDescriptor=None, CompanyRadioButtonManager=None):
        self.MainComponentDescriptor = MainComponentDescriptor
        self.PawnLineViewDescriptor = PawnLineViewDescriptor
        self.CompanyLineViewDescriptor = CompanyLineViewDescriptor
        self.CompanyRadioButtonManager = CompanyRadioButtonManager

    def __repr__(self):
        return f'<TUISpecificStrategicBattleOrderSubPanelViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentDescriptor', 'PawnLineViewDescriptor', 'CompanyLineViewDescriptor', 'CompanyRadioButtonManager']]) + '>'


class UISpecificStrategicBattleOrderPanelDefaultLineViewDescriptor:
    def __init__(self, TitleTextDico=None):
        self.TitleTextDico = TitleTextDico

    def __repr__(self):
        return f'<UISpecificStrategicBattleOrderPanelDefaultLineViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TitleTextDico']]) + '>'


class UISpecificStrategicBattleOrderPanelCompanyLineViewDescriptor:
    def __init__(self, RadioButtonManager=None):
        self.RadioButtonManager = RadioButtonManager

    def __repr__(self):
        return f'<UISpecificStrategicBattleOrderPanelCompanyLineViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['RadioButtonManager']]) + '>'


class BUCKSpecificStrategicHintableArea:
    def __init__(self, HintBodyToken=None, HintExtendedToken=None, ElementName=None, HintTitleToken=None, DicoToken=None):
        self.HintBodyToken = HintBodyToken
        self.HintExtendedToken = HintExtendedToken
        self.ElementName = ElementName
        self.HintTitleToken = HintTitleToken
        self.DicoToken = DicoToken

    def __repr__(self):
        return f'<BUCKSpecificStrategicHintableArea ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['HintBodyToken', 'HintExtendedToken', 'ElementName', 'HintTitleToken', 'DicoToken']]) + '>'


class TUISpecificStrategicConnectedPlayersViewDescriptor:
    def __init__(self, MainComponentDescriptor=None, MainComponentContainerUniqueName=None):
        self.MainComponentDescriptor = MainComponentDescriptor
        self.MainComponentContainerUniqueName = MainComponentContainerUniqueName

    def __repr__(self):
        return f'<TUISpecificStrategicConnectedPlayersViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentDescriptor', 'MainComponentContainerUniqueName']]) + '>'


class TUISpecificStrategicDateViewDescriptor:
    def __init__(self, MainComponentDescriptor=None, MainComponentContainerUniqueName=None, NbTurnWithMaxToken=None, NbTurnWithoutMaxToken=None):
        self.MainComponentDescriptor = MainComponentDescriptor
        self.MainComponentContainerUniqueName = MainComponentContainerUniqueName
        self.NbTurnWithMaxToken = NbTurnWithMaxToken
        self.NbTurnWithoutMaxToken = NbTurnWithoutMaxToken

    def __repr__(self):
        return f'<TUISpecificStrategicDateViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentDescriptor', 'MainComponentContainerUniqueName', 'NbTurnWithMaxToken', 'NbTurnWithoutMaxToken']]) + '>'


class BUCKSpotlightDescriptor:
    def __init__(self, UniqueName=None, ElementName=None, ComponentFrame=None):
        self.UniqueName = UniqueName
        self.ElementName = ElementName
        self.ComponentFrame = ComponentFrame

    def __repr__(self):
        return f'<BUCKSpotlightDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['UniqueName', 'ElementName', 'ComponentFrame']]) + '>'


class OmbrePanel:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<OmbrePanel>'


class TUISpecificStrategicHUDGameSpeedViewDescriptor:
    def __init__(self, MainComponentDescriptor=None, MainComponentContainerUniqueName=None, GameSpeedMutliplierInPercent=None):
        self.MainComponentDescriptor = MainComponentDescriptor
        self.MainComponentContainerUniqueName = MainComponentContainerUniqueName
        self.GameSpeedMutliplierInPercent = GameSpeedMutliplierInPercent

    def __repr__(self):
        return f'<TUISpecificStrategicHUDGameSpeedViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentDescriptor', 'MainComponentContainerUniqueName', 'GameSpeedMutliplierInPercent']]) + '>'


class TUISpecificStrategicHUDChatButtonViewDescriptor:
    def __init__(self, MainComponentDescriptor=None, MainComponentContainerUniqueName=None):
        self.MainComponentDescriptor = MainComponentDescriptor
        self.MainComponentContainerUniqueName = MainComponentContainerUniqueName

    def __repr__(self):
        return f'<TUISpecificStrategicHUDChatButtonViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentDescriptor', 'MainComponentContainerUniqueName']]) + '>'


class TUISpecificStrategicHUDHeaderViewDescriptor:
    def __init__(self, MainComponentDescriptor=None, MainComponentContainerUniqueName=None, CancelMenuBinding=None):
        self.MainComponentDescriptor = MainComponentDescriptor
        self.MainComponentContainerUniqueName = MainComponentContainerUniqueName
        self.CancelMenuBinding = CancelMenuBinding

    def __repr__(self):
        return f'<TUISpecificStrategicHUDHeaderViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentDescriptor', 'MainComponentContainerUniqueName', 'CancelMenuBinding']]) + '>'


class TUISpecificStrategicObjectiveBriefViewDescriptor:
    def __init__(self, MainComponentDescriptor=None, MainComponentContainerUniqueName=None, NationaliteFlagTextures=None, TextColorByObjectiveState=None):
        self.MainComponentDescriptor = MainComponentDescriptor
        self.MainComponentContainerUniqueName = MainComponentContainerUniqueName
        self.NationaliteFlagTextures = NationaliteFlagTextures
        self.TextColorByObjectiveState = TextColorByObjectiveState

    def __repr__(self):
        return f'<TUISpecificStrategicObjectiveBriefViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentDescriptor', 'MainComponentContainerUniqueName', 'NationaliteFlagTextures', 'TextColorByObjectiveState']]) + '>'


class TUISpecificStrategicObjectiveScoreViewDescriptor:
    def __init__(self, MainComponentDescriptor=None, MainComponentContainerUniqueName=None, NationaliteTextureTokens=None):
        self.MainComponentDescriptor = MainComponentDescriptor
        self.MainComponentContainerUniqueName = MainComponentContainerUniqueName
        self.NationaliteTextureTokens = NationaliteTextureTokens

    def __repr__(self):
        return f'<TUISpecificStrategicObjectiveScoreViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentDescriptor', 'MainComponentContainerUniqueName', 'NationaliteTextureTokens']]) + '>'


class TBUCKLocalLayerContainerDescriptor:
    def __init__(self, ComponentFrame=None, NbLayersToLock=None, ChildFitToContent=None, Components=None):
        self.ComponentFrame = ComponentFrame
        self.NbLayersToLock = NbLayersToLock
        self.ChildFitToContent = ChildFitToContent
        self.Components = Components

    def __repr__(self):
        return f'<TBUCKLocalLayerContainerDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ComponentFrame', 'NbLayersToLock', 'ChildFitToContent', 'Components']]) + '>'


class PowerValueContainer:
    def __init__(self, TextColorToken=None, ElementName=None, BackgroundBlockColorToken=None, TextToken=None):
        self.TextColorToken = TextColorToken
        self.ElementName = ElementName
        self.BackgroundBlockColorToken = BackgroundBlockColorToken
        self.TextToken = TextToken

    def __repr__(self):
        return f'<PowerValueContainer ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TextColorToken', 'ElementName', 'BackgroundBlockColorToken', 'TextToken']]) + '>'


class TUISpecificStrategicPlayerNameDisplayViewDescriptor:
    def __init__(self, MainComponentDescriptor=None):
        self.MainComponentDescriptor = MainComponentDescriptor

    def __repr__(self):
        return f'<TUISpecificStrategicPlayerNameDisplayViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentDescriptor']]) + '>'


class TUISpecificStrategicPlayerTurnCheckerResources:
    def __init__(self, LDHintComponentName=None, LDHintTextComponentNameToFill=None, LDHintDuration=None, PlayerTurnToken=None, OtherPlayerTurnToken=None):
        self.LDHintComponentName = LDHintComponentName
        self.LDHintTextComponentNameToFill = LDHintTextComponentNameToFill
        self.LDHintDuration = LDHintDuration
        self.PlayerTurnToken = PlayerTurnToken
        self.OtherPlayerTurnToken = OtherPlayerTurnToken

    def __repr__(self):
        return f'<TUISpecificStrategicPlayerTurnCheckerResources ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['LDHintComponentName', 'LDHintTextComponentNameToFill', 'LDHintDuration', 'PlayerTurnToken', 'OtherPlayerTurnToken']]) + '>'


class TUISpecificStrategicSpawnPointViewDescriptor:
    def __init__(self, MainComponentDescriptor=None, LabelsLayer=None, LabelsTransformation=None, TransparencyForNotSelectedReinforcementGroup=None, ColorTokenSpawnCapturedByEnemy=None, ColorTokenSpawnCapturedByLocalPlayer=None, ColorTokenSpawnPointMain=None, BlinkingFlagPeriod=None):
        self.MainComponentDescriptor = MainComponentDescriptor
        self.LabelsLayer = LabelsLayer
        self.LabelsTransformation = LabelsTransformation
        self.TransparencyForNotSelectedReinforcementGroup = TransparencyForNotSelectedReinforcementGroup
        self.ColorTokenSpawnCapturedByEnemy = ColorTokenSpawnCapturedByEnemy
        self.ColorTokenSpawnCapturedByLocalPlayer = ColorTokenSpawnCapturedByLocalPlayer
        self.ColorTokenSpawnPointMain = ColorTokenSpawnPointMain
        self.BlinkingFlagPeriod = BlinkingFlagPeriod

    def __repr__(self):
        return f'<TUISpecificStrategicSpawnPointViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentDescriptor', 'LabelsLayer', 'LabelsTransformation', 'TransparencyForNotSelectedReinforcementGroup', 'ColorTokenSpawnCapturedByEnemy', 'ColorTokenSpawnCapturedByLocalPlayer', 'ColorTokenSpawnPointMain', 'BlinkingFlagPeriod']]) + '>'


class BoutonStartBattle:
    def __init__(self, SpotlightUniqueName=None, Mapping=None, MagnifiableWidthHeight=None, TextToken=None, HintBodyToken=None, ElementName=None):
        self.SpotlightUniqueName = SpotlightUniqueName
        self.Mapping = Mapping
        self.MagnifiableWidthHeight = MagnifiableWidthHeight
        self.TextToken = TextToken
        self.HintBodyToken = HintBodyToken
        self.ElementName = ElementName

    def __repr__(self):
        return f'<BoutonStartBattle ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['SpotlightUniqueName', 'Mapping', 'MagnifiableWidthHeight', 'TextToken', 'HintBodyToken', 'ElementName']]) + '>'


class StrategicSecondaryCubeActionPanel:
    def __init__(self, ComponentFrame=None, ContentComponents=None):
        self.ComponentFrame = ComponentFrame
        self.ContentComponents = ContentComponents

    def __repr__(self):
        return f'<StrategicSecondaryCubeActionPanel ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['ComponentFrame', 'ContentComponents']]) + '>'


class TStrategicBattlePlanningResources:
    def __init__(self, MainComponent=None):
        self.MainComponent = MainComponent

    def __repr__(self):
        return f'<TStrategicBattlePlanningResources ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponent']]) + '>'


class TUIStrategicEndTurnResources:
    def __init__(self, MainComponent=None):
        self.MainComponent = MainComponent

    def __repr__(self):
        return f'<TUIStrategicEndTurnResources ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponent']]) + '>'


class Steelman_newLDHINT:
    def __init__(self, Texture=None, portrait_name=None, width=None):
        self.Texture = Texture
        self.portrait_name = portrait_name
        self.width = width

    def __repr__(self):
        return f'<Steelman_newLDHINT ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Texture', 'portrait_name', 'width']]) + '>'


class ST_Component_1Texture_1Text_Portrait:
    def __init__(self, portrait_name=None):
        self.portrait_name = portrait_name

    def __repr__(self):
        return f'<ST_Component_1Texture_1Text_Portrait ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['portrait_name']]) + '>'


class Steelman_LDHint_Portrait:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<Steelman_LDHint_Portrait>'


class FullScreenImageEtTexte:
    def __init__(self, TextureToken=None):
        self.TextureToken = TextureToken

    def __repr__(self):
        return f'<FullScreenImageEtTexte ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TextureToken']]) + '>'


class ST_Component_1Texture_1Text:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<ST_Component_1Texture_1Text>'


class ST_Popup_1Texture_5Text:
    def __init__(self):
        pass

    def __repr__(self):
        return f'<ST_Popup_1Texture_5Text>'


class EndgameResultAnimationStrategic:
    def __init__(self, victory=None, draw=None):
        self.victory = victory
        self.draw = draw

    def __repr__(self):
        return f'<EndgameResultAnimationStrategic ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['victory', 'draw']]) + '>'


class Steelman_video:
    def __init__(self, TextureToken=None):
        self.TextureToken = TextureToken

    def __repr__(self):
        return f'<Steelman_video ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TextureToken']]) + '>'


class Template_HardwareMouseWidgetResource:
    def __init__(self, HardwareMouseCursorAnimation=None):
        self.HardwareMouseCursorAnimation = HardwareMouseCursorAnimation

    def __repr__(self):
        return f'<Template_HardwareMouseWidgetResource ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['HardwareMouseCursorAnimation']]) + '>'


class Template_HardwareMouseWidgetResource_WithTerrainFeedback:
    def __init__(self, StillTimeBeforeHintAppearance=None, TerrainTypeToHintContent=None, TerrainTypeToMouseCursorAnimation=None):
        self.StillTimeBeforeHintAppearance = StillTimeBeforeHintAppearance
        self.TerrainTypeToHintContent = TerrainTypeToHintContent
        self.TerrainTypeToMouseCursorAnimation = TerrainTypeToMouseCursorAnimation

    def __repr__(self):
        return f'<Template_HardwareMouseWidgetResource_WithTerrainFeedback ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['StillTimeBeforeHintAppearance', 'TerrainTypeToHintContent', 'TerrainTypeToMouseCursorAnimation']]) + '>'


class THintContentHolder:
    def __init__(self, BodyToken=None, TitleToken=None, ExtendedToken=None):
        self.BodyToken = BodyToken
        self.TitleToken = TitleToken
        self.ExtendedToken = ExtendedToken

    def __repr__(self):
        return f'<THintContentHolder ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['BodyToken', 'TitleToken', 'ExtendedToken']]) + '>'


class TUISpecificStrategicResources:
    def __init__(self, Handler=None, UILayer=None, UILayerLDHint=None, CommonResources=None, MainStyleGuides=None, ViewDescriptors=None, MainContainerResource=None, CommonHUDResources=None, LabelResource=None, GabaritResources=None, ZoCResources=None, WarningPanelResources=None, LabelsOnMapResources=None, ScriptedLabelResources=None, FeedbackManagerDescriptor=None, UnitLabelResource=None, FlareLabelResources=None, SelectionHandlerInGameResources=None, GroupSelectionReminderResources=None, PositionEvents=None, MousePolicyManagerResources=None, OptionManager=None, ShortcutUserInputLayer=None, LDScriptUserInputLayer=None, DisplayAllOrdersMapping=None, StrategicOrderDisplayResources=None, EndTurnResources=None, AutoResolveResources=None, StartBattleResources=None, BattlePlanningResources=None, ConnectedPlayersResources=None, PlayerNameDisplayDescriptor=None, StrategicBattleResources=None, PlayerTurnCheckerResources=None, WorldFloorRegistry=None):
        self.Handler = Handler
        self.UILayer = UILayer
        self.UILayerLDHint = UILayerLDHint
        self.CommonResources = CommonResources
        self.MainStyleGuides = MainStyleGuides
        self.ViewDescriptors = ViewDescriptors
        self.MainContainerResource = MainContainerResource
        self.CommonHUDResources = CommonHUDResources
        self.LabelResource = LabelResource
        self.GabaritResources = GabaritResources
        self.ZoCResources = ZoCResources
        self.WarningPanelResources = WarningPanelResources
        self.LabelsOnMapResources = LabelsOnMapResources
        self.ScriptedLabelResources = ScriptedLabelResources
        self.FeedbackManagerDescriptor = FeedbackManagerDescriptor
        self.UnitLabelResource = UnitLabelResource
        self.FlareLabelResources = FlareLabelResources
        self.SelectionHandlerInGameResources = SelectionHandlerInGameResources
        self.GroupSelectionReminderResources = GroupSelectionReminderResources
        self.PositionEvents = PositionEvents
        self.MousePolicyManagerResources = MousePolicyManagerResources
        self.OptionManager = OptionManager
        self.ShortcutUserInputLayer = ShortcutUserInputLayer
        self.LDScriptUserInputLayer = LDScriptUserInputLayer
        self.DisplayAllOrdersMapping = DisplayAllOrdersMapping
        self.StrategicOrderDisplayResources = StrategicOrderDisplayResources
        self.EndTurnResources = EndTurnResources
        self.AutoResolveResources = AutoResolveResources
        self.StartBattleResources = StartBattleResources
        self.BattlePlanningResources = BattlePlanningResources
        self.ConnectedPlayersResources = ConnectedPlayersResources
        self.PlayerNameDisplayDescriptor = PlayerNameDisplayDescriptor
        self.StrategicBattleResources = StrategicBattleResources
        self.PlayerTurnCheckerResources = PlayerTurnCheckerResources
        self.WorldFloorRegistry = WorldFloorRegistry

    def __repr__(self):
        return f'<TUISpecificStrategicResources ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Handler', 'UILayer', 'UILayerLDHint', 'CommonResources', 'MainStyleGuides', 'ViewDescriptors', 'MainContainerResource', 'CommonHUDResources', 'LabelResource', 'GabaritResources', 'ZoCResources', 'WarningPanelResources', 'LabelsOnMapResources', 'ScriptedLabelResources', 'FeedbackManagerDescriptor', 'UnitLabelResource', 'FlareLabelResources', 'SelectionHandlerInGameResources', 'GroupSelectionReminderResources', 'PositionEvents', 'MousePolicyManagerResources', 'OptionManager', 'ShortcutUserInputLayer', 'LDScriptUserInputLayer', 'DisplayAllOrdersMapping', 'StrategicOrderDisplayResources', 'EndTurnResources', 'AutoResolveResources', 'StartBattleResources', 'BattlePlanningResources', 'ConnectedPlayersResources', 'PlayerNameDisplayDescriptor', 'StrategicBattleResources', 'PlayerTurnCheckerResources', 'WorldFloorRegistry']]) + '>'


class UISpecificSelectionPanelPawnViewDescriptorTemplate:
    def __init__(self, MainComponentContainerUniqueName=None, ContainsCubeAction=None, HasSpotlight=None):
        self.MainComponentContainerUniqueName = MainComponentContainerUniqueName
        self.ContainsCubeAction = ContainsCubeAction
        self.HasSpotlight = HasSpotlight

    def __repr__(self):
        return f'<UISpecificSelectionPanelPawnViewDescriptorTemplate ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentContainerUniqueName', 'ContainsCubeAction', 'HasSpotlight']]) + '>'


class TStrategicOrderDisplayResources:
    def __init__(self, Camera=None, OrderDisplayUserInputLayer=None, OrderDisplayDrawer=None, PhaseLabelDescriptor=None):
        self.Camera = Camera
        self.OrderDisplayUserInputLayer = OrderDisplayUserInputLayer
        self.OrderDisplayDrawer = OrderDisplayDrawer
        self.PhaseLabelDescriptor = PhaseLabelDescriptor

    def __repr__(self):
        return f'<TStrategicOrderDisplayResources ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['Camera', 'OrderDisplayUserInputLayer', 'OrderDisplayDrawer', 'PhaseLabelDescriptor']]) + '>'


class TStrategicOrderDisplayDrawer:
    def __init__(self, OrderDisplayDrawInfo=None):
        self.OrderDisplayDrawInfo = OrderDisplayDrawInfo

    def __repr__(self):
        return f'<TStrategicOrderDisplayDrawer ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['OrderDisplayDrawInfo']]) + '>'


class TStrategicOrderDisplayDrawInfo:
    def __init__(self, LineThickness=None, ArrowLength=None, ArrowWidth=None, ArrowLineWidth=None, ArrowFadeLength=None):
        self.LineThickness = LineThickness
        self.ArrowLength = ArrowLength
        self.ArrowWidth = ArrowWidth
        self.ArrowLineWidth = ArrowLineWidth
        self.ArrowFadeLength = ArrowFadeLength

    def __repr__(self):
        return f'<TStrategicOrderDisplayDrawInfo ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['LineThickness', 'ArrowLength', 'ArrowWidth', 'ArrowLineWidth', 'ArrowFadeLength']]) + '>'


class TUISpecificCubeActionViewDescriptor:
    def __init__(self, MainComponentDescriptor=None, MainComponentContainerUniqueName=None, ButtonTemplateDescriptorMap=None, EmptyButtonTemplateDescriptor=None, SpotlightDescriptor=None):
        self.MainComponentDescriptor = MainComponentDescriptor
        self.MainComponentContainerUniqueName = MainComponentContainerUniqueName
        self.ButtonTemplateDescriptorMap = ButtonTemplateDescriptorMap
        self.EmptyButtonTemplateDescriptor = EmptyButtonTemplateDescriptor
        self.SpotlightDescriptor = SpotlightDescriptor

    def __repr__(self):
        return f'<TUISpecificCubeActionViewDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['MainComponentDescriptor', 'MainComponentContainerUniqueName', 'ButtonTemplateDescriptorMap', 'EmptyButtonTemplateDescriptor', 'SpotlightDescriptor']]) + '>'


class CubeActionButton:
    def __init__(self, BackgroundBlockColorToken=None, BorderLineColorToken=None, RoundedVertexes=None, BigLineAction=None, HintableAreaComponent=None):
        self.BackgroundBlockColorToken = BackgroundBlockColorToken
        self.BorderLineColorToken = BorderLineColorToken
        self.RoundedVertexes = RoundedVertexes
        self.BigLineAction = BigLineAction
        self.HintableAreaComponent = HintableAreaComponent

    def __repr__(self):
        return f'<CubeActionButton ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['BackgroundBlockColorToken', 'BorderLineColorToken', 'RoundedVertexes', 'BigLineAction', 'HintableAreaComponent']]) + '>'


class CubeActionToggleButton:
    def __init__(self, BigLineAction=None):
        self.BigLineAction = BigLineAction

    def __repr__(self):
        return f'<CubeActionToggleButton ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['BigLineAction']]) + '>'


class TUISpecificUnitLabelResources:
    def __init__(self, UILayer=None, UI3DLayer=None, Camera=None, CameraMoverHelperProxy=None, FadeFactorForShaderParameter=None, OpacityControlByFloat=None, UI3DTransformation=None):
        self.UILayer = UILayer
        self.UI3DLayer = UI3DLayer
        self.Camera = Camera
        self.CameraMoverHelperProxy = CameraMoverHelperProxy
        self.FadeFactorForShaderParameter = FadeFactorForShaderParameter
        self.OpacityControlByFloat = OpacityControlByFloat
        self.UI3DTransformation = UI3DTransformation

    def __repr__(self):
        return f'<TUISpecificUnitLabelResources ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['UILayer', 'UI3DLayer', 'Camera', 'CameraMoverHelperProxy', 'FadeFactorForShaderParameter', 'OpacityControlByFloat', 'UI3DTransformation']]) + '>'
