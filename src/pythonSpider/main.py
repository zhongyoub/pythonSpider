#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
#import urllib2, httplib
from bs4 import BeautifulSoup as bs
import xlwt
#httplib.HTTPConnection._http_vsn = 10
#httplib.HTTPConnection._http_vsn_str = 'HTTP/1.1'

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36', \
"Cookie":"COVJSESSIONID8080CB=733349AA9F5D56F3785A9F2E01B88B70",\
"Host":"localhost:8080","Origin":"http://localhost:8080",\
"Referer":"http://localhost:8080/login/login.htm",\
"Accept-Language":"zh-CN,zh;q=0.8",\
"Accept-Encoding":"gzip, deflate, sdch",\
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",\
"Connection":"keep-alive","Cache-Control":"max-age=0"
}

cookies = {'COVJSESSIONID8080CB':'733349AA9F5D56F3785A9F2E01B88B70'}

style = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',num_format_str='#,##0.00')
wb = xlwt.Workbook(encoding='utf-8')

impact = { "High": "��Σ".decode('gbk'), "Medium" : "��Σ".decode('gbk') , "Low": "��Σ".decode('gbk')}

def set_style(name,height,bold=False, align="center"):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font

    alignment = xlwt.Alignment()
    if align == "center":
        alignment.horz = xlwt.Alignment.HORZ_CENTER
    else:
        alignment.horz = xlwt.Alignment.HORZ_LEFT
    alignment.vert = xlwt.Alignment.VERT_CENTER
    style.alignment = alignment
    return style

def main():
    global wb
    #login()
    projs = get_projects()
    for pj in projs:
        print(pj["id"], pj["label"])
        vid = get_viewid(pj["id"])
        get_table(pj["label"], pj["id"], vid)
    wb.save("chinaoil.csv")

def get_table(app, pid, vid):
    url = "http://localhost:8080/reports/table.json?projectId="+str(pid)+"&viewId="+str(vid)
    print(url)
    """
    global cookies
    s = requests.Session()
    rsp = s.get(url, cookies=cookies)
    if rsp.status_code != 200:
        print "get_projects failed: %d" % (rsp.status_code)
        return
    print rsp.text
    """
    msg = '{"activeViewKey":{"projectId":10003,"viewId":10026,"groupBy":false},"resultSet":{"offset":0,"overallCount":0,"selectedCount":0,"totalCount":16,"pageNum":1,"limit":200,"results":[{"id":10001,"cid":10001,"checker":"DEADCODE","status":"New","classification":"Unclassified","severity":"Unspecified","action":"Undecided","owner":"Unassigned","ownerId":-1,"displayFunction":"SaOrgDAO.queryCompanyInfo","displayFile":"/src/main/java/wl/petrochina/base/org/infrastructure/SaOrgDAO.java","firstDetected":"07/12/17","lastFixed":"07/12/17","lastDetected":"07/12/17","lastTriaged":"","subcategory":"","domain":"","externalReference":"","comment":"","mergeKey":"dc65236740c69a8232e1e7f9b7fb3c9b","displayComponent":"Other","firstSnapshotDate":"07/12/17","firstSnapshotId":10003,"firstSnapshotVersion":"","firstSnapshotTarget":"","firstSnapshotDescription":"","firstSnapshotStream":"wl.petrochina.base","lastDetectedId":10003,"lastDetectedVersion":"","lastDetectedTarget":"","lastDetectedDescription":"","lastDetectedStream":"wl.petrochina.base","occurrenceCount":1,"lastDefectInstanceId":1017,"displayImpact":"Medium","displayCategory":"Control flow issues","displayType":"Logically dead code","cwe":561,"fixTarget":"Untargeted","displayIssueKind":"Quality","ownerFullName":"","mergeExtra":"sb","functionMergeName":"wl.petrochina.base.org.infrastructure.SaOrgDAO.queryCompanyInfo(java.lang.String, java.lang.String)","legacy":"False","displayComparison":"Absent","displayFirstDetectedBy":"Snapshot","committed":true,"fileLanguage":"Java","ruleStrength":"None","fileInstanceId":4006,"projectId":10003,"pivotKey":"cid"},{"id":10002,"cid":10002,"checker":"DEADCODE","status":"New","classification":"Unclassified","severity":"Unspecified","action":"Undecided","owner":"Unassigned","ownerId":-1,"displayFunction":"BaseBusinessStationDAO.findPortStationInfo","displayFile":"/src/main/java/wl/petrochina/base/portstation/infrastructure/BaseBusinessStationDAO.java","firstDetected":"07/12/17","lastFixed":"07/12/17","lastDetected":"07/12/17","lastTriaged":"","subcategory":"","domain":"","externalReference":"","comment":"","mergeKey":"e0675a5b75e78632bd8058610778a2ae","displayComponent":"Other","firstSnapshotDate":"07/12/17","firstSnapshotId":10003,"firstSnapshotVersion":"","firstSnapshotTarget":"","firstSnapshotDescription":"","firstSnapshotStream":"wl.petrochina.base","lastDetectedId":10003,"lastDetectedVersion":"","lastDetectedTarget":"","lastDetectedDescription":"","lastDetectedStream":"wl.petrochina.base","occurrenceCount":1,"lastDefectInstanceId":1018,"displayImpact":"Medium","displayCategory":"Control flow issues","displayType":"Logically dead code","cwe":561,"fixTarget":"Untargeted","displayIssueKind":"Quality","ownerFullName":"","mergeExtra":"sb","functionMergeName":"wl.petrochina.base.portstation.infrastructure.BaseBusinessStationDAO.findPortStationInfo(java.lang.String, java.lang.String, java.lang.String)","legacy":"False","displayComparison":"Absent","displayFirstDetectedBy":"Snapshot","committed":true,"fileLanguage":"Java","ruleStrength":"None","fileInstanceId":3526,"projectId":10003,"pivotKey":"cid"},{"id":10003,"cid":10003,"checker":"FORWARD_NULL","status":"New","classification":"Unclassified","severity":"Unspecified","action":"Undecided","owner":"Unassigned","ownerId":-1,"displayFunction":"BaseBusStorageServiceImpl.findBusStorageInfo","displayFile":"/src/main/java/wl/petrochina/base/service/application/internal/BaseBusStorageServiceImpl.java","firstDetected":"07/12/17","lastFixed":"07/12/17","lastDetected":"07/12/17","lastTriaged":"","subcategory":"","domain":"","externalReference":"","comment":"","mergeKey":"cf82a47d0e0f6f10e011546e754915f1","displayComponent":"Other","firstSnapshotDate":"07/12/17","firstSnapshotId":10003,"firstSnapshotVersion":"","firstSnapshotTarget":"","firstSnapshotDescription":"","firstSnapshotStream":"wl.petrochina.base","lastDetectedId":10003,"lastDetectedVersion":"","lastDetectedTarget":"","lastDetectedDescription":"","lastDetectedStream":"wl.petrochina.base","occurrenceCount":1,"lastDefectInstanceId":1019,"displayImpact":"Medium","displayCategory":"Null pointer dereferences","displayType":"Explicit null dereferenced","cwe":476,"fixTarget":"Untargeted","displayIssueKind":"Quality","ownerFullName":"","mergeExtra":"st","functionMergeName":"wl.petrochina.base.service.application.internal.BaseBusStorageServiceImpl.findBusStorageInfo(java.lang.String, java.lang.String)","legacy":"False","displayComparison":"Absent","displayFirstDetectedBy":"Snapshot","committed":true,"fileLanguage":"Java","ruleStrength":"None","fileInstanceId":4011,"projectId":10003,"pivotKey":"cid"},{"id":10004,"cid":10004,"checker":"FORWARD_NULL","status":"New","classification":"Unclassified","severity":"Unspecified","action":"Undecided","owner":"Unassigned","ownerId":-1,"displayFunction":"PointOfDepartureServiceImpl.queryPointOfDeparture","displayFile":"/src/main/java/wl/petrochina/base/popupControl/sender/application/internal/internal/PointOfDepartureServiceImpl.java","firstDetected":"07/12/17","lastFixed":"07/12/17","lastDetected":"07/12/17","lastTriaged":"","subcategory":"","domain":"","externalReference":"","comment":"","mergeKey":"85ce3b5dda5fbd0184e5e56f5e68af66","displayComponent":"Other","firstSnapshotDate":"07/12/17","firstSnapshotId":10003,"firstSnapshotVersion":"","firstSnapshotTarget":"","firstSnapshotDescription":"","firstSnapshotStream":"wl.petrochina.base","lastDetectedId":10003,"lastDetectedVersion":"","lastDetectedTarget":"","lastDetectedDescription":"","lastDetectedStream":"wl.petrochina.base","occurrenceCount":1,"lastDefectInstanceId":1022,"displayImpact":"Medium","displayCategory":"Null pointer dereferences","displayType":"Explicit null dereferenced","cwe":476,"fixTarget":"Untargeted","displayIssueKind":"Quality","ownerFullName":"","mergeExtra":"st","functionMergeName":"wl.petrochina.base.popupControl.sender.application.internal.internal.PointOfDepartureServiceImpl.queryPointOfDeparture(java.lang.String, java.lang.String, java.lang.String)","legacy":"False","displayComparison":"Absent","displayFirstDetectedBy":"Snapshot","committed":true,"fileLanguage":"Java","ruleStrength":"None","fileInstanceId":4470,"projectId":10003,"pivotKey":"cid"},{"id":10005,"cid":10005,"checker":"FORWARD_NULL","status":"New","classification":"Unclassified","severity":"Unspecified","action":"Undecided","owner":"Unassigned","ownerId":-1,"displayFunction":"BasePlantDeviceServiceImpl.findCurrencyInfo","displayFile":"/src/main/java/wl/petrochina/base/service/application/internal/BasePlantDeviceServiceImpl.java","firstDetected":"07/12/17","lastFixed":"07/12/17","lastDetected":"07/12/17","lastTriaged":"","subcategory":"","domain":"","externalReference":"","comment":"","mergeKey":"a70a8ba64c720695a90afe51a8dff808","displayComponent":"Other","firstSnapshotDate":"07/12/17","firstSnapshotId":10003,"firstSnapshotVersion":"","firstSnapshotTarget":"","firstSnapshotDescription":"","firstSnapshotStream":"wl.petrochina.base","lastDetectedId":10003,"lastDetectedVersion":"","lastDetectedTarget":"","lastDetectedDescription":"","lastDetectedStream":"wl.petrochina.base","occurrenceCount":1,"lastDefectInstanceId":1020,"displayImpact":"Medium","displayCategory":"Null pointer dereferences","displayType":"Explicit null dereferenced","cwe":476,"fixTarget":"Untargeted","displayIssueKind":"Quality","ownerFullName":"","mergeExtra":"st","functionMergeName":"wl.petrochina.base.service.application.internal.BasePlantDeviceServiceImpl.findCurrencyInfo(java.lang.String, java.lang.String)","legacy":"False","displayComparison":"Absent","displayFirstDetectedBy":"Snapshot","committed":true,"fileLanguage":"Java","ruleStrength":"None","fileInstanceId":4612,"projectId":10003,"pivotKey":"cid"},{"id":10006,"cid":10006,"checker":"FORWARD_NULL","status":"New","classification":"Unclassified","severity":"Unspecified","action":"Undecided","owner":"Unassigned","ownerId":-1,"displayFunction":"HairStandingServiceImpl.queryHairStanding","displayFile":"/src/main/java/wl/petrochina/base/popupControl/sender/application/internal/internal/HairStandingServiceImpl.java","firstDetected":"07/12/17","lastFixed":"07/12/17","lastDetected":"07/12/17","lastTriaged":"","subcategory":"","domain":"","externalReference":"","comment":"","mergeKey":"36ac336c492132260b30ca762ffea61d","displayComponent":"Other","firstSnapshotDate":"07/12/17","firstSnapshotId":10003,"firstSnapshotVersion":"","firstSnapshotTarget":"","firstSnapshotDescription":"","firstSnapshotStream":"wl.petrochina.base","lastDetectedId":10003,"lastDetectedVersion":"","lastDetectedTarget":"","lastDetectedDescription":"","lastDetectedStream":"wl.petrochina.base","occurrenceCount":1,"lastDefectInstanceId":1021,"displayImpact":"Medium","displayCategory":"Null pointer dereferences","displayType":"Explicit null dereferenced","cwe":476,"fixTarget":"Untargeted","displayIssueKind":"Quality","ownerFullName":"","mergeExtra":"st","functionMergeName":"wl.petrochina.base.popupControl.sender.application.internal.internal.HairStandingServiceImpl.queryHairStanding(java.lang.String, java.lang.String, java.lang.String)","legacy":"False","displayComparison":"Absent","displayFirstDetectedBy":"Snapshot","committed":true,"fileLanguage":"Java","ruleStrength":"None","fileInstanceId":4196,"projectId":10003,"pivotKey":"cid"},{"id":10007,"cid":10007,"checker":"NULL_RETURNS","status":"New","classification":"Unclassified","severity":"Unspecified","action":"Undecided","owner":"Unassigned","ownerId":-1,"displayFunction":"SaOrgServiceImpl.findThirdLevelOrgByOrgNo","displayFile":"/src/main/java/wl/petrochina/base/service/application/internal/SaOrgServiceImpl.java","firstDetected":"07/12/17","lastFixed":"07/12/17","lastDetected":"07/12/17","lastTriaged":"","subcategory":"","domain":"","externalReference":"","comment":"","mergeKey":"a4e9757b69764a6adfa6fe924f2839e8","displayComponent":"Other","firstSnapshotDate":"07/12/17","firstSnapshotId":10003,"firstSnapshotVersion":"","firstSnapshotTarget":"","firstSnapshotDescription":"","firstSnapshotStream":"wl.petrochina.base","lastDetectedId":10003,"lastDetectedVersion":"","lastDetectedTarget":"","lastDetectedDescription":"","lastDetectedStream":"wl.petrochina.base","occurrenceCount":1,"lastDefectInstanceId":1026,"displayImpact":"Medium","displayCategory":"Null pointer dereferences","displayType":"Dereference null return value","cwe":476,"fixTarget":"Untargeted","displayIssueKind":"Quality","ownerFullName":"","mergeExtra":"findByOrgNo","functionMergeName":"wl.petrochina.base.service.application.internal.SaOrgServiceImpl.findThirdLevelOrgByOrgNo(java.lang.String, wl.petrochina.base.Constants$OrgTypeLevel)","legacy":"False","displayComparison":"Absent","displayFirstDetectedBy":"Snapshot","committed":true,"fileLanguage":"Java","ruleStrength":"None","fileInstanceId":4449,"projectId":10003,"pivotKey":"cid"},{"id":10008,"cid":10008,"checker":"NULL_RETURNS","status":"New","classification":"Unclassified","severity":"Unspecified","action":"Undecided","owner":"Unassigned","ownerId":-1,"displayFunction":"BaseFlowTrsServiceImpl.querybaseConvenientStoreByOrgNo","displayFile":"/src/main/java/wl/petrochina/base/popupControl/sender/application/internal/internal/BaseFlowTrsServiceImpl.java","firstDetected":"07/12/17","lastFixed":"07/12/17","lastDetected":"07/12/17","lastTriaged":"","subcategory":"","domain":"","externalReference":"","comment":"","mergeKey":"d241f32b1918096766b070be3fb341fc","displayComponent":"Other","firstSnapshotDate":"07/12/17","firstSnapshotId":10003,"firstSnapshotVersion":"","firstSnapshotTarget":"","firstSnapshotDescription":"","firstSnapshotStream":"wl.petrochina.base","lastDetectedId":10003,"lastDetectedVersion":"","lastDetectedTarget":"","lastDetectedDescription":"","lastDetectedStream":"wl.petrochina.base","occurrenceCount":1,"lastDefectInstanceId":1027,"displayImpact":"Medium","displayCategory":"Null pointer dereferences","displayType":"Dereference null return value","cwe":476,"fixTarget":"Untargeted","displayIssueKind":"Quality","ownerFullName":"","mergeExtra":"findOrgNosByOrgTreeInfo","functionMergeName":"wl.petrochina.base.popupControl.sender.application.internal.internal.BaseFlowTrsServiceImpl.querybaseConvenientStoreByOrgNo(java.lang.String, java.lang.String)","legacy":"False","displayComparison":"Absent","displayFirstDetectedBy":"Snapshot","committed":true,"fileLanguage":"Java","ruleStrength":"None","fileInstanceId":4404,"projectId":10003,"pivotKey":"cid"},{"id":10009,"cid":10009,"checker":"NULL_RETURNS","status":"New","classification":"Unclassified","severity":"Unspecified","action":"Undecided","owner":"Unassigned","ownerId":-1,"displayFunction":"AuthenticationWithExcludeUrlFilter.doFilter","displayFile":"/src/main/java/wl/petrochina/base/casClient/AuthenticationWithExcludeUrlFilter.java","firstDetected":"07/12/17","lastFixed":"07/12/17","lastDetected":"07/12/17","lastTriaged":"","subcategory":"","domain":"","externalReference":"","comment":"","mergeKey":"37fae1345bc88bade93ddc52411548a0","displayComponent":"Other","firstSnapshotDate":"07/12/17","firstSnapshotId":10003,"firstSnapshotVersion":"","firstSnapshotTarget":"","firstSnapshotDescription":"","firstSnapshotStream":"wl.petrochina.base","lastDetectedId":10003,"lastDetectedVersion":"","lastDetectedTarget":"","lastDetectedDescription":"","lastDetectedStream":"wl.petrochina.base","occurrenceCount":1,"lastDefectInstanceId":1028,"displayImpact":"Medium","displayCategory":"Null pointer dereferences","displayType":"Dereference null return value","cwe":476,"fixTarget":"Untargeted","displayIssueKind":"Quality","ownerFullName":"","mergeExtra":"getUserName","functionMergeName":"wl.petrochina.base.casClient.AuthenticationWithExcludeUrlFilter.doFilter(javax.servlet.ServletRequest, javax.servlet.ServletResponse, javax.servlet.FilterChain)","legacy":"False","displayComparison":"Absent","displayFirstDetectedBy":"Snapshot","committed":true,"fileLanguage":"Java","ruleStrength":"None","fileInstanceId":4000,"projectId":10003,"pivotKey":"cid"},{"id":10010,"cid":10010,"checker":"NULL_RETURNS","status":"New","classification":"Unclassified","severity":"Unspecified","action":"Undecided","owner":"Unassigned","ownerId":-1,"displayFunction":"BaseOilAreaDensityServiceImpl.addEnsity","displayFile":"/src/main/java/wl/petrochina/base/buscontrol/application/internal/BaseOilAreaDensityServiceImpl.java","firstDetected":"07/12/17","lastFixed":"07/12/17","lastDetected":"07/12/17","lastTriaged":"","subcategory":"","domain":"","externalReference":"","comment":"","mergeKey":"bae3a131811eec05acf64aa20afa6e62","displayComponent":"Other","firstSnapshotDate":"07/12/17","firstSnapshotId":10003,"firstSnapshotVersion":"","firstSnapshotTarget":"","firstSnapshotDescription":"","firstSnapshotStream":"wl.petrochina.base","lastDetectedId":10003,"lastDetectedVersion":"","lastDetectedTarget":"","lastDetectedDescription":"","lastDetectedStream":"wl.petrochina.base","occurrenceCount":1,"lastDefectInstanceId":1032,"displayImpact":"Medium","displayCategory":"Null pointer dereferences","displayType":"Dereference null return value","cwe":476,"fixTarget":"Untargeted","displayIssueKind":"Quality","ownerFullName":"","mergeExtra":"findOriginalDensity","functionMergeName":"wl.petrochina.base.buscontrol.application.internal.BaseOilAreaDensityServiceImpl.addEnsity(wl.petrochina.base.buscontrol.application.BaseOilAreaDensityDTO)","legacy":"False","displayComparison":"Absent","displayFirstDetectedBy":"Snapshot","committed":true,"fileLanguage":"Java","ruleStrength":"None","fileInstanceId":4199,"projectId":10003,"pivotKey":"cid"},{"id":10011,"cid":10011,"checker":"NULL_RETURNS","status":"New","classification":"Unclassified","severity":"Unspecified","action":"Undecided","owner":"Unassigned","ownerId":-1,"displayFunction":"BaseOilAreaDensityServiceImpl.addEnsity","displayFile":"/src/main/java/wl/petrochina/base/buscontrol/application/internal/BaseOilAreaDensityServiceImpl.java","firstDetected":"07/12/17","lastFixed":"07/12/17","lastDetected":"07/12/17","lastTriaged":"","subcategory":"","domain":"","externalReference":"","comment":"","mergeKey":"b83da4a929a1790dc1ae58d7afbb9a92","displayComponent":"Other","firstSnapshotDate":"07/12/17","firstSnapshotId":10003,"firstSnapshotVersion":"","firstSnapshotTarget":"","firstSnapshotDescription":"","firstSnapshotStream":"wl.petrochina.base","lastDetectedId":10003,"lastDetectedVersion":"","lastDetectedTarget":"","lastDetectedDescription":"","lastDetectedStream":"wl.petrochina.base","occurrenceCount":1,"lastDefectInstanceId":1030,"displayImpact":"Medium","displayCategory":"Null pointer dereferences","displayType":"Dereference null return value","cwe":476,"fixTarget":"Untargeted","displayIssueKind":"Quality","ownerFullName":"","mergeExtra":"findMaxOriginalDensity","functionMergeName":"wl.petrochina.base.buscontrol.application.internal.BaseOilAreaDensityServiceImpl.addEnsity(wl.petrochina.base.buscontrol.application.BaseOilAreaDensityDTO)","legacy":"False","displayComparison":"Absent","displayFirstDetectedBy":"Snapshot","committed":true,"fileLanguage":"Java","ruleStrength":"None","fileInstanceId":4199,"projectId":10003,"pivotKey":"cid"},{"id":10012,"cid":10012,"checker":"NULL_RETURNS","status":"New","classification":"Unclassified","severity":"Unspecified","action":"Undecided","owner":"Unassigned","ownerId":-1,"displayFunction":"BaseMediaFileServiceImpl.replaceFile","displayFile":"/src/main/java/wl/petrochina/base/service/application/internal/BaseMediaFileServiceImpl.java","firstDetected":"07/12/17","lastFixed":"07/12/17","lastDetected":"07/12/17","lastTriaged":"","subcategory":"","domain":"","externalReference":"","comment":"","mergeKey":"db74947bd62930a6aa09508a19cfed28","displayComponent":"Other","firstSnapshotDate":"07/12/17","firstSnapshotId":10003,"firstSnapshotVersion":"","firstSnapshotTarget":"","firstSnapshotDescription":"","firstSnapshotStream":"wl.petrochina.base","lastDetectedId":10003,"lastDetectedVersion":"","lastDetectedTarget":"","lastDetectedDescription":"","lastDetectedStream":"wl.petrochina.base","occurrenceCount":1,"lastDefectInstanceId":1029,"displayImpact":"Medium","displayCategory":"Null pointer dereferences","displayType":"Dereference null return value","cwe":476,"fixTarget":"Untargeted","displayIssueKind":"Quality","ownerFullName":"","mergeExtra":"upload","functionMergeName":"wl.petrochina.base.service.application.internal.BaseMediaFileServiceImpl.replaceFile(java.math.BigDecimal, java.lang.String)","legacy":"False","displayComparison":"Absent","displayFirstDetectedBy":"Snapshot","committed":true,"fileLanguage":"Java","ruleStrength":"None","fileInstanceId":4258,"projectId":10003,"pivotKey":"cid"},{"id":10013,"cid":10013,"checker":"NULL_RETURNS","status":"New","classification":"Unclassified","severity":"Unspecified","action":"Undecided","owner":"Unassigned","ownerId":-1,"displayFunction":"StationSaUtils.getFiles","displayFile":"/src/main/java/wl/petrochina/base/station/StationSaUtils.java","firstDetected":"07/12/17","lastFixed":"07/12/17","lastDetected":"07/12/17","lastTriaged":"","subcategory":"","domain":"","externalReference":"","comment":"","mergeKey":"cdaa919b0f2b373bf3b49910b6d8de12","displayComponent":"Other","firstSnapshotDate":"07/12/17","firstSnapshotId":10003,"firstSnapshotVersion":"","firstSnapshotTarget":"","firstSnapshotDescription":"","firstSnapshotStream":"wl.petrochina.base","lastDetectedId":10003,"lastDetectedVersion":"","lastDetectedTarget":"","lastDetectedDescription":"","lastDetectedStream":"wl.petrochina.base","occurrenceCount":1,"lastDefectInstanceId":1023,"displayImpact":"Medium","displayCategory":"Null pointer dereferences","displayType":"Dereference null return value","cwe":476,"fixTarget":"Untargeted","displayIssueKind":"Quality","ownerFullName":"","mergeExtra":"listFiles","functionMergeName":"wl.petrochina.base.station.StationSaUtils.getFiles(java.util.List, java.io.File)","legacy":"False","displayComparison":"Absent","displayFirstDetectedBy":"Snapshot","committed":true,"fileLanguage":"Java","ruleStrength":"None","fileInstanceId":4716,"projectId":10003,"pivotKey":"cid"},{"id":10014,"cid":10014,"checker":"NULL_RETURNS","status":"New","classification":"Unclassified","severity":"Unspecified","action":"Undecided","owner":"Unassigned","ownerId":-1,"displayFunction":"BaseOilAreaDensityServiceImpl.addEnsity","displayFile":"/src/main/java/wl/petrochina/base/buscontrol/application/internal/BaseOilAreaDensityServiceImpl.java","firstDetected":"07/12/17","lastFixed":"07/12/17","lastDetected":"07/12/17","lastTriaged":"","subcategory":"","domain":"","externalReference":"","comment":"","mergeKey":"891334beab5c9ce1c8f97c8478a07f38","displayComponent":"Other","firstSnapshotDate":"07/12/17","firstSnapshotId":10003,"firstSnapshotVersion":"","firstSnapshotTarget":"","firstSnapshotDescription":"","firstSnapshotStream":"wl.petrochina.base","lastDetectedId":10003,"lastDetectedVersion":"","lastDetectedTarget":"","lastDetectedDescription":"","lastDetectedStream":"wl.petrochina.base","occurrenceCount":1,"lastDefectInstanceId":1031,"displayImpact":"Medium","displayCategory":"Null pointer dereferences","displayType":"Dereference null return value","cwe":476,"fixTarget":"Untargeted","displayIssueKind":"Quality","ownerFullName":"","mergeExtra":"findMinOriginalDensity","functionMergeName":"wl.petrochina.base.buscontrol.application.internal.BaseOilAreaDensityServiceImpl.addEnsity(wl.petrochina.base.buscontrol.application.BaseOilAreaDensityDTO)","legacy":"False","displayComparison":"Absent","displayFirstDetectedBy":"Snapshot","committed":true,"fileLanguage":"Java","ruleStrength":"None","fileInstanceId":4199,"projectId":10003,"pivotKey":"cid"},{"id":10015,"cid":10015,"checker":"RESOURCE_LEAK","status":"New","classification":"Unclassified","severity":"Unspecified","action":"Undecided","owner":"Unassigned","ownerId":-1,"displayFunction":"BaseMediaFileDAO.getSHA256","displayFile":"/src/main/java/wl/petrochina/base/service/infrastructure/BaseMediaFileDAO.java","firstDetected":"07/12/17","lastFixed":"07/12/17","lastDetected":"07/12/17","lastTriaged":"","subcategory":"","domain":"","externalReference":"","comment":"","mergeKey":"aff6356084d7e511419f64c8cf28b405","displayComponent":"Other","firstSnapshotDate":"07/12/17","firstSnapshotId":10003,"firstSnapshotVersion":"","firstSnapshotTarget":"","firstSnapshotDescription":"","firstSnapshotStream":"wl.petrochina.base","lastDetectedId":10003,"lastDetectedVersion":"","lastDetectedTarget":"","lastDetectedDescription":"","lastDetectedStream":"wl.petrochina.base","occurrenceCount":1,"lastDefectInstanceId":1024,"displayImpact":"Low","displayCategory":"Exceptional resource leaks","displayType":"Resource leak on an exceptional path","cwe":404,"fixTarget":"Untargeted","displayIssueKind":"Various","ownerFullName":"","mergeExtra":"FileInputStream","functionMergeName":"wl.petrochina.base.service.infrastructure.BaseMediaFileDAO.getSHA256(java.lang.String)","legacy":"False","displayComparison":"Absent","displayFirstDetectedBy":"Snapshot","committed":true,"fileLanguage":"Java","ruleStrength":"None","fileInstanceId":4204,"projectId":10003,"pivotKey":"cid"},{"id":10016,"cid":10016,"checker":"RESOURCE_LEAK","status":"New","classification":"Unclassified","severity":"Unspecified","action":"Undecided","owner":"Unassigned","ownerId":-1,"displayFunction":"MediaFileServlet.doGet","displayFile":"/src/main/java/wl/petrochina/base/servlet/MediaFileServlet.java","firstDetected":"07/12/17","lastFixed":"07/12/17","lastDetected":"07/12/17","lastTriaged":"","subcategory":"","domain":"","externalReference":"","comment":"","mergeKey":"25fa9dec50e45f0539848e61089ed82d","displayComponent":"Other","firstSnapshotDate":"07/12/17","firstSnapshotId":10003,"firstSnapshotVersion":"","firstSnapshotTarget":"","firstSnapshotDescription":"","firstSnapshotStream":"wl.petrochina.base","lastDetectedId":10003,"lastDetectedVersion":"","lastDetectedTarget":"","lastDetectedDescription":"","lastDetectedStream":"wl.petrochina.base","occurrenceCount":1,"lastDefectInstanceId":1025,"displayImpact":"Low","displayCategory":"Exceptional resource leaks","displayType":"Resource leak on an exceptional path","cwe":404,"fixTarget":"Untargeted","displayIssueKind":"Various","ownerFullName":"","mergeExtra":"FileInputStream","functionMergeName":"wl.petrochina.base.servlet.MediaFileServlet.doGet(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse)","legacy":"False","displayComparison":"Absent","displayFirstDetectedBy":"Snapshot","committed":true,"fileLanguage":"Java","ruleStrength":"None","fileInstanceId":4314,"projectId":10003,"pivotKey":"cid"}],"selectedIds":[],"filteredIds":[10001,10002,10003,10004,10005,10006,10007,10008,10009,10010,10011,10012,10013,10014,10015,10016]}}'
    data = json.loads(msg)
    print("total count: ", data["resultSet"]["totalCount"])

    global wb
    ws = wb.add_sheet(app, cell_overwrite_ok=True)
    ws.write(0, 0, "���".decode('gbk'), set_style('Times New Roman',280,True))
    ws.write(0, 1, "ȱ������".decode('gbk'), set_style('Times New Roman',280,True))
    ws.write(0, 2, "���س̶�".decode('gbk'), set_style('Times New Roman',280,True))
    ws.write(0, 3, "�ļ�".decode('gbk'), set_style('Times New Roman',280,True))
    ws.write(0, 4, "�к�".decode('gbk'), set_style('Times New Roman',280,True))
    ws.write(0, 5, "������".decode('gbk'), set_style('Times New Roman',280,True))
    ws.write(0, 6, "ȱ��˵��".decode('gbk'), set_style('Times New Roman',280,True))
    ws.col(0).width=256*6
    ws.col(1).width=256*20
    ws.col(2).width=256*20
    ws.col(3).width=256*80
    ws.col(4).width=256*10
    ws.col(5).width=256*80
    ws.col(6).width=256*80

    global impact
    row = 1
    for idx, t in enumerate(data["resultSet"]["results"]):
        print("idx: ", idx)
        #if t["displayImpact"] == "Medium" or t["displayImpact"] == "High":
            #print t["firstSnapshotStream"], t["functionMergeName"], t["displayCategory"], t["displayImpact"], t["displayFile"], t["id"], t["lastDefectInstanceId"], t["fileInstanceId"]
        row = get_defects(ws, row, idx, t, app, pid, t["fileInstanceId"], t["lastDefectInstanceId"], t["cid"])

def get_defects(ws, row, idx, t, app, projId, fileId, defectId, mergeId):
    url = "http://localhost:8080/sourcebrowser/source.json?projectId="+str(projId)+"&fileInstanceId="+str(fileId)+"&defectInstanceId="+str(defectId)+"&mergedDefectId="+str(mergeId)
    print(url)
    """
    global cookies
    s = requests.Session()
    rsp = s.get(url, cookies=cookies)
    if rsp.status_code != 200:
        print "get_projects failed: %d" % (rsp.status_code)
        return
    print rsp.text
    """
    msg = r'{"fileMax":250,"ancestorFileInstanceIds":[3362,3363,3364,3365,4006,3366,3367,3368,3641,3466],"filePath":"/src/main/java/wl/petrochina/base/org/infrastructure/SaOrgDAO.java","fileStart":1,"lineIdPrefix":"main","ta":{"functionLineNumbers":[26,33,46,63,78,93,110,127,144,161,179],"fileChangeRecords":[],"fileAnnotations":[],"testViolationRules":[]},"mainEventId":"1017-4","fileInstanceId":4006,"fileEnd":202,"fileLast":202,"defects":[{"checker":"DEADCODE","defectInstanceIds":[1017],"shortDescription":"Logically dead code","ids":{"cid":10001,"defectInstanceId":1017,"fileInstanceId":4006,"mergedDefectId":10001},"occurrenceIndex":1,"occurrenceCount":1,"mainEvent":{"id":"1017-4","description":"Execution cannot reach this statement: <span class=\"code\">sb.append(<span class=\"literal\">&quot;&nbsp;and&nbsp;1&nbsp;=&nbsp;1&nbsp;&quot;</span>);</span>.","lineNumber":196}}],"purged":false,"events":[{"id":"1017-0","lineNumber":181,"ordered":false,"tag":"new_never_null","description":"<span class=\"code\"><span class=\"keyword\">new</span>&nbsp;java.lang.StringBuffer()</span> is never null.","eventSet":0,"main":false},{"id":"1017-1","lineNumber":181,"ordered":false,"tag":"assignment","description":"Assigning: <span class=\"code\">sb</span> = <span class=\"code\"><span class=\"keyword\">new</span>&nbsp;java.lang.StringBuffer()</span>.","eventSet":0,"main":false},{"id":"1017-2","lineNumber":190,"ordered":false,"tag":"notnull","description":"At condition <span class=\"code\"><span class=\"literal\">null</span>&nbsp;!=&nbsp;sb</span>, the value of <span class=\"code\">sb</span> cannot be <span class=\"code\"><span class=\"literal\">null</span></span>.","eventSet":0,"main":false},{"id":"1017-3","lineNumber":190,"ordered":false,"tag":"dead_error_condition","description":"The condition <span class=\"code\"><span class=\"literal\">null</span>&nbsp;!=&nbsp;sb</span> must be true.","eventSet":0,"main":false},{"id":"1017-4","lineNumber":196,"ordered":false,"tag":"dead_error_begin","description":"Execution cannot reach this statement: <span class=\"code\">sb.append(<span class=\"literal\">&quot;&nbsp;and&nbsp;1&nbsp;=&nbsp;1&nbsp;&quot;</span>);</span>.","eventSet":0,"main":true}],"mergedDefectId":10001}'
    data = json.loads(msg)
    print(data["fileStart"], data["fileEnd"], data["filePath"])
    line_info = {}
    for e in data["events"]:
        if line_info.has_key(e["lineNumber"]):
            desc = bs(e["description"], "lxml")
            line_info[e["lineNumber"]].append(e["tag"] + ":" + desc.text)
        else:
            l = []
            desc = bs(e["description"], "lxml")
            l.append(e["tag"] + ":" + desc.text)
            line_info[e["lineNumber"]] = l
    print(line_info)
    return get_source(ws, row, idx, t, app, projId, fileId, data["fileStart"], data["fileEnd"], line_info)

def get_source(ws, row, idx, t, app, projId, fileId, fileStart, fileEnd, line_info):
    global cookies
    url = "http://localhost:8080/sourcebrowser/source.htm?projectId="+str(projId)+"&fileInstanceId="+str(fileId)+"&fileStart="+str(fileStart)+"&fileEnd="+str(fileEnd)+"&lineIdPrefix=main&allow-caching=true"
    print(url)
    """
    s = requests.Session()
    rsp = s.get(url, cookies=cookies)
    if rsp.status_code != 200:
        print "get_projects failed: %d" % (rsp.status_code)
        return
    print rsp.text
    """
    f = open("code", "r")
    lines = f.readlines()
    f.close()

    codes = ""
    for l in lines:
        codes += l

    soup = bs(codes, "lxml")


    span = row
    r = 0
    for (target, info) in line_info.items():
        ws.write_merge(span, span+4, 0, 0, (row/5)+1+r, set_style('Times New Roman',220,False))
        ws.write_merge(span, span+4, 1, 1, t["displayCategory"], set_style('Times New Roman',220,False))
        ws.write_merge(span, span+4, 2, 2, impact[t["displayImpact"]], set_style('Times New Roman',220,False))
        ws.write_merge(span, span+4, 3, 3, t["displayFile"], set_style('Times New Roman',220,False))

        ws.write_merge(span, span+4, 4, 4, target, set_style('Times New Roman',220,False))
        targets = [target-2, target-1, target, target+1, target+2]

        source = []
        red_font = xlwt.easyfont("italic false, color_index red")
        for pos, tt in enumerate(targets):
            div = soup.find("div", id="main-source-line-"+str(tt))
            text = div.text.replace(u'\xa0', ' ')
            vals = text.split(" ")
            text = ""
            for v in vals[1:]:
                text += v + " "
            if tt == target:
                highlight = ("%s" % text, red_font)
                source.append(highlight)
                source.append("\n")
            else:
                source.append(text)
                source.append("\n")
        source.append("\n")
        style = xlwt.easyxf("align: wrap true, horiz left, vert center")
        ws.write_merge(span, span+4, 5, 5, "", style)
        ws.row(span).set_cell_rich_text(5, tuple(source), style)

        tip = []
        for i in info:
            tip.append(i)
            tip.append("\n")
        tip.append("\n")
        ws.write_merge(span, span+4, 6, 6, "", style)
        ws.row(span).set_cell_rich_text(6, tuple(tip), style)

        span += 5
        r += 1
    return span

def get_viewid(pid):
    """
    global cookies
    url = "http://localhost:8080/views.json?projectId="+pid
    s = requests.Session()
    rsp = s.get(url, cookies=cookies)
    if rsp.status_code != 200:
        print "get_projects failed: %d" % (rsp.status_code)
        return
    print rsp.text
    """
    msg = '{"dashboardLabel":"Dashboards","tables":[{"key":"DefectsTable","label":"Issues: By Snapshot","views":[{"id":10011,"name":"High Impact Outstanding","sharedBy":null,"groupColumn":null,"hidden":false,"transient":false,"shared":false},{"id":10015,"name":"My Outstanding","sharedBy":null,"groupColumn":null,"hidden":false,"transient":false,"shared":false},{"id":10012,"name":"Outstanding Defects","sharedBy":null,"groupColumn":null,"hidden":false,"transient":false,"shared":false},{"id":10013,"name":"Outstanding Security Risks","sharedBy":null,"groupColumn":null,"hidden":false,"transient":false,"shared":false},{"id":10014,"name":"Outstanding Test Rules Violations","sharedBy":null,"groupColumn":null,"hidden":false,"transient":false,"shared":false},{"id":10010,"name":"Outstanding Untriaged","sharedBy":null,"groupColumn":null,"hidden":false,"transient":false,"shared":false},{"id":10026,"name":"testsss","sharedBy":null,"groupColumn":null,"hidden":false,"transient":false,"shared":false},{"id":10025,"name":"Unsaved view","sharedBy":null,"groupColumn":null,"hidden":false,"transient":true,"shared":false}],"isHidden":false},{"key":"DefectsBPTable","label":"Issues: Project Scope","views":[{"id":10016,"name":"All In Project","sharedBy":null,"groupColumn":null,"hidden":false,"transient":false,"shared":false}],"isHidden":false},{"key":"FilesTable","label":"Files","views":[{"id":10005,"name":"In Latest Snapshot","sharedBy":null,"groupColumn":null,"hidden":false,"transient":false,"shared":false},{"id":10006,"name":"Uncovered By Tests","sharedBy":null,"groupColumn":null,"hidden":false,"transient":false,"shared":false}],"isHidden":false},{"key":"FunctionsTable","label":"Functions","views":[{"id":10008,"name":"High CCM (>15)","sharedBy":null,"groupColumn":null,"hidden":false,"transient":false,"shared":false},{"id":10007,"name":"In Latest Snapshot","sharedBy":null,"groupColumn":null,"hidden":false,"transient":false,"shared":false},{"id":10009,"name":"Uncovered By Tests","sharedBy":null,"groupColumn":null,"hidden":false,"transient":false,"shared":false}],"isHidden":false},{"key":"ComponentsTable","label":"Components","views":[{"id":10018,"name":"All In Project","sharedBy":null,"groupColumn":null,"hidden":false,"transient":false,"shared":false},{"id":10021,"name":"High Issue Density (>1)","sharedBy":null,"groupColumn":null,"hidden":false,"transient":false,"shared":false},{"id":10020,"name":"With Outstanding Issues","sharedBy":null,"groupColumn":null,"hidden":false,"transient":false,"shared":false},{"id":10019,"name":"With Untriaged Issues","sharedBy":null,"groupColumn":null,"hidden":false,"transient":false,"shared":false}],"isHidden":false},{"key":"CheckersTable","label":"Checkers","views":[{"id":10023,"name":"All In Project","sharedBy":null,"groupColumn":null,"hidden":false,"transient":false,"shared":false}],"isHidden":false},{"key":"OwnersTable","label":"Owners","views":[{"id":10022,"name":"All In Project","sharedBy":null,"groupColumn":null,"hidden":false,"transient":false,"shared":false}],"isHidden":false},{"key":"SnapshotsTable","label":"Snapshots","views":[{"id":10004,"name":"All In Project","sharedBy":null,"groupColumn":null,"hidden":false,"transient":false,"shared":false}],"isHidden":false},{"key":"TrendsTable","label":"Trends","views":[{"id":10003,"name":"Project Lifetime","sharedBy":null,"groupColumn":null,"hidden":false,"transient":false,"shared":false}],"isHidden":false},{"key":"TestsTable","label":"Tests","views":[{"id":10001,"name":"All Tests","sharedBy":null,"groupColumn":null,"hidden":false,"transient":false,"shared":false},{"id":10002,"name":"Currently Failing","sharedBy":null,"groupColumn":null,"hidden":false,"transient":false,"shared":false}],"isHidden":false}],"dashboards":[{"key":"QUALITY","title":"Quality Advisor"},{"key":"SECURITY","title":"Security Advisor"},{"key":"TEST","title":"Test Advisor"}],"dashboardsAreHidden":false,"projectId":10003,"recentView":{"projectId":10003,"dashboardKind":null,"viewId":10026,"groupViewId":null,"nodeId":null,"reportId":null,"hash":"#v10026/p10003"}}'
    data = json.loads(msg)
    vid = data["recentView"]["viewId"]
    return vid

def get_projects():
    """
    global cookies
    url = "http://localhost:8080/projects/mru.json"
    s = requests.Session()
    rsp = s.get(url, cookies=cookies)
    if rsp.status_code != 200:
        print "get_projects failed: %d" % (rsp.status_code)
        return
    print rsp.text
    """
    msg = '{"projects":{"views":[{"id":"10003","label":"wl.petrochina.base"}],"viewId":10017}}'
    data = json.loads(msg)
    projs = data["projects"]["views"]
    pjs = []
    for p in projs:
        pjs.append(p["id"])
    return projs

def login():
    global cookies
    url = "http://localhost:8080/j_spring_security_check"
    s = requests.Session()
    #s.headers.update(headers)
    rsp = s.post(url, data={'j_username':'admin','j_password':'123456'}, cookies=cookies)
    if rsp.status_code != 200:
        print("login failed: %d" % (rsp.status_code))
        return
    print(rsp.text)

    """
    soup = bs(rsp.text, "lxml")
    div = soup.findAll("div", class_="cont_details")

    if len(div) == 0:
        print "%s failed" % fn
        return

    trs = div[0].findAll("tr")
    tds = trs[0].findAll("td")
    vuln_name = tds[1].text.strip(" ").replace("'",'"')

    tds = trs[2].findAll("td")
    publish_date = tds[1].text.strip(" ")

    tds = trs[3].findAll("td")
    update_date = tds[1].text.strip(" ")

    tds = trs[4].findAll("td")
    vuln_level = tds[1].text.strip()

    tds = trs[5].findAll("td")
    vuln_type = tds[1].text.strip()

    tds = trs[6].findAll("td")
    threat_type = tds[1].text.strip()

    tds = trs[7].findAll("td")
    cve = tds[1].text.strip()

    origin = ""
    if len(trs) == 9:
        tds = trs[8].findAll("td")
        origin = tds[1].text.strip().replace("'",'"')

    ps = div[1].findAll("p")
    summary = ""
    for p in ps:
        summary += p.text.replace("&nbsp;","").strip().replace("'",'"').replace('\\','')

    ps = div[2].findAll("p")
    patch = ""
    for p in ps:
        patch += p.text.replace("&nbsp;","").strip().replace("'",'"').replace('\\','')

    div = soup.findAll("div", class_="cont_details1")
    reference = ""
    if len(div) > 0:
        ps = div[0].findAll("p")
        for p in ps:
            reference += p.text.replace("&nbsp;","").strip().replace("'",'"').replace('\\','')
    """

if __name__ == "__main__":
    main()
