# -*- coding: utf-8 -*-
# :Project:   pglast -- DO NOT EDIT: automatically extracted from nodes.h @ 10-1.0.2-0-gd710cb0
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017-2019 Lele Gaifax
#

try:
    from enum import Enum, IntEnum, IntFlag, auto
except ImportError: #pragma: no cover
    # Python < 3.6
    from aenum import Enum, IntEnum, IntFlag, auto


class AggSplit(IntEnum):
    AGGSPLIT_SIMPLE = 0
    AGGSPLIT_INITIAL_SERIAL = 0x02 | 0x04
    AGGSPLIT_FINAL_DESERIAL = 0x01 | 0x08

class AggStrategy(IntEnum):
    AGG_PLAIN = 0
    AGG_SORTED = auto()
    AGG_HASHED = auto()
    AGG_MIXED = auto()

class CmdType(IntEnum):
    CMD_UNKNOWN = 0
    CMD_SELECT = auto()
    CMD_UPDATE = auto()
    CMD_INSERT = auto()
    CMD_DELETE = auto()
    CMD_UTILITY = auto()
    CMD_NOTHING = auto()

class JoinType(IntEnum):
    JOIN_INNER = 0
    JOIN_LEFT = auto()
    JOIN_FULL = auto()
    JOIN_RIGHT = auto()
    JOIN_SEMI = auto()
    JOIN_ANTI = auto()
    JOIN_UNIQUE_OUTER = auto()
    JOIN_UNIQUE_INNER = auto()

class NodeTag(IntEnum):
    T_Invalid = 0
    T_IndexInfo = auto()
    T_ExprContext = auto()
    T_ProjectionInfo = auto()
    T_JunkFilter = auto()
    T_ResultRelInfo = auto()
    T_EState = auto()
    T_TupleTableSlot = auto()
    T_Plan = auto()
    T_Result = auto()
    T_ProjectSet = auto()
    T_ModifyTable = auto()
    T_Append = auto()
    T_MergeAppend = auto()
    T_RecursiveUnion = auto()
    T_BitmapAnd = auto()
    T_BitmapOr = auto()
    T_Scan = auto()
    T_SeqScan = auto()
    T_SampleScan = auto()
    T_IndexScan = auto()
    T_IndexOnlyScan = auto()
    T_BitmapIndexScan = auto()
    T_BitmapHeapScan = auto()
    T_TidScan = auto()
    T_SubqueryScan = auto()
    T_FunctionScan = auto()
    T_ValuesScan = auto()
    T_TableFuncScan = auto()
    T_CteScan = auto()
    T_NamedTuplestoreScan = auto()
    T_WorkTableScan = auto()
    T_ForeignScan = auto()
    T_CustomScan = auto()
    T_Join = auto()
    T_NestLoop = auto()
    T_MergeJoin = auto()
    T_HashJoin = auto()
    T_Material = auto()
    T_Sort = auto()
    T_Group = auto()
    T_Agg = auto()
    T_WindowAgg = auto()
    T_Unique = auto()
    T_Gather = auto()
    T_GatherMerge = auto()
    T_Hash = auto()
    T_SetOp = auto()
    T_LockRows = auto()
    T_Limit = auto()
    T_NestLoopParam = auto()
    T_PlanRowMark = auto()
    T_PlanInvalItem = auto()
    T_PlanState = auto()
    T_ResultState = auto()
    T_ProjectSetState = auto()
    T_ModifyTableState = auto()
    T_AppendState = auto()
    T_MergeAppendState = auto()
    T_RecursiveUnionState = auto()
    T_BitmapAndState = auto()
    T_BitmapOrState = auto()
    T_ScanState = auto()
    T_SeqScanState = auto()
    T_SampleScanState = auto()
    T_IndexScanState = auto()
    T_IndexOnlyScanState = auto()
    T_BitmapIndexScanState = auto()
    T_BitmapHeapScanState = auto()
    T_TidScanState = auto()
    T_SubqueryScanState = auto()
    T_FunctionScanState = auto()
    T_TableFuncScanState = auto()
    T_ValuesScanState = auto()
    T_CteScanState = auto()
    T_NamedTuplestoreScanState = auto()
    T_WorkTableScanState = auto()
    T_ForeignScanState = auto()
    T_CustomScanState = auto()
    T_JoinState = auto()
    T_NestLoopState = auto()
    T_MergeJoinState = auto()
    T_HashJoinState = auto()
    T_MaterialState = auto()
    T_SortState = auto()
    T_GroupState = auto()
    T_AggState = auto()
    T_WindowAggState = auto()
    T_UniqueState = auto()
    T_GatherState = auto()
    T_GatherMergeState = auto()
    T_HashState = auto()
    T_SetOpState = auto()
    T_LockRowsState = auto()
    T_LimitState = auto()
    T_Alias = auto()
    T_RangeVar = auto()
    T_TableFunc = auto()
    T_Expr = auto()
    T_Var = auto()
    T_Const = auto()
    T_Param = auto()
    T_Aggref = auto()
    T_GroupingFunc = auto()
    T_WindowFunc = auto()
    T_ArrayRef = auto()
    T_FuncExpr = auto()
    T_NamedArgExpr = auto()
    T_OpExpr = auto()
    T_DistinctExpr = auto()
    T_NullIfExpr = auto()
    T_ScalarArrayOpExpr = auto()
    T_BoolExpr = auto()
    T_SubLink = auto()
    T_SubPlan = auto()
    T_AlternativeSubPlan = auto()
    T_FieldSelect = auto()
    T_FieldStore = auto()
    T_RelabelType = auto()
    T_CoerceViaIO = auto()
    T_ArrayCoerceExpr = auto()
    T_ConvertRowtypeExpr = auto()
    T_CollateExpr = auto()
    T_CaseExpr = auto()
    T_CaseWhen = auto()
    T_CaseTestExpr = auto()
    T_ArrayExpr = auto()
    T_RowExpr = auto()
    T_RowCompareExpr = auto()
    T_CoalesceExpr = auto()
    T_MinMaxExpr = auto()
    T_SQLValueFunction = auto()
    T_XmlExpr = auto()
    T_NullTest = auto()
    T_BooleanTest = auto()
    T_CoerceToDomain = auto()
    T_CoerceToDomainValue = auto()
    T_SetToDefault = auto()
    T_CurrentOfExpr = auto()
    T_NextValueExpr = auto()
    T_InferenceElem = auto()
    T_TargetEntry = auto()
    T_RangeTblRef = auto()
    T_JoinExpr = auto()
    T_FromExpr = auto()
    T_OnConflictExpr = auto()
    T_IntoClause = auto()
    T_ExprState = auto()
    T_AggrefExprState = auto()
    T_WindowFuncExprState = auto()
    T_SetExprState = auto()
    T_SubPlanState = auto()
    T_AlternativeSubPlanState = auto()
    T_DomainConstraintState = auto()
    T_PlannerInfo = auto()
    T_PlannerGlobal = auto()
    T_RelOptInfo = auto()
    T_IndexOptInfo = auto()
    T_ForeignKeyOptInfo = auto()
    T_ParamPathInfo = auto()
    T_Path = auto()
    T_IndexPath = auto()
    T_BitmapHeapPath = auto()
    T_BitmapAndPath = auto()
    T_BitmapOrPath = auto()
    T_TidPath = auto()
    T_SubqueryScanPath = auto()
    T_ForeignPath = auto()
    T_CustomPath = auto()
    T_NestPath = auto()
    T_MergePath = auto()
    T_HashPath = auto()
    T_AppendPath = auto()
    T_MergeAppendPath = auto()
    T_ResultPath = auto()
    T_MaterialPath = auto()
    T_UniquePath = auto()
    T_GatherPath = auto()
    T_GatherMergePath = auto()
    T_ProjectionPath = auto()
    T_ProjectSetPath = auto()
    T_SortPath = auto()
    T_GroupPath = auto()
    T_UpperUniquePath = auto()
    T_AggPath = auto()
    T_GroupingSetsPath = auto()
    T_MinMaxAggPath = auto()
    T_WindowAggPath = auto()
    T_SetOpPath = auto()
    T_RecursiveUnionPath = auto()
    T_LockRowsPath = auto()
    T_ModifyTablePath = auto()
    T_LimitPath = auto()
    T_EquivalenceClass = auto()
    T_EquivalenceMember = auto()
    T_PathKey = auto()
    T_PathTarget = auto()
    T_RestrictInfo = auto()
    T_PlaceHolderVar = auto()
    T_SpecialJoinInfo = auto()
    T_AppendRelInfo = auto()
    T_PartitionedChildRelInfo = auto()
    T_PlaceHolderInfo = auto()
    T_MinMaxAggInfo = auto()
    T_PlannerParamItem = auto()
    T_RollupData = auto()
    T_GroupingSetData = auto()
    T_StatisticExtInfo = auto()
    T_MemoryContext = auto()
    T_AllocSetContext = auto()
    T_SlabContext = auto()
    T_Value = auto()
    T_Integer = auto()
    T_Float = auto()
    T_String = auto()
    T_BitString = auto()
    T_Null = auto()
    T_List = auto()
    T_IntList = auto()
    T_OidList = auto()
    T_ExtensibleNode = auto()
    T_RawStmt = auto()
    T_Query = auto()
    T_PlannedStmt = auto()
    T_InsertStmt = auto()
    T_DeleteStmt = auto()
    T_UpdateStmt = auto()
    T_SelectStmt = auto()
    T_AlterTableStmt = auto()
    T_AlterTableCmd = auto()
    T_AlterDomainStmt = auto()
    T_SetOperationStmt = auto()
    T_GrantStmt = auto()
    T_GrantRoleStmt = auto()
    T_AlterDefaultPrivilegesStmt = auto()
    T_ClosePortalStmt = auto()
    T_ClusterStmt = auto()
    T_CopyStmt = auto()
    T_CreateStmt = auto()
    T_DefineStmt = auto()
    T_DropStmt = auto()
    T_TruncateStmt = auto()
    T_CommentStmt = auto()
    T_FetchStmt = auto()
    T_IndexStmt = auto()
    T_CreateFunctionStmt = auto()
    T_AlterFunctionStmt = auto()
    T_DoStmt = auto()
    T_RenameStmt = auto()
    T_RuleStmt = auto()
    T_NotifyStmt = auto()
    T_ListenStmt = auto()
    T_UnlistenStmt = auto()
    T_TransactionStmt = auto()
    T_ViewStmt = auto()
    T_LoadStmt = auto()
    T_CreateDomainStmt = auto()
    T_CreatedbStmt = auto()
    T_DropdbStmt = auto()
    T_VacuumStmt = auto()
    T_ExplainStmt = auto()
    T_CreateTableAsStmt = auto()
    T_CreateSeqStmt = auto()
    T_AlterSeqStmt = auto()
    T_VariableSetStmt = auto()
    T_VariableShowStmt = auto()
    T_DiscardStmt = auto()
    T_CreateTrigStmt = auto()
    T_CreatePLangStmt = auto()
    T_CreateRoleStmt = auto()
    T_AlterRoleStmt = auto()
    T_DropRoleStmt = auto()
    T_LockStmt = auto()
    T_ConstraintsSetStmt = auto()
    T_ReindexStmt = auto()
    T_CheckPointStmt = auto()
    T_CreateSchemaStmt = auto()
    T_AlterDatabaseStmt = auto()
    T_AlterDatabaseSetStmt = auto()
    T_AlterRoleSetStmt = auto()
    T_CreateConversionStmt = auto()
    T_CreateCastStmt = auto()
    T_CreateOpClassStmt = auto()
    T_CreateOpFamilyStmt = auto()
    T_AlterOpFamilyStmt = auto()
    T_PrepareStmt = auto()
    T_ExecuteStmt = auto()
    T_DeallocateStmt = auto()
    T_DeclareCursorStmt = auto()
    T_CreateTableSpaceStmt = auto()
    T_DropTableSpaceStmt = auto()
    T_AlterObjectDependsStmt = auto()
    T_AlterObjectSchemaStmt = auto()
    T_AlterOwnerStmt = auto()
    T_AlterOperatorStmt = auto()
    T_DropOwnedStmt = auto()
    T_ReassignOwnedStmt = auto()
    T_CompositeTypeStmt = auto()
    T_CreateEnumStmt = auto()
    T_CreateRangeStmt = auto()
    T_AlterEnumStmt = auto()
    T_AlterTSDictionaryStmt = auto()
    T_AlterTSConfigurationStmt = auto()
    T_CreateFdwStmt = auto()
    T_AlterFdwStmt = auto()
    T_CreateForeignServerStmt = auto()
    T_AlterForeignServerStmt = auto()
    T_CreateUserMappingStmt = auto()
    T_AlterUserMappingStmt = auto()
    T_DropUserMappingStmt = auto()
    T_AlterTableSpaceOptionsStmt = auto()
    T_AlterTableMoveAllStmt = auto()
    T_SecLabelStmt = auto()
    T_CreateForeignTableStmt = auto()
    T_ImportForeignSchemaStmt = auto()
    T_CreateExtensionStmt = auto()
    T_AlterExtensionStmt = auto()
    T_AlterExtensionContentsStmt = auto()
    T_CreateEventTrigStmt = auto()
    T_AlterEventTrigStmt = auto()
    T_RefreshMatViewStmt = auto()
    T_ReplicaIdentityStmt = auto()
    T_AlterSystemStmt = auto()
    T_CreatePolicyStmt = auto()
    T_AlterPolicyStmt = auto()
    T_CreateTransformStmt = auto()
    T_CreateAmStmt = auto()
    T_CreatePublicationStmt = auto()
    T_AlterPublicationStmt = auto()
    T_CreateSubscriptionStmt = auto()
    T_AlterSubscriptionStmt = auto()
    T_DropSubscriptionStmt = auto()
    T_CreateStatsStmt = auto()
    T_AlterCollationStmt = auto()
    T_A_Expr = auto()
    T_ColumnRef = auto()
    T_ParamRef = auto()
    T_A_Const = auto()
    T_FuncCall = auto()
    T_A_Star = auto()
    T_A_Indices = auto()
    T_A_Indirection = auto()
    T_A_ArrayExpr = auto()
    T_ResTarget = auto()
    T_MultiAssignRef = auto()
    T_TypeCast = auto()
    T_CollateClause = auto()
    T_SortBy = auto()
    T_WindowDef = auto()
    T_RangeSubselect = auto()
    T_RangeFunction = auto()
    T_RangeTableSample = auto()
    T_RangeTableFunc = auto()
    T_RangeTableFuncCol = auto()
    T_TypeName = auto()
    T_ColumnDef = auto()
    T_IndexElem = auto()
    T_Constraint = auto()
    T_DefElem = auto()
    T_RangeTblEntry = auto()
    T_RangeTblFunction = auto()
    T_TableSampleClause = auto()
    T_WithCheckOption = auto()
    T_SortGroupClause = auto()
    T_GroupingSet = auto()
    T_WindowClause = auto()
    T_ObjectWithArgs = auto()
    T_AccessPriv = auto()
    T_CreateOpClassItem = auto()
    T_TableLikeClause = auto()
    T_FunctionParameter = auto()
    T_LockingClause = auto()
    T_RowMarkClause = auto()
    T_XmlSerialize = auto()
    T_WithClause = auto()
    T_InferClause = auto()
    T_OnConflictClause = auto()
    T_CommonTableExpr = auto()
    T_RoleSpec = auto()
    T_TriggerTransition = auto()
    T_PartitionElem = auto()
    T_PartitionSpec = auto()
    T_PartitionBoundSpec = auto()
    T_PartitionRangeDatum = auto()
    T_PartitionCmd = auto()
    T_IdentifySystemCmd = auto()
    T_BaseBackupCmd = auto()
    T_CreateReplicationSlotCmd = auto()
    T_DropReplicationSlotCmd = auto()
    T_StartReplicationCmd = auto()
    T_TimeLineHistoryCmd = auto()
    T_SQLCmd = auto()
    T_TriggerData = auto()
    T_EventTriggerData = auto()
    T_ReturnSetInfo = auto()
    T_WindowObjectData = auto()
    T_TIDBitmap = auto()
    T_InlineCodeBlock = auto()
    T_FdwRoutine = auto()
    T_IndexAmRoutine = auto()
    T_TsmRoutine = auto()
    T_ForeignKeyCacheInfo = auto()

class OnConflictAction(IntEnum):
    ONCONFLICT_NONE = 0
    ONCONFLICT_NOTHING = auto()
    ONCONFLICT_UPDATE = auto()

class SetOpCmd(IntEnum):
    SETOPCMD_INTERSECT = 0
    SETOPCMD_INTERSECT_ALL = auto()
    SETOPCMD_EXCEPT = auto()
    SETOPCMD_EXCEPT_ALL = auto()

class SetOpStrategy(IntEnum):
    SETOP_SORTED = 0
    SETOP_HASHED = auto()


# #define-ed constants

AGGSPLITOP_COMBINE = 0x01

AGGSPLITOP_SKIPFINAL = 0x02

AGGSPLITOP_SERIALIZE = 0x04

AGGSPLITOP_DESERIALIZE = 0x08
