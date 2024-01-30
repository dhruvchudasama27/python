import sys
sys.path.append('C:\\users\\priyanka\\appdata\\roaming\\python\\python311\\site-packages')

from bs4 import BeautifulSoup

html_document = '''<!DOCTYPE html>
<html lang="en" itemscope itemtype="http://schema.org/WebPage">
  <head>
    <meta charset="utf-8" />
    <script>
      var is_mobile =
        /symbian|tizen|midp|uc(web|browser)|MSIE (5.0|6.0|7.0|8.0)|tablet/i.test(
          navigator.userAgent
        );
      if (is_mobile && window.location.hostname != "www1.cricbuzz.com")
        window.location.hostname = "m.cricbuzz.com";
    </script>
    <style>
      html {
        scroll-behavior: smooth;
      }
      body {
        background: #e3e6e3;
        font-family: helvetica, "Segoe UI", Arial, sans-serif;
        color: #222;
        font-size: 14px;
        line-height: 1.5;
        margin: 0;
      }
      body,
      .cb-comm-pg,
      .cb-hm-mid {
        min-height: 1000px;
      }
      .container {
        width: 980px;
        margin: 0 auto;
      }
      .page {
        max-width: 980px;
        margin: 0 auto;
        position: relative;
      }
      .cb-col-8 {
        width: 8%;
      }
      .cb-col-10 {
        width: 10%;
      }
      .cb-col-14 {
        width: 14%;
      }
      .cb-col-16 {
        width: 16%;
      }
      .cb-col-20 {
        width: 20%;
      }
      .cb-col-25 {
        width: 25%;
      }
      .cb-col-27 {
        width: 27%;
      }
      .cb-col-30 {
        width: 30%;
      }
      .cb-col-33 {
        width: 33%;
      }
      .cb-col-40 {
        width: 40%;
      }
      .cb-col-46 {
        width: 46%;
      }
      .cb-col-47 {
        width: 47%;
      }
      .cb-col-50 {
        width: 50%;
      }
      .cb-col-60 {
        width: 60%;
      }
      .cb-col-65 {
        width: 65%;
      }
      .cb-col-66 {
        width: 66%;
      }
      .cb-col-67 {
        width: 67%;
      }
      .cb-col-73 {
        width: 73%;
      }
      .cb-col-75 {
        width: 75%;
      }
      .cb-col-70 {
        width: 70%;
      }
      .cb-col-84 {
        width: 84%;
      }
      .cb-col-80 {
        width: 80%;
      }
      .cb-col-90 {
        width: 90%;
      }
      .cb-col-100 {
        width: 100%;
      }
      .cb-col {
        display: inline-block;
        box-sizing: border-box;
        float: left;
        min-height: 1px;
      }
      h1 {
        font-size: 36px;
        line-height: 42px;
        margin: 0;
      }
      h2 {
        font-size: 24px;
        margin: 0;
        line-height: 30px;
      }
      h3 {
        font-size: 18px;
        line-height: 24px;
        margin: 0;
      }
      h4 {
        font-size: 16px;
        margin: 0;
      }
      h5 {
        font-size: 14px;
        margin: 0;
      }
      .cb-font-18 {
        font-size: 18px;
      }
      img {
        border-radius: 4px;
      }
      a {
        text-decoration: none;
        color: #222;
      }
      a,
      a:hover,
      a:active,
      a:focus {
        outline: medium none;
      }
      .text-center {
        text-align: center;
      }
      .cb-nws-lft-col {
        padding: 15px 20px;
      }
      .cb-nws-dtl-lft-col {
        padding: 10px 30px 0 30px;
        border-right: 1px solid #ecebeb;
      }
      .cb-nws-lst-rt {
        padding-left: 10px;
      }
      .cb-srs-lst-itm {
        padding: 10px 0;
      }
      .cb-lst-itm-sm {
        padding: 10px 0 5px;
      }
      .cb-scrd-lft-col {
        padding: 15px 10px;
      }
      .cb-col-rt {
        padding: 10px;
      }
      .text-white {
        color: #fff;
      }
      .cb-text-apple-red {
        color: #e90b37;
      }
      .cb-color-light-sec {
        color: #464646;
      }
      .cb-scrd-hdr-rw,
      .cb-nav-pill-1.active {
        background: #028062;
        color: #fff;
      }
      .cb-nav {
        position: relative;
        height: 48px;
        background: #009270;
      }
      .cb-hm-mnu-itm {
        padding: 16px 6px 11px;
        color: #fff;
        display: inline-block;
      }
      .cb-hm-text {
        padding: 10px 18px 10px 20px;
      }
      .cb-hm-rght {
        padding: 15px;
      }
      .cb-subnav .cb-sub-navigation {
        display: none;
        position: absolute;
      }
      .cb-mat-mnu {
        background: #4a4a4a;
        width: 980px;
        font-size: 0;
      }
      .cb-mat-mnu-itm {
        font-size: 12px;
        color: #fff;
        padding: 10px;
        cursor: pointer;
        display: inline-block;
        max-width: 140px;
      }
      .cb-mat-mnu-ttl {
        background: #333;
        padding: 10px 20px;
      }
      .cb-mat-mnu-wrp {
        margin-bottom: 10px;
      }
      .cb-ovr-flo {
        overflow: hidden;
        white-space: nowrap;
        text-overflow: ellipsis;
      }
      .cb-mat-mnu-all {
        text-align: center;
        float: right;
        width: 60px;
      }
      .cb-nav-main {
        border-bottom: 1px solid #e3e6e3;
        padding: 0 0 5px 20px;
      }
      .cb-nav-bar {
        padding-top: 10px;
        clear: both;
      }
      .cb-lst-itm,
      .cb-bg-white {
        background: #fff;
      }
      .cb-nav-tab.active,
      .cb-nav-tab-hm.active {
        font-weight: bold;
        color: #028062;
      }
      .cb-nav-tab.active {
        border-bottom: 3px solid #028062;
        line-height: 24px;
      }
      .cb-nav-tab-hm.active {
        border-bottom: 2px solid #028062;
        line-height: 22px;
      }
      .cb-nav-tab {
        margin-right: 20px;
        padding-bottom: 6px;
      }
      .cb-nav-tab-hm {
        margin-right: 15px;
        padding-bottom: 6px;
      }
      .cb-nav-hdr {
        padding-top: 15px;
      }
      .cb-nav-subhdr {
        padding: 5px 0 10px 0;
      }
      .cb-lv-scr-mtch-hdr {
        line-height: 21px;
        font-size: 16px;
      }
      .disp-none {
        display: none;
      }
      .disp-blck {
        display: block;
      }
      .cb-font-24 {
        font-size: 24px;
      }
      .line-ht30 {
        line-height: 30px;
      }
      .line-ht24 {
        line-height: 24px;
      }
      .cb-hm-scg-blk {
        background: #fff;
        margin-bottom: 5px;
        height: 90px;
      }
      .mrgn-btm-5 {
        margin-bottom: 5px;
      }
      #scagTabContent .show {
        display: block;
        visibility: visible;
      }
      #scagTabContent .hide {
        display: none;
        visibility: hidden;
      }
      [ng\:cloak],
      [ng-cloak],
      [data-ng-cloak],
      [x-ng-cloak],
      .ng-cloak,
      .x-ng-cloak {
        display: none !important;
      }
      .cb-hm-lft {
        margin-bottom: 5px;
        padding: 0 15px;
      }
      .cb-hm-lft-hdr {
        margin: 0;
        padding: 15px 15px 0;
        color: #009270;
      }
      .cb-hm-mid {
        border-left: 5px solid #e3e6e3;
        border-right: 5px solid #e3e6e3;
        padding: 0 15px;
      }
      .cb-mtch-blk {
        border-right: 1px solid #ecebeb;
        line-height: 1.4;
        margin: 15px 0;
        padding: 0 20px;
      }
      .crd-cntxt {
        font-size: 12px;
        color: #666;
        padding-bottom: 10px;
      }
      .big-crd-main {
        border-top: 1px solid #ecebeb;
        padding: 15px 0 5px;
        margin-bottom: 1px;
        clear: both;
      }
      .big-crd-reltd-itm {
        margin: 0 0 10px;
        width: 100%;
        display: inline-block;
      }
      .cb-nws-time {
        font-size: 12px;
        padding-bottom: 5px;
      }
      .cb-nws-hdln-ancr {
        padding-bottom: 5px;
      }
      .cb-hmscg-bwl-txt,
      .cb-hmscg-bat-txt {
        font-weight: bold;
        padding-bottom: 4px;
        height: 18px;
      }
      .cb-hmscg-bwl-txt {
        color: #666;
      }
      .sml-crd-main {
        padding: 15px 0 5px;
        width: 100%;
      }
      .big-crd-hdln {
        margin: 10px 0;
      }
      .big-crd-rltd-txt {
        font-weight: bold;
        margin: 10px 0;
        color: #1866db;
      }
      .cb-nws-intr {
        color: #666;
        padding-bottom: 5px;
      }
      .cb-lv-scrs-well {
        background: #f5f5f5;
        display: inline-block;
        margin: 10px 0;
        padding: 10px 5px;
      }
      .cb-hm-mtch-crd-width {
        min-width: 300px;
      }
      .cb-mr-30 {
        margin-right: 30px;
      }
      .cb-pretag {
        color: #b34a57;
      }
      .cb-plus-trending-img {
        border-bottom-left-radius: 0;
        border-bottom-right-radius: 0;
      }
      .cb-plus-editorial-img {
        border-top-right-radius: 0;
        border-bottom-right-radius: 0;
      }
      .cb-plus-news-lst-rt {
        padding: 25px 20px 20px 15px;
      }
      .cb-plus-trending-block {
        border: 1px solid #ddd;
        border-radius: 4px;
      }
      .cb-plus-main {
        min-height: 600px;
      }
      .cb-editorial-pills {
        padding: 20px 20px 0;
      }
      .cb-editorial-carousal-list {
        white-space: nowrap;
        overflow: hidden;
        padding: 20px 20px 5px;
      }
      .cb-editorial-carousal-wrapper {
        transition: all 0.3s ease;
      }
      .cb-modal-hide {
        visibility: hidden;
        opacity: 0;
      }
      .cb-schdl-hdr {
        margin: 0;
        padding: 15px 0 10px 10px;
      }
      .cb-lst-itm-lg {
        padding: 20px 0;
      }
      .cb-left-pad {
        padding: 20px 10px 0;
      }
      .cb-nav-pill-1 {
        background: #cfe0db;
        border-radius: 20px;
        color: #222;
        cursor: pointer;
        margin-right: 15px;
        padding: 5px 20px;
      }
      .cb-mtch-lst {
        padding: 15px 0;
      }
      .cb-nws-min-cntr {
        padding: 10px;
        background: #f5f5f5;
        color: #333;
        margin: 10px 0 15px;
      }
      .sml-crd-subtxt {
        margin: 0 10px 10px;
      } /*-------------------------Live Pages -----------------------*/
      .cb-scrcrd-status {
        padding: 0 0 10px 10px;
      }
      .cb-scrd-hdr-rw {
        padding: 8px 10px;
      }
      .cb-bg-gray {
        background: #ecebeb;
      }
      .cb-bg-red {
        background: #e90b37;
      }
      .cb-lv-grn-strip {
        background: #ecebeb;
      }
      .cb-min-hdr-rw,
      .cb-scrd-sub-hdr {
        padding: 4px 10px;
        font-size: 12px;
        color: #666;
      }
      .cb-scrd-itms {
        padding: 4px 10px;
        font-size: 13px;
      }
      .cb-redeem-coupon-link,
      .cb-text-link {
        color: #1866db;
      }
      .text-bold {
        font-weight: bold;
      }
      .text-normal {
        font-weight: normal;
      }
      .cb-mat-fct-itm {
        padding: 5px 0;
      }
      .cb-min-bat-rw {
        padding-bottom: 5px;
      }
      .cb-font-10 {
        font-size: 10px;
      }
      .cb-nws-sub-txt,
      .cb-nws-sub-txt,
      .cb-font-12 {
        font-size: 12px;
      }
      .cb-font-16 {
        font-size: 16px;
      }
      .cb-font-20 {
        font-size: 20px;
      }
      .cb-min-inf {
        padding-top: 10px;
        margin-left: -10px;
        display: inline-block;
      }
      .cb-min-itm-rw {
        padding: 5px 10px 0;
      }
      .text-right {
        text-align: right;
      }
      .cb-key-st-lst {
        padding: 10px 0 0 5px;
      }
      .cb-min-prw-time {
        padding: 20px 0 0;
      }
      .cb-toss-sts {
        padding: 10px 0 30px;
      }
      .cb-min-rcnt {
        padding: 7px 10px;
        margin: 0 -10px 0;
      }
      .cb-key-lst-wrp {
        border: 1px solid #ecebeb;
        padding-bottom: 15px;
        margin-right: -10px;
      }
      .cb-min-tm {
        font-size: 18px;
        font-weight: bold;
      }
      .cb-min-stts {
        padding: 20px 0;
      }
      .cb-mom-itm {
        padding: 0 0 10px;
      }
      .cb-lv-grn-strip {
        padding: 10px 10px 5px;
      }
      .cb-ovr-num {
        padding-top: 2px;
      }
      .cb-min-pad {
        padding-left: 5px;
      } /*Upcoming Series*/
      .cb-mnth {
        margin-top: 10px;
        padding: 0 10px;
      }
      .cb-sch-lst-itm {
        padding: 10px 0;
        margin-left: 20px;
        border-bottom: 1px solid #ecebeb;
      } /*Matches By Day*/
      .cb-mtchs-dy {
        padding: 20px 20px 20px 10px;
      }
      .cb-mtchs-dy-tm,
      .cb-mtchs-dy-vnu {
        padding: 20px 20px 20px 0px;
      } /*Schedule Teams*/
      .cb-lv-upcom-strip {
        padding: 5px 10px;
        background: #ecebeb;
      } /*Archives*/
      .cb-srs-cat {
        padding: 10px;
        color: #028062;
      }
      .pad-left {
        padding-left: 30px;
      }
      .cb-arcv-yr {
        font-size: 20px;
        padding: 0 0 5px 10px;
        font-weight: bold;
      }
      .cb-yr-tmline {
        padding: 2px 15px 15px 0;
      }
      .cb-sch-tms-widgt {
        padding: 5px 10px;
        margin: 5px 2px 2px 2px;
        background: #f5f5f5;
        border-radius: 0;
        border: 0;
        display: inline-block;
      } /*Photos*/
      .cb-thmb-dark {
        background: #333333;
        box-shadow: none;
        border-radius: 4px;
        border: none;
        padding: 0;
        color: #ccc;
      }
      .cb-pht-main {
        padding: 20px 15px;
        margin: 0 -10px;
      }
      .cb-pht-block {
        padding: 9px;
        float: left;
        height: 280px;
        box-sizing: border-box;
      }
      .cb-gallery-pht-block {
        padding: 9px 9px 9px 16px;
      }
      .img-responsive {
        height: auto;
        max-width: 100%;
      }
      .center-block {
        margin-right: auto;
        margin-left: auto;
      }
      .cb-schdl {
        padding: 0 10px;
        line-height: 1.5;
      }
      .cb-caret-up,
      .cb-caret-down {
        display: inline-block;
        width: 0;
        height: 0;
        margin-left: 4px;
        margin-bottom: 1px;
        border-right: 4px solid transparent;
        border-left: 4px solid transparent;
      }
      .cb-caret-up {
        border-bottom: 4px solid;
      }
      .cb-caret-down {
        border-top: 4px solid;
      }
      .cb-hm-rt-itm {
        margin: 0 0 5px;
        padding: 10px 10px 5px;
      }
      .cb-hmscg-tm-nm {
        display: inline-block;
        width: 60px;
      }
      .pull-right,
      .cb-all-mtch-tab {
        float: right;
      }
      .cb-skin-ads-close {
        display: none;
      }
      .cb-nws-sub-txt {
        padding-top: 10px;
      }
      .nws-dtl-hdln {
        margin-top: 10px;
      }
      .cb-min-lv {
        min-height: 270px;
      }
      .cb-min-comp {
        min-height: 150px;
      }
      .cb-ttl-vts {
        margin-top: 20px;
      }
      .cb-poll-radio {
        width: 5%;
        margin: 4px 10px 0 0;
      }
      .cb-mini-tim {
        padding-bottom: 20px;
      }
      .cb-com-ln {
        margin: 0 0 10px;
        line-height: 24px;
      }
      .cb-comm-static {
        margin: 0 -10px 10px;
      }
      .cb-com-ovr-sum-ad {
        min-height: 31px;
      }
      .cb-comm-static-anchr {
        margin: 5px 10px;
        display: block;
      }
      .ad-unit-rendered {
        margin-bottom: 5px;
      }
      .cb-mm-wrp {
        max-height: 0px;
        -webkit-transition: max-height 0.35s ease;
        transition: max-height 0.35s ease;
        overflow: hidden;
      }
      .cb-mm-wrp.down {
        max-height: 1000px;
        transition: max-height 0.75s ease;
        -webkit-transition: max-height 0.75s ease;
        overflow: hidden;
      }
      .cb-srs-hstry-dtl {
        padding: 10px 15px;
        margin-top: 20px;
        border-radius: 4px;
      }
      .cb-qck-lnk {
        margin-bottom: 5px;
        padding: 10px 15px;
      }
      .cb-qck-hdr {
        padding-right: 15px;
        border-right: 1px solid #ecebeb;
      }
      .cb-qck-ancr {
        margin-left: 15px;
      }
      .cb-lst-vid-rw {
        padding-bottom: 0;
        height: 64px;
        border: 1px solid #ecebeb;
        margin-right: -10px;
      }
      .cb-auth-img {
        border-radius: 100%;
      }
      .cb-expt-athr {
        vertical-align: top;
        padding: 5px 0 0 0;
        display: inline-block;
        font-size: 16px;
      }
      .inline-block {
        display: inline-block;
      }
      .cb-exprt-athr-hdr {
        text-align: right;
        font-size: 42px;
        font-family: bodani;
        color: #fff;
        padding-right: 15px;
        line-height: 44px;
        text-transform: uppercase;
      }
      .cb-exprt-athr-hdr-tag {
        text-align: right;
        font-size: 24px;
        font-family: bodani;
        color: #fff;
        padding-right: 15px;
        font-style: italic;
      }
      .cb-athr-wgt-wrp {
        border: 1px solid #ecebeb;
        padding: 15px;
        margin-bottom: 20px;
        background: #f5f5f5;
      }
      .cb-exprt-athr-hdr-img {
        background: url("/images/harsha-banner.jpg") no-repeat scroll;
        height: 80px;
      }
      .cb-overflow-hidden {
        overflow: hidden;
      } /*Videos*/
      .cb-vid-sm-ply-api {
        color: #fff;
        line-height: 34px;
        font-size: 18px;
        margin-left: 3px;
      }
      .cb-vid-sml-card-api {
        margin-top: 10px;
        height: auto;
        padding: 0 12px 0 11px;
      }
      .cb-cat-head-wrap {
        padding: 0 12px 0 11px;
      }
      .cb-cat-head-text {
        margin-top: 5px;
        line-height: 20px;
      }
      .cb-more-btn {
        padding: 8px 20px;
        border-radius: 2px;
        color: #fff;
        background: #009270;
        border: 0;
        cursor: pointer;
      }
      .cb-cat-head-link {
        float: right;
        padding: 5px 25px;
        margin-top: 10px;
        border-radius: 4px;
      }
      .cb-pos-rel {
        position: relative;
      }
      .cb-videos-cat {
        border-bottom: 1px solid #ecebeb;
        padding: 10px 3px 15px 4px;
      }
      .cb-cat-head-text-wrap {
        float: left;
      }
      .cb-cat-head-count {
        margin: 0;
        color: #666;
      }
      h2.cb-cat-head-text {
        font-size: 18px;
      }
      .cb-vid-sml-card-api-head {
        font-size: 14px;
        font-weight: bold;
        line-height: 18px;
        max-height: 55px;
        margin: 2px 0 5px;
        overflow: hidden;
      }
      .cb-cen {
        position: absolute;
        top: 50%;
        left: 50%;
        opacity: 0.8;
        transform: translateX(-50%) translateY(-50%);
        -webkit-transform: translateX(-50%) translateY(-50%);
        -moz-transform: translateX(-50%) translateY(-50%);
        -ms-transform: translateX(-50%) translateY(-50%);
        -o-transform: translateX(-50%) translateY(-50%);
        background: #222;
        text-align: center;
        height: 35px;
        width: 35px;
        border-radius: 50px;
      }
      .cb-cen:hover {
        opacity: 1;
      }
      .padding-handling-errors {
        padding: 20px 0px 10px 15px;
        border-bottom: 1px solid #ecebeb;
      }
      .cb-col .cb-align-cen {
        float: none;
        text-align: center;
        padding: 7px 25px;
        margin-top: 20px;
      }
      .cb-align-cen {
        padding-top: 10px;
      }
      .cb-hot-cat {
        max-width: 90px;
        text-align: center;
        padding-right: 0;
      }
      .cb-hot-cat-img {
        width: 72px;
      }
      .cb-vid-slider-arrs {
        position: absolute;
        top: 52px;
        left: 0;
        right: 0;
        z-index: 5;
      }
      .cb-vid-slider-arr {
        position: absolute;
        z-index: 5;
        height: 43px;
        width: 43px;
        border-radius: 50%;
        cursor: pointer;
      }
      .cb-vid-slider-arr-prev {
        display: none;
        left: 0;
      }
      .cb-vid-slider-arr-next {
        right: 0;
      }
      .videos-list-carousal {
        overflow: hidden;
        position: relative;
        height: 220px;
      }
      .videos-carousal-wrapper {
        float: none;
        list-style: none;
        padding: 0;
        margin: 0;
        transition: all 0.3s ease;
        display: flex;
        flex-direction: row;
        position: absolute;
        left: 0;
      }
      .videos-carousal-item {
        min-width: 25%;
        justify-content: center;
        align-items: center;
      }
      .cb-vid-more {
        float: right;
        color: #2c3e9a;
        font-size: 18px;
      }
      .cb-vid-more:hover {
        text-decoration: underline;
      }
      .cat-vid-carousal {
        height: 135px !important;
      }
      .cat-vid-carousal .videos-carousal-item {
        min-width: auto;
      }
      .cat-vid-carousal .cb-vid-slider-arrs {
        top: 24px;
      }
      .cb-srs-sqd-box {
        min-height: 700px;
        background: #fff;
      }
      .cb-float-none {
        float: none;
      }
      .cb-margin-top-10 {
        margin-top: 10px;
      }
      .cb-schdl-nvtb {
        margin: 0 0 10px 0;
        padding: 10px;
      }
      .cb-carousal-item-small {
        padding: 0 0 0 16px;
      }
      .cb-carousal-item-small:first-child {
        padding-left: 11px;
      }
      .cb-carousal-item-large {
        padding: 0 11px;
      }
      .cb-carousal-item-small .cb-vid-txt-wrp {
        font-size: 12px;
      }
      .cb-hot-cat .cb-vid-txt-wrp {
        display: -webkit-box;
        -webkit-box-orient: vertical;
        -webkit-line-clamp: 2;
        overflow: hidden;
        max-height: 40px;
      }
      .cb-more-video {
        float: right;
        color: #2c3e9a;
      }
      .cb-more-video:hover {
        text-decoration: underline;
      }
      .home_video .cb-vid-slider-arrs {
        opacity: 0.8;
      }
      .home_matches .cb-vid-slider-arrs {
        opacity: 0.8;
        top: 22px;
      }
      #hm-scag-mtch-blk ul li:not(:first-of-type) {
        padding: 0 11px 0 20px;
      } /*Rankings*/
      .cb-ranking-nav.active {
        line-height: 21px;
      }
      .cb-rank-plyr {
        padding-left: 15px;
      }
      .text-left {
        text-align: left;
      }
      .cb-rank-tabs {
        padding-left: 10px;
      }
      .cb-plyr-tbody {
        padding: 5px 0;
      }
      .cb-padding-left0 {
        padding-left: 0;
      }
      .cb-rank-hdr {
        margin-top: 15px;
        padding: 5px 0;
      }
      .cb-bg-grey {
        background: #f5f5f5;
      } /*Players*/
      .cb-player-name-wrap {
        padding-top: 90px;
      }
      .cb-plyr-tbl {
        margin-top: 30px;
      }
      .cb-font-40 {
        font-size: 40px;
      } /*Teams*/
      .cb-cursor-pointer {
        cursor: pointer;
      }
      .cb-team-stats-btn {
        margin-top: 21px;
      }
      .cb-upper-text {
        text-transform: capitalize;
      }
      .cb-user-icon {
        background-position: -628px -19px;
        height: 20px;
      }
      .cb-user-itm {
        position: absolute;
        top: 0;
        right: 5px;
        padding: 16px 6px 11px;
      } /* Icon specific stylings */
      .cb-ico-premium {
        width: 35px !important;
        height: 50px !important;
        background-position: -527px -5px !important;
      } /* featured matches carousal */
      .hgt-145 {
        height: 145px;
      }
      .cb-mtch-crd-rt {
        margin: 0 0 5px;
      }
      .cb-mtch-crd-rt-itm,
      .cb-match-card {
        height: 100%;
      }
      .cb-mtch-crd-rt-itm {
        padding: 2px 0px;
      }
      .cb-match-card {
        width: 250px;
        box-shadow: 0px 0px 2px rgba(0, 0, 0, 0.12),
          0px 1px 2px rgba(0, 0, 0, 0.12);
        border-radius: 4px;
        margin-right: 10px;
        justify-content: center;
        align-items: center;
        position: relative;
        margin-left: 1px;
        min-width: 250px;
      }
      .cb-mtch-crd-hdr,
      .cb-hmscg-tm-bat-scr,
      .cb-hmscg-tm-bwl-scr,
      .cb-mtch-crd-state,
      .cb-mtch-crd-time,
      .cb-match-footer-body {
        padding: 0px 5px 0px 12px;
      }
      .cb-mtch-crd-hdr {
        display: flex;
        padding-top: 8px;
        width: 230px;
        justify-content: space-between;
      }
      .cb-mtch-crd-liv-strm {
        display: flex;
        justify-content: center;
        align-items: center;
        min-width: 27px;
        border-radius: 24px;
      }
      .cb-vid-ply-btn-red {
        text-align: center;
        width: 11px;
        height: 10px;
        border-radius: 50%;
        line-height: 10px;
      }
      .cb-card-match-format {
        display: block;
        min-width: 28px;
        padding: 1px 0 0;
        border-radius: 24px;
      }
      .cb-hmscg-tm-bat-scr,
      .cb-hmscg-tm-bwl-scr,
      .cb-hmscg-tm-name {
        display: flex;
        align-items: center;
        width: 90%;
      }
      .cb-hmscg-tm-bat-scr {
        padding-top: 5px;
      }
      .cb-hmscg-tm-bwl-scr {
        padding-top: 12px;
      }
      .cb-hmscg-tm-nm-img {
        padding: 3px 5px 0px 0px;
      }
      .cb-img-rad-0 {
        border-radius: 0px;
      }
      .cb-mtch-crd-state,
      .cb-mtch-crd-time {
        padding-top: 20px;
      }
      .cb-match-footer {
        position: absolute;
        bottom: 0px;
        background-color: #f0f0f0;
        border-radius: 0px 0px 4px 4px;
        height: 30px;
      }
      .cb-match-footer-body {
        display: flex;
        justify-content: end;
        padding-top: 4px;
      }
      .cb-match-footer-link {
        color: rgba(0, 0, 0, 0.54);
        margin-left: 10px;
        text-transform: uppercase;
      }
    </style>
    <script>
      function getCookie(c_name) {
        var i,
          x,
          y,
          ARRcookies = document.cookie.split(";");
        for (i = 0; i < ARRcookies.length; i++) {
          x = ARRcookies[i].substr(0, ARRcookies[i].indexOf("="));
          y = ARRcookies[i].substr(ARRcookies[i].indexOf("=") + 1);
          x = x.replace(/^\s+|\s+$/g, "");
          if (x == c_name) {
            return unescape(y);
          }
        }
      }
      var cbads_value = getCookie("cbzads");
      if (cbads_value != null && cbads_value.indexOf("IN|") >= 0) {
        document.write("<style>.cb-geo-in-50{height:50px}</style>");
      }
      /*polifill for remove function*/ if (!("remove" in Element.prototype)) {
        Element.prototype["remove"] = function () {
          if (this.parentNode) {
            this.parentNode.removeChild(this);
          }
        };
      }
    </script>
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <link
      rel="shortcut icon"
      type="image/x-icon"
      href="/images/cb_favicon.ico"
    />
    <meta
      name="google-signin-client_id"
      content="125255339112-d594jen12o0j854sufu8jfn2gbbnaskj.apps.googleusercontent.com"
    />
    <link rel="apple-touch-icon" href="/images/apple-touch-icon.png" />
    <title itemprop="name">
      Cricket scorecard - India vs England, 1st Test, England tour of India,
      2024 | Cricbuzz.com
    </title>
    <meta
      name="description"
      itemprop="description"
      content="Catch live and fully detailed scorecard of India vs England, 1st Test, Jan 25, England tour of India, 2024 on Cricbuzz"
    />
    <link
      rel="alternate"
      href="android-app://com.cricbuzz.android/https/www.cricbuzz.com/cricket-scorecard/21533/ind-vs-aus-2nd-odi-australia-tour-of-india-2019"
    />
    <link
      rel="alternate"
      href="//m.cricbuzz.com/cricket-scorecard/21533/ind-vs-aus-2nd-odi-australia-tour-of-india-2019"
      media="only screen and (max-width: 640px)"
    />
    <meta name="robots" content="index, follow" />
    <meta name="googlebot" content="index, follow" />
    <meta
      name="google-site-verification"
      content="google89fd37b1258ef4b9.html"
    />
    <meta name="msvalidate.01" content="A509FA8BAE50018F9DF2553AEDEDF77B" />
    <meta
      property="og:title"
      content="Cricket scorecard - India vs England, 1st Test, England tour of India, 2024"
    />
    <meta
      property="og:description"
      content="Catch live and fully detailed scorecard of India vs England, 1st Test, Jan 25, England tour of India, 2024 on Cricbuzz"
    />
    <meta property="fb:app_id" content="30119633160" />
    <meta property="og:site_name" content="Cricbuzz" />
    <meta
      property="twitter:title"
      content="Cricket scorecard - India vs England, 1st Test, England tour of India, 2024"
    />
    <meta
      property="twitter:description"
      content="Catch live and fully detailed scorecard of India vs England, 1st Test, Jan 25, England tour of India, 2024 on Cricbuzz"
    />
    <meta name="twitter:site" content="@cricbuzz" />
    <meta name="twitter:domain" content="cricbuzz.com" />
    <meta name="twitter:app:name:iphone" content="Cricbuzz" />
    <meta name="twitter:app:id:iphone" content="360466413" />
    <meta name="twitter:app:name:googleplay" content="Cricbuzz" />
    <meta name="twitter:app:id:googleplay" content="com.cricbuzz.android" />
    <meta name="twitter:widgets:csp" content="on" />
    <meta property="fb:pages" content="178697151159" />
    <meta name="keywords" content="" />
    <meta name="news_keywords" content="" />
    <link
      rel="canonical"
      href="https://www.cricbuzz.com/live-cricket-scorecard/78628/ind-vs-eng-1st-test-england-tour-of-india-2024"
    />
    <meta name="msapplication-config" content="none" />
    <link rel="dns-prefetch" href="https://static.cricbuzz.com/" />
    <script>
      var PAGE_NAME = "scorecard-page";
      var PAGE_TARGETS = {};
      var CBQueue = CBQueue || [];
      var CBQueueOnLoad = CBQueueOnLoad || [];
      /*	Clever Tap */ var CTEventName = "";
      var CTEventObj = {};
      /*CBQueue.push(function(){roadblock(2,{country:["US","CA", "ZA", "AU"], continent:["EU"]});});	CBQueue.push(function(){roadblock(2,{country:["US"]});});*/ _udn =
        "cricbuzz.com";
    </script>
    <script>
      (function (w) {
        "use strict";
        var loadCSS = function (href, before, media) {
          var doc = w.document;
          var ss = doc.createElement("link");
          var ref;
          if (before) {
            ref = before;
          } else {
            var refs = (doc.body || doc.getElementsByTagName("head")[0])
              .childNodes;
            ref = refs[refs.length - 1];
          }
          var sheets = doc.styleSheets;
          ss.rel = "stylesheet";
          ss.href = href;
          ss.media = "only x";
          ref.parentNode.insertBefore(ss, before ? ref : ref.nextSibling);
          var onloadcssdefined = function (cb) {
            var resolvedHref = ss.href;
            var i = sheets.length;
            while (i--) {
              if (sheets[i].href === resolvedHref) {
                return cb();
              }
            }
            setTimeout(function () {
              onloadcssdefined(cb);
            });
          };
          ss.onloadcssdefined = onloadcssdefined;
          onloadcssdefined(function () {
            ss.media = media || "all";
          });
          return ss;
        };
        if (typeof module !== "undefined") {
          module.exports = loadCSS;
        } else {
          w.loadCSS = loadCSS;
        }
      })(typeof global !== "undefined" ? global : this);
      loadCSS("/dist/css/cricbuzz.min.1704179977.css");
    </script>
    <noscript
      ><link
        rel="stylesheet"
        type="text/css"
        href="/dist/css/cricbuzz.min.1704179977.css"
    /></noscript>
  </head>
  <body>
    <script type="text/javascript">
      (function () {
        var user_state =
          localStorage.getItem("PlanState") != null
            ? localStorage.getItem("PlanState")
            : "NOTSET";
        if (user_state == "ACTIVE") {
          var css = ".ad-unit,.cb-ad-unit { display: none; }",
            head = document.head || document.getElementsByTagName("head")[0],
            style = document.createElement("style");
          head.appendChild(style);
          style.type = "text/css";
          if (style.styleSheet) {
            style.styleSheet.cssText = css;
          } else {
            style.appendChild(document.createTextNode(css));
          }
        }
      })();
    </script>
    <a href="https://plus.google.com/104502282508811467249" rel="publisher"></a
    ><a
      id="ad-skin"
      target="_blank"
      href="Javascript:void(0)"
      class="cb-skin-ads-link cb-skin-ads-link-fixed ad-skin"
    ></a
    ><a
      href="Javascript:void(0)"
      class="cb-skin-ads-close cb-font-12 ad-skin-close"
      style="
        position: fixed;
        z-index: 1001;
        color: #fff;
        background: #000;
        padding: 2px 5px;
        right: 2px;
      "
      >&#x2716;</a
    >
    <header
      id="top"
      style="
        z-index: 1000;
        position: relative;
        padding-top: 10px;
        width: 980px;
        margin: 0 auto;
      "
      itemscope
      itemtype="http://schema.org/WPHeader"
    >
      <div class="container">
        <div
          id="leaderboard"
          class="ad-unit text-center center-block"
          style="min-height: 90px; margin-bottom: 10px"
        ></div>
        <div
          id="countdown"
          class="ad-unit"
          style="margin: -10px 15px 0px; float: right; position: absolute"
        ></div>
        <div class="toi-branding toi-referral"></div>
        <nav
          class="cb-nav cb-col cb-col-100"
          id="cb-main-menu"
          ng-controller="CBPlusAuth"
        >
          <a href="/" target="_self" class="cb-hm-text"
            ><img
              id="cb-logo-main-menu"
              itemprop="image"
              height="40"
              width="101"
              style="bottom: 4px; position: relative; vertical-align: middle"
              alt="Cricbuzz Logo"
              title="Cricbuzz Logo"
              src="https://static.cricbuzz.com/images/cb_logo.svg" /></a
          ><a
            class="cb-hm-mnu-itm"
            target="_self"
            href="/cricket-match/live-scores"
            title="Live Cricket Score"
            >Live Scores</a
          ><a
            class="cb-hm-mnu-itm"
            target="_self"
            href="/cricket-schedule/upcoming-series/international"
            title="Cricket Schedule"
            >Schedule</a
          ><a
            class="cb-hm-mnu-itm"
            target="_self"
            href="/cricket-scorecard-archives"
            title="Cricket Scorecard Archives"
            >Archives</a
          >
          <div
            class="cb-subnav cb-hm-mnu-itm feature-button cursor-pointer"
            id="newsDropDown"
            title="Cricket News"
          >
            <a class="text-white" target="_self" href="/cricket-news">News</a
            ><span class="cb-caret-down"></span>
            <nav class="cb-sub-navigation">
              <a
                class="cb-subnav-item"
                target="_self"
                href="/cricket-news"
                title="Latest Cricket News"
                >All Stories</a
              >
              <a
                class="cb-subnav-item"
                target="_self"
                href="/cricket-news/editorial/cb-plus"
                title="Cricbuzz Plus Premium Articles"
                >Cricbuzz Plus</a
              ><a
                class="cb-subnav-item"
                target="_self"
                href="/cricket-news/latest-news"
                title="Latest Cricket News"
                >Latest News</a
              ><a
                class="cb-subnav-item"
                target="_self"
                href="/cricket-news/info/"
                title="Latest Cricket Topics"
                >Topics</a
              ><a
                class="cb-subnav-item"
                target="_self"
                href="/cricket-news/editorial/spotlight"
                title="Cricket Editorials and Specials"
                >Spotlight</a
              ><a
                class="cb-subnav-item"
                target="_self"
                href="/cricket-news/editorial/editorial-list"
                title="Latest Cricket Opinions & Editorials"
                >Opinions</a
              ><a
                class="cb-subnav-item"
                target="_self"
                href="/cricket-news/editorial/specials"
                title="Latest Cricket Specials"
                >Specials</a
              ><a
                class="cb-subnav-item"
                target="_self"
                href="/cricket-news/editorial/stats-analysis"
                title="Latest Cricket Stats & Analysis"
                >Stats & Analysis</a
              ><a
                class="cb-subnav-item"
                target="_self"
                href="/cricket-news/editorial/interviews"
                title="Latest Cricket Player Interviews"
                >Interviews</a
              ><a
                class="cb-subnav-item"
                target="_self"
                href="/cricket-news/editorial/live-blogs"
                title="Latest Cricket Match live blogs"
                >Live Blogs</a
              ><a
                class="cb-subnav-item"
                target="_self"
                href="/cricket-news/experts/harsha-bhogle/170"
                title="Articles and Videos by Harsha Bhogle"
                >Harsha Bhogle</a
              >
            </nav>
          </div>
          <div
            class="cb-subnav cb-hm-mnu-itm feature-button cursor-pointer"
            id="seriesDropDown"
            title="Cricket Series"
          >
            <a class="text-white" target="_self" href="/cricket-schedule/series"
              >Series</a
            ><span class="cb-caret-down"></span>
            <nav class="cb-sub-navigation">
              <a
                class="cb-subnav-item"
                target="_self"
                href="/cricket-series/6927/england-tour-of-india-2024"
                title="England tour of India, 2024"
                >England tour of India, 2024</a
              >
              <a
                class="cb-subnav-item"
                target="_self"
                href="/cricket-series/7175/icc-under-19-world-cup-2024"
                title="ICC Under 19 World Cup 2024"
                >ICC Under 19 World Cup 2024</a
              >
              <a
                class="cb-subnav-item"
                target="_self"
                href="/cricket-series/6297/west-indies-tour-of-australia-2024"
                title="West Indies tour of Australia, 2024"
                >West Indies tour of Australia, 2024</a
              >
              <a
                class="cb-subnav-item"
                target="_self"
                href="/cricket-series/6892/south-africa-tour-of-new-zealand-2024"
                title="South Africa tour of New Zealand, 2024"
                >South Africa tour of New Zealand, 2024</a
              >
              <a
                class="cb-subnav-item"
                target="_self"
                href="/cricket-series/7481/afghanistan-tour-of-sri-lanka-2024"
                title="Afghanistan tour of Sri Lanka, 2024"
                >Afghanistan tour of Sri Lanka, 2024</a
              >
              <a
                class="cb-subnav-item"
                target="_self"
                href="/cricket-series/7044/sa20-2024"
                title="SA20, 2024"
                >SA20, 2024</a
              >
              <a
                class="cb-subnav-item"
                target="_self"
                href="/cricket-series/7257/international-league-t20-2024"
                title="International League T20, 2024"
                >International League T20, 2024</a
              >
              <a
                class="cb-subnav-item"
                target="_self"
                href="/cricket-series/7422/bangladesh-premier-league-2024"
                title="Bangladesh Premier League 2024"
                >Bangladesh Premier League 2024</a
              >
              <a
                class="cb-subnav-item"
                target="_self"
                href="/cricket-series/6725/ranji-trophy-2023-24"
                title="Ranji Trophy 2023-24"
                >Ranji Trophy 2023-24</a
              >
              <a
                class="cb-text-link cb-subnav-item"
                target="_self"
                href="/cricket-schedule/series"
                >All Series »</a
              >
            </nav>
          </div>
          <div
            class="cb-subnav cb-hm-mnu-itm feature-button cursor-pointer"
            id="teamDropDown"
            title="Cricket Teams"
          >
            <a class="text-white" target="_self" href="/cricket-team">Teams</a
            ><span class="cb-caret-down"></span>
            <nav class="cb-sub-navigation cb-sub-lg">
              <div class="cb-sub-lg-outer">
                <div class="cb-sub-lg-sec">
                  <h4 class="cb-sub-lg-sec-head">Test Teams</h4>
                  <a
                    class="cb-subnav-item cb-sub-lg-sec-item"
                    target="_self"
                    href="/cricket-team/india/2"
                    title="India Cricket Team"
                    >India</a
                  >
                  <a
                    class="cb-subnav-item cb-sub-lg-sec-item"
                    target="_self"
                    href="/cricket-team/afghanistan/96"
                    title="Afghanistan Cricket Team"
                    >Afghanistan</a
                  >
                  <a
                    class="cb-subnav-item cb-sub-lg-sec-item"
                    target="_self"
                    href="/cricket-team/ireland/27"
                    title="Ireland Cricket Team"
                    >Ireland</a
                  >
                  <a
                    class="cb-subnav-item cb-sub-lg-sec-item"
                    target="_self"
                    href="/cricket-team/pakistan/3"
                    title="Pakistan Cricket Team"
                    >Pakistan</a
                  >
                  <a
                    class="cb-subnav-item cb-sub-lg-sec-item"
                    target="_self"
                    href="/cricket-team/australia/4"
                    title="Australia Cricket Team"
                    >Australia</a
                  >
                  <a
                    class="cb-subnav-item cb-sub-lg-sec-item"
                    target="_self"
                    href="/cricket-team/sri-lanka/5"
                    title="Sri Lanka Cricket Team"
                    >Sri Lanka</a
                  >
                  <a
                    class="cb-subnav-item cb-sub-lg-sec-item"
                    target="_self"
                    href="/cricket-team/bangladesh/6"
                    title="Bangladesh Cricket Team"
                    >Bangladesh</a
                  >
                  <a
                    class="cb-subnav-item cb-sub-lg-sec-item"
                    target="_self"
                    href="/cricket-team/england/9"
                    title="England Cricket Team"
                    >England</a
                  >
                  <a
                    class="cb-subnav-item cb-sub-lg-sec-item"
                    target="_self"
                    href="/cricket-team/west-indies/10"
                    title="West Indies Cricket Team"
                    >West Indies</a
                  >
                  <a
                    class="cb-subnav-item cb-sub-lg-sec-item"
                    target="_self"
                    href="/cricket-team/south-africa/11"
                    title="South Africa Cricket Team"
                    >South Africa</a
                  >
                  <a
                    class="cb-subnav-item cb-sub-lg-sec-item"
                    target="_self"
                    href="/cricket-team/zimbabwe/12"
                    title="Zimbabwe Cricket Team"
                    >Zimbabwe</a
                  >
                  <a
                    class="cb-subnav-item cb-sub-lg-sec-item"
                    target="_self"
                    href="/cricket-team/new-zealand/13"
                    title="New Zealand Cricket Team"
                    >New Zealand</a
                  >
                </div>
                <div class="cb-sub-lg-sec">
                  <h4 class="cb-sub-lg-sec-head">Associate</h4>
                  <a
                    class="cb-subnav-item cb-sub-lg-sec-item"
                    target="_self"
                    href="/cricket-team/malaysia/71"
                    title="Malaysia Cricket Team"
                    >Malaysia</a
                  >
                  <a
                    class="cb-subnav-item cb-sub-lg-sec-item"
                    target="_self"
                    href="/cricket-team/nepal/72"
                    title="Nepal Cricket Team"
                    >Nepal</a
                  >
                  <a
                    class="cb-subnav-item cb-sub-lg-sec-item"
                    target="_self"
                    href="/cricket-team/germany/77"
                    title="Germany Cricket Team"
                    >Germany</a
                  >
                  <a
                    class="cb-subnav-item cb-sub-lg-sec-item"
                    target="_self"
                    href="/cricket-team/namibia/161"
                    title="Namibia Cricket Team"
                    >Namibia</a
                  >
                  <a
                    class="cb-subnav-item cb-sub-lg-sec-item"
                    target="_self"
                    href="/cricket-team/denmark/185"
                    title="Denmark Cricket Team"
                    >Denmark</a
                  >
                  <a
                    class="cb-subnav-item cb-sub-lg-sec-item"
                    target="_self"
                    href="/cricket-team/singapore/190"
                    title="Singapore Cricket Team"
                    >Singapore</a
                  >
                  <a
                    class="cb-subnav-item cb-sub-lg-sec-item"
                    target="_self"
                    href="/cricket-team/papua-new-guinea/287"
                    title="Papua New Guinea Cricket Team"
                    >Papua New Guinea</a
                  >
                  <a
                    class="cb-subnav-item cb-sub-lg-sec-item"
                    target="_self"
                    href="/cricket-team/kuwait/298"
                    title="Kuwait Cricket Team"
                    >Kuwait</a
                  >
                  <a
                    class="cb-subnav-item cb-sub-lg-sec-item"
                    target="_self"
                    href="/cricket-team/vanuatu/300"
                    title="Vanuatu Cricket Team"
                    >Vanuatu</a
                  >
                  <a
                    class="cb-subnav-item cb-sub-lg-sec-item"
                    target="_self"
                    href="/cricket-team/jersey/303"
                    title="Jersey Cricket Team"
                    >Jersey</a
                  >
                  <a
                    class="cb-subnav-item cb-sub-lg-sec-item"
                    target="_self"
                    href="/cricket-team/oman/304"
                    title="Oman Cricket Team"
                    >Oman</a
                  >
                  <a
                    class="cb-subnav-item cb-sub-lg-sec-item"
                    target="_self"
                    href="/cricket-team/fiji/343"
                    title="Fiji Cricket Team"
                    >Fiji</a
                  >
                </div>
              </div>
              <a target="_self" href="/cricket-team" class="cb-sub-lg-more"
                >More...</a
              >
            </nav>
          </div>
          <div
            class="cb-subnav cb-hm-mnu-itm feature-button cursor-pointer"
            id="videosDropDown"
            title="Cricket Videos"
          >
            <a class="text-white" target="_self" href="/cricket-videos"
              >Videos</a
            ><span class="cb-caret-down"></span>
            <nav class="cb-sub-navigation">
              <a
                target="_self"
                class="cb-subnav-item"
                href="/cricket-videos"
                title="All Cricket Videos"
                >All Videos</a
              >
              <a
                target="_self"
                class="cb-subnav-item"
                href="/cricket-videos/categories"
                title="Cricket Videos Categories"
                >Categories</a
              >
              <a
                target="_self"
                class="cb-subnav-item"
                href="/cricket-videos/playlists"
                title="Cricket Videos Playlists"
                >Playlists</a
              >
            </nav>
          </div>
          <div
            class="cb-subnav cb-hm-mnu-itm feature-button cursor-pointer"
            id="rankingDropDown"
            title="ICC Rankings"
          >
            <a class="text-white" href="/cricket-stats/icc-rankings/men/batting"
              >Rankings</a
            ><span class="cb-caret-down"></span>
            <nav class="cb-sub-navigation">
              <a
                class="cb-subnav-item"
                target="_self"
                href="/cricket-stats/icc-rankings/men/batting"
                title="ICC Rankings Men"
                >ICC Rankings - Men</a
              ><a
                class="cb-subnav-item"
                target="_self"
                href="/cricket-stats/icc-rankings/women/batting"
                title="ICC Rankings Women"
                >ICC Rankings - Women</a
              >
            </nav>
          </div>
          <div class="cb-subnav cb-hm-mnu-itm feature-button cursor-pointer">
            More<span class="cb-caret-down"></span>
            <nav class="cb-sub-navigation" style="right: 0px">
              <a
                class="cb-subnav-item"
                target="_self"
                href="/cricket-stats/points-table/test/icc-world-test-championship"
                title="World Test Championship"
                >World Test Championship</a
              >
              <a
                class="cb-subnav-item"
                target="_self"
                href="/ipl-live-streaming"
                title="IPL Live Stream"
                >IPL Live Stream</a
              >
              <a
                class="cb-subnav-item"
                target="_self"
                href="/cricket-stats/points-table/odi/icc-men-cricket-world-cup-super-league"
                title="World Cup Super League"
                >World Cup Super League</a
              >
              <a
                class="cb-subnav-item"
                target="_self"
                href="/cricket-photo-gallery"
                title="Photo Gallery"
                >Photos</a
              >
              <a
                class="cb-subnav-item"
                target="_self"
                href="/mobileapps"
                title="Mobile Apps"
                >Mobile Apps</a
              ><a
                class="cb-subnav-item"
                target="_self"
                href="/careers"
                title="Careers"
                >Careers</a
              ><a
                class="cb-subnav-item"
                target="_self"
                href="/info/contact"
                title="Contact Us"
                >Contact Us</a
              >
            </nav>
          </div>
          <a
            href="/cb-plus/premium-content/home"
            class="cb-plus-menu-button cb-text-gray"
            id="cricbuzz-plus-main-menu"
          >
            Cricbuzz Plus
          </a>
          <div
            ng-controller="SearchCtrl"
            ng-init=" init(-1, 61, 76, 350, '', 'nav')"
          >
            <div
              id="main-menu_search"
              class="cb-nav-search-wrap"
              ng-style="{width: inputFocus?'800px':'30px'}"
            >
              <div class="cb-col-100 cb-col cb-srch-bar cb-srch-bar-nav">
                <form
                  ng-submit="search_results(false, false)"
                  name="form"
                  class="cb-search-form"
                  ng-cloak
                >
                  <div class="cb-search-input-nav">
                    <div class="cb-search-outer">
                      <div
                        class="cb-search-input-wrap"
                        ng-blur="loseInputFocus()"
                        ng-click="onInputFocus()"
                      >
                        <input
                          type="text"
                          class="js-cb-search-input cb-search-input-elem cb-search-input-elem-nav form-control cb-car-inp cb-srch-bg"
                          ng-change="suggest_search()"
                          maxlength="500"
                          ng-model="searchText"
                          id="search_bar_menu"
                          name="search"
                          value="suggest.title"
                          autocomplete="off"
                          ng-class="{'cb-search-input-elem-error-nav':errorText, 'cb-srch-high-zIndex':dropdownVisible, 'cb-srch-input-focus':inputFocus}"
                          placeholder="{{errorText?errorText:(source == 'nav' && inputFocus) || source == 'search-page'?'Search for Player, Series, Team, News or Video. eg: Windies tour of India': ''}}"
                          ng-keydown="onKeyPress($event)"
                          ng-focus="onInputFocus()"
                          ng-blur="loseInputFocus()"
                          ng-model-options="{ debounce: 400 }"
                        />
                        <span
                          class="cb-ico cb-search-input-icon cb-search-input-icon-nav"
                        ></span>
                        <span
                          class="cb-srch-cross-new cb-srch-cross-new-nav cb-font-14"
                          ng-class="{'cb-srch-cross-focus': inputFocus, 'cb-srch-high-zIndex':dropdownVisible, 'disp-none':clearVisible}"
                          ng-click="reset_form('view');"
                          ng-show="searchText.length > 0"
                          id="cb-search-menubar-clear"
                          >✖</span
                        >
                      </div>
                      <div
                        ng-show="dropdownVisible"
                        class="cb-srch-backdrop"
                        ng-click="hideDropdown()"
                      ></div>
                      <div
                        ng-show="dropdownVisible && searchText.length >= 2 && search_ftr_suggst.length > 0"
                        class="cb-main-srch-box-wrap"
                      >
                        <ul class="cb-main-srch-box" id="searchBox_nav">
                          <li
                            class="cb-main-srch-box-item {{selected_suggestions == $index?'highlight':''}}"
                            id="search_item_{{$index}}"
                            ng-click="search_results()"
                            ng-repeat="suggest in search_ftr_suggst track by $index"
                            ng-show="suggestions && searchText.length > 0 && inputFocus"
                            ng-mouseover="highlight_item_mouse_hover($index)"
                            ng-class="{'cb-main-srch-box-item-border':suggest.hasBorder, 'cb-big': suggest.isSearchItem}"
                          >
                            <a
                              ng-if="!suggest.isSearchItem"
                              class="text-black cb-srch-suggest-link"
                            >
                              <div
                                class="cb-srch-suggest-img"
                                ng-class="{'cb-srch-suggest-img-teams': suggest.type == 'Teams'}"
                              >
                                <div ng-if="suggest.imgUrl" class="">
                                  <img
                                    class="cb-srch-suggest-icon-img"
                                    ng-src="{{suggest.imgUrl}}"
                                  />
                                </div>
                                <div
                                  ng-if="!suggest.imgUrl"
                                  class="cb-srch-sugggest-icon {{suggest.iconClass}} cb-ico"
                                ></div>
                              </div>
                              <div class="cb-srch-suggest-content">
                                <p
                                  class="cb-srch-suggest-content-title"
                                  ng-bind-html="suggest | searchfilter:oldText"
                                ></p>
                                <p
                                  class="cb-srch-suggest-content-subtitle cb-font-12 cb-text-gray"
                                >
                                  {{suggest.tag}}
                                </p>
                              </div>
                            </a>
                            <a
                              ng-if="suggest.isSearchItem"
                              href="javascript:void(0)"
                              class="text-black cb-srch-suggest-link"
                            >
                              <div class="cb-srch-suggest-img">
                                <div
                                  class="cb-srch-sugggest-icon cb-srch-sugggest-icon-search cb-ico"
                                ></div>
                              </div>
                              <div
                                class="cb-srch-suggest-content cb-center-text"
                              >
                                <p class="cb-srch-suggest-content-title">
                                  Search for &#8220;<span
                                    ng-bind="searchText"
                                  ></span
                                  >&#8221;
                                </p>
                              </div>
                            </a>
                          </li>
                        </ul>
                      </div>
                    </div>
                  </div>
                  <div
                    class="cb-search-submit-nav"
                    ng-class="{'cb-search-submit-input-focus': inputFocus, 'cb-search-submit-error': errorText}"
                  >
                    <a
                      class="text-white cb-srch-bttn"
                      ng-class="{'cb-srch-high-zIndex':dropdownVisible}"
                      ng-click="search_results(false, true)"
                      >SEARCH</a
                    >
                  </div>
                  <input type="hidden" name="anticsrf" value="bowled" />
                </form>
              </div>
              <style>
                .cb-srch-ico {
                  margin: 0;
                }
                .cb-user-itm {
                  position: absolute;
                  top: 0;
                  right: 5px;
                }
              </style>
            </div>
          </div>
          <div class="cb-user-itm cb-subnav">
            <a
              id="cb-plus-user-icon"
              href="/premium-subscription/user/account-info"
              ><span class="cb-plus-ico cb-user-icon"></span
            ></a>
            <nav
              id="cb-plus-dropdown"
              class="cb-sub-navigation"
              style="right: 0px"
            >
              <a
                class="cb-subnav-item"
                target="_self"
                href="/premium-subscription/user/account-info"
                title="My Account"
                >My Account</a
              >
              <a
                class="cb-subnav-item"
                target="_self"
                title="Sign Out"
                ng-click="sign_out_user(false)"
                >Sign Out</a
              >
            </nav>
          </div>
        </nav>
        <style>
          .cb-text-link {
            color: #1866db;
          }
          .cb-plus-menu-button {
            padding: 8px 14px;
            background: #fff;
            border-radius: 18px;
            border: 0;
          }
          .cb-plus-menu-button:hover,
          .cb-plus-menu-button:focus,
          .cb-plus-menu-button:active {
            background: #fff;
          }
        </style>
      </div>
    </header>
    <div class="page">
      <div id="fb-root"></div>
      <div id="page-wrapper" class="container" style="display: inline-block">
        <div
          id="shosh"
          class="ad-unit shosh-embed"
          style="height: 0; width: 980px; text-align: center"
        ></div>
        <span
          id="skin_left"
          class="ad-unit"
          style="
            overflow: hidden;
            position: fixed;
            top: 0;
            left: calc(50% - 635px);
            margin-right: 3px;
            z-index: -99;
          "
        ></span>
        <div
          class="html-refresh"
          url="/api/html/matches-menu"
          timeout="300000"
          disable-first-load="true"
        >
          <div class="cb-col cb-col-100 mrgn-btm-5">
            <nav class="cb-mat-mnu" ng-init="direction='up'">
              <a
                class="cb-mat-mnu-itm cb-ovr-flo cb-mat-mnu-ttl"
                target="_self"
                title=""
                href="/cricket-match/live-scores"
                id="live-scores-link"
                >MATCHES</a
              ><a
                class="cb-mat-mnu-itm cb-ovr-flo"
                title="Durban Super Giants v Pretoria Capitals, 24th Match - Live"
                href="/live-cricket-scores/80078/dsg-vs-pc-24th-match-sa20-2024"
                target="_self"
                >DSG vs PC - Live</a
              ><a
                class="cb-mat-mnu-itm cb-ovr-flo"
                title="MI Emirates v Desert Vipers, 15th Match - Live"
                href="/live-cricket-scores/82829/mie-vs-dv-15th-match-international-league-t20-2024"
                target="_self"
                >MIE vs DV - Live</a
              ><a
                class="cb-mat-mnu-itm cb-ovr-flo"
                title="Fortune Barishal v Sylhet Strikers, 16th Match - Live"
                href="/live-cricket-scores/86994/brsal-vs-syst-16th-match-bangladesh-premier-league-2024"
                target="_self"
                >BRSAL vs SYST - Live</a
              ><a
                class="cb-mat-mnu-itm cb-ovr-flo"
                title="India U19 v New Zealand U19, 25th Match, Super Six, Group 1 - INDU19 Won"
                href="/live-cricket-scores/86634/indu19-vs-nzu19-25th-match-super-six-group-1-icc-under-19-world-cup-2024"
                target="_self"
                >INDU19 vs NZU19 - INDU19 Won</a
              ><a
                class="cb-mat-mnu-itm cb-ovr-flo"
                title="Rangpur Riders v Comilla Victorians, 15th Match - RGR Won"
                href="/live-cricket-scores/86991/rgr-vs-cv-15th-match-bangladesh-premier-league-2024"
                target="_self"
                >RGR vs CV - RGR Won</a
              ><span
                ng-click="(direction=='up')?direction = 'down' : direction = 'up'"
                ><a
                  class="cb-mat-mnu-itm cb-mat-mnu-all"
                  ng-class="{true:'cb-mat-mnu-cls'}[direction=='down']"
                  id="match-dropdown"
                  ><span ng-bind="(direction=='up') ? 'ALL': 'CLOSE'"></span
                  ><span
                    ng-class="(direction=='up') ? 'cb-caret-down' : 'cb-caret-up'"
                  ></span></a
              ></span>
            </nav>
            <div id="matchmenu">
              <div class="cb-mm-wrp {{direction}}">
                <div
                  class="cb-scg-drp-dwn cb-col cb-col-100 cb-mnu-{{direction}}"
                >
                  <nav class="nav cb-mm-nvtb" ng-init="option= 'all'">
                    <a
                      class="cb-nav-pill-2 {{(option=='all')?'active':''}}"
                      ng-click="option='all'"
                      style="margin-right: 20px"
                      >All</a
                    ><a
                      class="cb-nav-pill-2 {{(option=='live')?'active':''}}"
                      ng-click="option='live'"
                      style="margin-right: 20px"
                      >Live Now</a
                    ><a
                      class="cb-nav-pill-2 {{(option=='today')?'active':''}}"
                      ng-click="option='today'"
                      style="margin-right: 20px"
                      >Today</a
                    >
                  </nav>
                  <style>
                    .cb-nt-{{option}}{opacity:0.4!important;}
                  </style>
                  <ul class="cb-scg-drp-dwn-ul">
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mm-typ">INTERNATIONAL</div>
                        <div class="cb-scg-srs-nm">IND V ENG, 2024</div>
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/78628/eng-vs-ind-1st-test-ind-v-eng-2024"
                            title="England v India, 1st Test - ENG Won"
                            ><span class="cb-mm-mtch-tm">England vs India</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">1st Test</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-scg-srs-nm">
                          Australia V West Indies, 2024
                        </div>
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/70333/wi-vs-aus-2nd-test-australia-v-west-indies-2024"
                            title="West Indies v Australia, 2nd Test - WI Won"
                            ><span class="cb-mm-mtch-tm"
                              >West Indies vs Australia</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">2nd Test</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-scg-srs-nm">
                          ACC Mens T20I Challenger Cup
                        </div>
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/88284/chn-vs-mmr-3rd-match-qualifiers-acc-mens-t20i-challenger-cup"
                            title="China v Myanmar, 3rd Match, Qualifiers - MMR Won"
                            ><span class="cb-mm-mtch-tm">China vs Myanmar</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">3rd Match, Qualifiers</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live">
                          <a
                            target="_self"
                            href="/live-cricket-scores/88291/chn-vs-mmr-9th-place-play-off-acc-mens-t20i-challenger-cup"
                            title="China v Myanmar, 9th Place Play-off - CHN Won"
                            ><span class="cb-mm-mtch-tm">China vs Myanmar</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">9th Place Play-off</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/88298/sau-vs-cbd-1st-match-group-a-acc-mens-t20i-challenger-cup"
                            title="Saudi Arabia v Cambodia, 1st Match, Group A - Upcoming"
                            ><span class="cb-mm-mtch-tm"
                              >Saudi Arabia vs Cambodia</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">1st Match, Group A</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/88305/idn-vs-btn-2nd-match-group-a-acc-mens-t20i-challenger-cup"
                            title="Indonesia v Bhutan, 2nd Match, Group A - Upcoming"
                            ><span class="cb-mm-mtch-tm"
                              >Indonesia vs Bhutan</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">2nd Match, Group A</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mm-typ">T20 LEAGUE</div>
                        <div class="cb-scg-srs-nm">SA20</div>
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/80068/dsg-vs-pr-22nd-match-sa20"
                            title="Durban Super Giants v Paarl Royals, 22nd Match - DSG Won"
                            ><span class="cb-mm-mtch-tm"
                              >Durban Super Giants vs Paarl Royals</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">22nd Match</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/80075/mict-vs-jsk-23rd-match-sa20"
                            title="MI Cape Town v Joburg Super Kings, 23rd Match - JSK Won"
                            ><span class="cb-mm-mtch-tm"
                              >MI Cape Town vs Joburg Super Kings</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">23rd Match</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all">
                          <a
                            target="_self"
                            href="/live-cricket-scores/80078/dsg-vs-pc-24th-match-sa20"
                            title="Durban Super Giants v Pretoria Capitals, 24th Match - Live"
                            ><span class="cb-mm-mtch-tm"
                              >Durban Super Giants vs Pretoria Capitals</span
                            ><span class="cb-mm-liv-tag"
                              >&nbsp;&nbsp;LIVE</span
                            ></a
                          >
                          <div class="cb-mm-mtch-nm">24th Match</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/80082/jsk-vs-sec-25th-match-sa20"
                            title="Joburg Super Kings v Sunrisers Eastern Cape, 25th Match - Upcoming"
                            ><span class="cb-mm-mtch-tm"
                              >Joburg Super Kings vs Sunrisers Eastern
                              Cape</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">25th Match</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/80085/pc-vs-mict-26th-match-sa20"
                            title="Pretoria Capitals v MI Cape Town, 26th Match - Upcoming"
                            ><span class="cb-mm-mtch-tm"
                              >Pretoria Capitals vs MI Cape Town</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">26th Match</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-scg-srs-nm">
                          International League T20, 2024
                        </div>
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/82815/sw-vs-dv-13th-match-international-league-t20-2024"
                            title="Sharjah Warriors v Desert Vipers, 13th Match - SW Won"
                            ><span class="cb-mm-mtch-tm"
                              >Sharjah Warriors vs Desert Vipers</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">13th Match</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/82822/dcp-vs-sw-14th-match-international-league-t20-2024"
                            title="Dubai Capitals v Sharjah Warriors, 14th Match - SW Won"
                            ><span class="cb-mm-mtch-tm"
                              >Dubai Capitals vs Sharjah Warriors</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">14th Match</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all">
                          <a
                            target="_self"
                            href="/live-cricket-scores/82829/mie-vs-dv-15th-match-international-league-t20-2024"
                            title="MI Emirates v Desert Vipers, 15th Match - Live"
                            ><span class="cb-mm-mtch-tm"
                              >MI Emirates vs Desert Vipers</span
                            ><span class="cb-mm-liv-tag"
                              >&nbsp;&nbsp;LIVE</span
                            ></a
                          >
                          <div class="cb-mm-mtch-nm">15th Match</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/82836/adkr-vs-gg-16th-match-international-league-t20-2024"
                            title="Abu Dhabi Knight Riders v Gulf Giants, 16th Match - Upcoming"
                            ><span class="cb-mm-mtch-tm"
                              >Abu Dhabi Knight Riders vs Gulf Giants</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">16th Match</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/82843/dcp-vs-dv-17th-match-international-league-t20-2024"
                            title="Dubai Capitals v Desert Vipers, 17th Match - Upcoming"
                            ><span class="cb-mm-mtch-tm"
                              >Dubai Capitals vs Desert Vipers</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">17th Match</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-scg-srs-nm">BPL 2024</div>
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/86980/syst-vs-cgc-13th-match-bpl-2024"
                            title="Sylhet Strikers v Chattogram Challengers, 13th Match - CGC Won"
                            ><span class="cb-mm-mtch-tm"
                              >Sylhet Strikers vs Chattogram Challengers</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">13th Match</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/86984/drd-vs-klt-14th-match-bpl-2024"
                            title="Durdanto Dhaka v Khulna Tigers, 14th Match - KLT Won"
                            ><span class="cb-mm-mtch-tm"
                              >Durdanto Dhaka vs Khulna Tigers</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">14th Match</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live">
                          <a
                            target="_self"
                            href="/live-cricket-scores/86991/rgr-vs-cv-15th-match-bpl-2024"
                            title="Rangpur Riders v Comilla Victorians, 15th Match - RGR Won"
                            ><span class="cb-mm-mtch-tm"
                              >Rangpur Riders vs Comilla Victorians</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">15th Match</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all">
                          <a
                            target="_self"
                            href="/live-cricket-scores/86994/brsal-vs-syst-16th-match-bpl-2024"
                            title="Fortune Barishal v Sylhet Strikers, 16th Match - Live"
                            ><span class="cb-mm-mtch-tm"
                              >Fortune Barishal vs Sylhet Strikers</span
                            ><span class="cb-mm-liv-tag"
                              >&nbsp;&nbsp;LIVE</span
                            ></a
                          >
                          <div class="cb-mm-mtch-nm">16th Match</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mm-typ">DOMESTIC</div>
                        <div class="cb-scg-srs-nm">
                          ICC Under 19 World Cup 2024
                        </div>
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/86627/slu19-vs-ausu19-24th-match-group-c-icc-under-19-world-cup-2024"
                            title="Sri Lanka U19 v Australia U19, 24th Match, Group C - AUSU19 Won"
                            ><span class="cb-mm-mtch-tm"
                              >Sri Lanka U19 vs Australia U19</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">24th Match, Group C</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/86623/indu19-vs-usau19-23rd-match-group-a-icc-under-19-world-cup-2024"
                            title="India U19 v United States U19, 23rd Match, Group A - INDU19 Won"
                            ><span class="cb-mm-mtch-tm"
                              >India U19 vs United States U19</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">23rd Match, Group A</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live">
                          <a
                            target="_self"
                            href="/live-cricket-scores/86641/ireu19-vs-paku19-27th-match-super-six-group-1-icc-under-19-world-cup-2024"
                            title="Ireland U19 v Pakistan U19, 27th Match, Super Six, Group 1 - Complete"
                            ><span class="cb-mm-mtch-tm"
                              >Ireland U19 vs Pakistan U19</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">
                            27th Match, Super Six, Group 1
                          </div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all">
                          <a
                            target="_self"
                            href="/live-cricket-scores/86637/slu19-vs-wiu19-26th-match-super-six-group-2-icc-under-19-world-cup-2024"
                            title="Sri Lanka U19 v West Indies U19, 26th Match, Super Six, Group 2 - Live"
                            ><span class="cb-mm-mtch-tm"
                              >Sri Lanka U19 vs West Indies U19</span
                            ><span class="cb-mm-liv-tag"
                              >&nbsp;&nbsp;LIVE</span
                            ></a
                          >
                          <div class="cb-mm-mtch-nm">
                            26th Match, Super Six, Group 2
                          </div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live">
                          <a
                            target="_self"
                            href="/live-cricket-scores/86634/indu19-vs-nzu19-25th-match-super-six-group-1-icc-under-19-world-cup-2024"
                            title="India U19 v New Zealand U19, 25th Match, Super Six, Group 1 - INDU19 Won"
                            ><span class="cb-mm-mtch-tm"
                              >India U19 vs New Zealand U19</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">
                            25th Match, Super Six, Group 1
                          </div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/88895/afgu19-vs-usau19-28th-match-16th-place-play-off-icc-under-19-world-cup-2024"
                            title="Afghanistan U19 v United States U19, 28th Match, 16th Place Play Off - Upcoming"
                            ><span class="cb-mm-mtch-tm"
                              >Afghanistan U19 vs United States U19</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">
                            28th Match, 16th Place Play Off
                          </div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/86658/ausu19-vs-engu19-30th-match-super-six-group-2-icc-under-19-world-cup-2024"
                            title="Australia U19 v England U19, 30th Match, Super Six, Group 2 - Preview"
                            ><span class="cb-mm-mtch-tm"
                              >Australia U19 vs England U19</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">
                            30th Match, Super Six, Group 2
                          </div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/86651/nplu19-vs-banu19-29th-match-super-six-group-1-icc-under-19-world-cup-2024"
                            title="Nepal U19 v Bangladesh U19, 29th Match, Super Six, Group 1 - Preview"
                            ><span class="cb-mm-mtch-tm"
                              >Nepal U19 vs Bangladesh U19</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">
                            29th Match, Super Six, Group 1
                          </div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/86644/zimu19-vs-rsau19-31st-match-super-six-group-2-icc-under-19-world-cup-2024"
                            title="Zimbabwe U19 v South Africa U19, 31st Match, Super Six, Group 2 - Preview"
                            ><span class="cb-mm-mtch-tm"
                              >Zimbabwe U19 vs South Africa U19</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">
                            31st Match, Super Six, Group 2
                          </div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/86672/scou19-vs-namu19-32nd-match-16th-place-play-off-icc-under-19-world-cup-2024"
                            title="Scotland U19 v Namibia U19, 32nd Match, 16th Place Play Off - Upcoming"
                            ><span class="cb-mm-mtch-tm"
                              >Scotland U19 vs Namibia U19</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">
                            32nd Match, 16th Place Play Off
                          </div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-scg-srs-nm">Ranji Trophy</div>
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/74380/skm-vs-ngl-plate-ranji-trophy"
                            title="Sikkim v Nagaland, Plate - NGL Won"
                            ><span class="cb-mm-mtch-tm"
                              >Sikkim vs Nagaland</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">Plate</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/74310/ben-vs-asm-elite-group-b-ranji-trophy"
                            title="Bengal v Assam, Elite Group B - BEN Won"
                            ><span class="cb-mm-mtch-tm">Bengal vs Assam</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">Elite Group B</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/74331/kar-vs-tri-elite-group-c-ranji-trophy"
                            title="Karnataka v Tripura, Elite Group C - KAR Won"
                            ><span class="cb-mm-mtch-tm"
                              >Karnataka vs Tripura</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">Elite Group C</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/74321/ap-vs-cg-elite-group-b-ranji-trophy"
                            title="Andhra v Chhattisgarh, Elite Group B - AP Won"
                            ><span class="cb-mm-mtch-tm"
                              >Andhra vs Chhattisgarh</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">Elite Group B</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/74356/vid-vs-jhkd-elite-group-a-ranji-trophy"
                            title="Vidarbha v Jharkhand, Elite Group A - VID Won"
                            ><span class="cb-mm-mtch-tm"
                              >Vidarbha vs Jharkhand</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">Elite Group A</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/74377/odsa-vs-hp-elite-group-d-ranji-trophy"
                            title="Odisha v Himachal Pradesh, Elite Group D - ODSA Won"
                            ><span class="cb-mm-mtch-tm"
                              >Odisha vs Himachal Pradesh</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">Elite Group D</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/74328/ker-vs-bih-elite-group-b-ranji-trophy"
                            title="Kerala v Bihar, Elite Group B - Match drawn"
                            ><span class="cb-mm-mtch-tm">Kerala vs Bihar</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">Elite Group B</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/74363/har-vs-mah-elite-group-a-ranji-trophy"
                            title="Haryana v Maharashtra, Elite Group A - Match drawn"
                            ><span class="cb-mm-mtch-tm"
                              >Haryana vs Maharashtra</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">Elite Group A</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/74324/mum-vs-up-elite-group-b-ranji-trophy"
                            title="Mumbai v Uttar Pradesh, Elite Group B - UP Won"
                            ><span class="cb-mm-mtch-tm"
                              >Mumbai vs Uttar Pradesh</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">Elite Group B</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/74359/mp-vs-pdc-elite-group-d-ranji-trophy"
                            title="Madhya Pradesh v Puducherry, Elite Group D - MP Won"
                            ><span class="cb-mm-mtch-tm"
                              >Madhya Pradesh vs Puducherry</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">Elite Group D</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/74391/miz-vs-mgly-plate-ranji-trophy"
                            title="Mizoram v Meghalaya, Plate - MIZ Won"
                            ><span class="cb-mm-mtch-tm"
                              >Mizoram vs Meghalaya</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">Plate</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/74317/jk-vs-brd-elite-group-d-ranji-trophy"
                            title="Jammu and Kashmir v Baroda, Elite Group D - Match drawn"
                            ><span class="cb-mm-mtch-tm"
                              >Jammu and Kashmir vs Baroda</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">Elite Group D</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/74349/cdg-vs-tn-elite-group-c-ranji-trophy"
                            title="Chandigarh v Tamil Nadu, Elite Group C - TN Won"
                            ><span class="cb-mm-mtch-tm"
                              >Chandigarh vs Tamil Nadu</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">Elite Group C</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/74387/arnp-vs-hyd-plate-ranji-trophy"
                            title="Arunachal Pradesh v Hyderabad, Plate - HYD Won"
                            ><span class="cb-mm-mtch-tm"
                              >Arunachal Pradesh vs Hyderabad</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">Plate</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/74342/ser-vs-saur-elite-group-a-ranji-trophy"
                            title="Services v Saurashtra, Elite Group A - Match drawn"
                            ><span class="cb-mm-mtch-tm"
                              >Services vs Saurashtra</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">Elite Group A</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/74338/rlys-vs-guj-elite-group-c-ranji-trophy"
                            title="Railways v Gujarat, Elite Group C - RLYS Won"
                            ><span class="cb-mm-mtch-tm"
                              >Railways vs Gujarat</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">Elite Group C</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/74335/goa-vs-pun-elite-group-c-ranji-trophy"
                            title="Goa v Punjab, Elite Group C - PUN Won"
                            ><span class="cb-mm-mtch-tm">Goa vs Punjab</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">Elite Group C</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/74373/mnp-vs-raj-elite-group-a-ranji-trophy"
                            title="Manipur v Rajasthan, Elite Group A - RAJ Won"
                            ><span class="cb-mm-mtch-tm"
                              >Manipur vs Rajasthan</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">Elite Group A</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/74366/del-vs-utk-elite-group-d-ranji-trophy"
                            title="Delhi v Uttarakhand, Elite Group D - DEL Won"
                            ><span class="cb-mm-mtch-tm"
                              >Delhi vs Uttarakhand</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">Elite Group D</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-scg-srs-nm">Ford Trophy</div>
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/79480/nk-vs-akl-16th-match-ford-trophy"
                            title="Northern Knights v Auckland, 16th Match - Upcoming"
                            ><span class="cb-mm-mtch-tm"
                              >Northern Knights vs Auckland</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">16th Match</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-scg-srs-nm">
                          England Lions tour of India
                        </div>
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/87353/inda-vs-enga-3rd-unofficial-test-england-lions-tour-of-india"
                            title="India A v England Lions, 3rd unofficial Test - Upcoming"
                            ><span class="cb-mm-mtch-tm"
                              >India A vs England Lions</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">3rd unofficial Test</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-scg-srs-nm">
                          Australia Domestic One-Day Cup 2023-24
                        </div>
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/79182/wa-vs-nsw-16th-match-australia-domestic-one-day-cup-2023-24"
                            title="Western Australia v New South Wales, 16th Match - Upcoming"
                            ><span class="cb-mm-mtch-tm"
                              >Western Australia vs New South Wales</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">16th Match</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-scg-srs-nm">
                          CSA Four-Day Series Division Two 2023-24
                        </div>
                        <div class="cb-mtch-all cb-nt-live cb-nt-today">
                          <a
                            target="_self"
                            href="/live-cricket-scores/82539/bor-vs-kng-15th-match-csa-four-day-series-division-two-2023-24"
                            title="Border v Knights, 15th Match - Upcoming"
                            ><span class="cb-mm-mtch-tm">Border vs Knights</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">15th Match</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-mm-typ">WOMEN</div>
                        <div class="cb-scg-srs-nm">
                          Zimbabwe Women v Ireland Women, 2024
                        </div>
                        <div class="cb-mtch-all cb-nt-live">
                          <a
                            target="_self"
                            href="/live-cricket-scores/88172/irew-vs-zimw-3rd-t20i-zimbabwe-women-v-ireland-women-2024"
                            title="Ireland Women v Zimbabwe Women, 3rd T20I - IREW Won"
                            ><span class="cb-mm-mtch-tm"
                              >Ireland Women vs Zimbabwe Women</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">3rd T20I</div>
                        </div>
                      </div>
                    </li>
                    <li class="cb-lst-mtch cb-lst-dom">
                      <div style="display: inline-block">
                        <div class="cb-scg-srs-nm">
                          Australia Women v South Africa Women
                        </div>
                        <div class="cb-mtch-all cb-nt-live">
                          <a
                            target="_self"
                            href="/live-cricket-scores/70445/rsaw-vs-ausw-3rd-t20i-australia-women-v-south-africa-women"
                            title="South Africa Women v Australia Women, 3rd T20I - AUSW Won"
                            ><span class="cb-mm-mtch-tm"
                              >South Africa Women vs Australia Women</span
                            ><span class="cb-mm-liv-tag"></span
                          ></a>
                          <div class="cb-mm-mtch-nm">3rd T20I</div>
                        </div>
                      </div>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
        <script>
          var matchId = "78628";
          var seriesId = "6927";
          PAGE_TARGETS["match"] = matchId;
          PAGE_TARGETS["series"] = seriesId;
          PAGE_TARGETS["team"] = [2, 9];
        </script>
        <div id="strip_wrapper" class="cb-col cb-col-100">
          <div id="large_strip" class="pull-left ad-unit"></div>
          <div id="small_strip" class="pull-right ad-unit"></div>
          <div id="super_strip" class="pull-left ad-unit"></div>
        </div>
        <div class="cb-col cb-col-100 cb-bg-white">
          <div
            class="cb-nav-main cb-col-100 cb-col cb-bg-white"
            itemscope
            itemtype="http://schema.org/SportsEvent"
          >
            <div class="cb-billing-plans-text cb-team-lft-item">
              <h1 class="cb-nav-hdr cb-font-18 line-ht24" itemprop="name">
                India vs England, 1st Test - Live Cricket Score, Commentary
              </h1>
            </div>
            <span
              itemprop="description"
              content="Follow India vs England, 1st Test, Jan 25, England tour of India, 2024 with live Cricket score, ball by ball commentary updates on Cricbuzz"
            ></span>
            <div class="cb-nav-subhdr cb-font-12">
              <span class="text-bold">Series: </span>
              <a
                href="/cricket-series/6927/england-tour-of-india-2024"
                title="England tour of India, 2024"
                ><span class="text-hvr-underline text-gray"
                  >England tour of India, 2024</span
                ></a
              >
              <span class="text-bold pad-left">Venue: </span
              ><a
                href="/cricket-series/6927/england-tour-of-india-2024/venues/80/rajiv-gandhi-international-stadium"
                title="Rajiv Gandhi International Stadium, Hyderabad"
                itemprop="location"
                itemscope
                itemtype="http://schema.org/Place"
                ><span class="text-hvr-underline text-gray"
                  ><span itemprop="name"
                    >Rajiv Gandhi International Stadium,&nbsp;</span
                  ><span
                    itemprop="address"
                    itemscope
                    itemtype="http://schema.org/PostalAddress"
                    ><span itemprop="addressLocality">Hyderabad</span></span
                  ></span
                ></a
              >
              <span class="text-bold pad-left">Date & Time: </span
              ><span itemprop="startDate" content="2024-01-25T04:00:00+00:00"
                ><span>Jan 25</span><span>-</span
                ><span>Jan 28</span>,&nbsp;<span>09:30 AM</span
                ><span>&nbsp;LOCAL</span
                ><span itemprop="endDate" content="2024-01-28"></span>
              </span>
            </div>
            <nav class="cb-nav-bar" role="navigation">
              <a
                class="cb-nav-tab"
                href="/live-cricket-scores/78628/ind-vs-eng-1st-test-england-tour-of-india-2024"
                title="India vs England, 1st Test Live Scores & Commentary"
                >Commentary</a
              >
              <a
                class="cb-nav-tab active"
                href="/live-cricket-scorecard/78628/ind-vs-eng-1st-test-england-tour-of-india-2024"
                title="India vs England, 1st Test Scorecard"
                >Scorecard</a
              >
              <a
                class="cb-nav-tab"
                href="/cricket-match-squads/78628/ind-vs-eng-1st-test-england-tour-of-india-2024"
                title="India vs England, 1st Test Squads"
                >Squads</a
              >
              <a
                class="cb-nav-tab"
                href="/cricket-match-highlights/78628/ind-vs-eng-1st-test-england-tour-of-india-2024"
                title="India vs England, 1st Test Highlights"
                target="_self"
                >Highlights</a
              >
              <a
                class="cb-nav-tab"
                href="/live-cricket-full-commentary/78628/ind-vs-eng-1st-test-england-tour-of-india-2024"
                title="India vs England, 1st Test Full Commentary"
              >
                Full Commentary</a
              >
              <a
                class="cb-nav-tab"
                href="/live-cricket-match-blog/78628/ind-vs-eng-1st-test-england-tour-of-india-2024"
                title="India vs England, 1st Test Live Blog"
                >Live Blog</a
              >
              <a
                class="cb-nav-tab"
                href="/cricket-match-facts/78628/ind-vs-eng-1st-test-england-tour-of-india-2024"
                title="India vs England, 1st Test Match Facts"
                >Match Facts</a
              >
              <a
                class="cb-nav-tab"
                href="/cricket-match-news/78628/ind-vs-eng-1st-test-england-tour-of-india-2024"
                title="India vs England, 1st Test News"
                >News</a
              >
              <a
                class="cb-nav-tab"
                href="/cricket-match-photos/78628/ind-vs-eng-1st-test-england-tour-of-india-2024"
                title="India vs England, 1st Test Photos"
                >Photos</a
              >
            </nav>
          </div>
          <div
            class="cb-col cb-col-67 cb-scrd-lft-col html-refresh"
            url="/api/html/cricket-scorecard/78628"
            timeout="30000"
            ng-init="seriesId='6927';"
          >
            <div class="cb-col cb-scrcrd-status cb-col-100 cb-text-complete">
              England won by 28 runs
            </div>
            <div id="innings_1">
              <div class="cb-col cb-col-100 cb-ltst-wgt-hdr">
                <div class="cb-col cb-col-100 cb-scrd-hdr-rw">
                  <span>England 1st Innings</span>
                  <span class="pull-right">246-10 (64.3 Ov)</span>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-sub-hdr cb-bg-gray">
                  <div class="cb-col cb-col-25 text-bold">Batter</div>
                  <div class="cb-col cb-col-33"></div>
                  <div class="cb-col cb-col-8 text-right text-bold">R</div>
                  <div class="cb-col cb-col-8 text-right">B</div>
                  <div class="cb-col cb-col-8 text-right">4s</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    6s
                  </div>
                  <div class="cb-col cb-col-8 text-right">SR</div>
                  <div class="cb-col cb-col-82 text-right"></div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/12770/zak-crawley"
                      title="View profile of Zak Crawley"
                      class="cb-text-link"
                    >
                      Zak Crawley
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">c Siraj b Ashwin</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">20</div>
                  <div class="cb-col cb-col-8 text-right">40</div>
                  <div class="cb-col cb-col-8 text-right">3</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    0
                  </div>
                  <div class="cb-col cb-col-8 text-right">50.00</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Zak Crawley"
                      href="/player-match-highlights/78628/1/12770/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/8502/duckett"
                      title="View profile of Duckett"
                      class="cb-text-link"
                    >
                      Duckett
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">lbw b Ashwin</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">35</div>
                  <div class="cb-col cb-col-8 text-right">39</div>
                  <div class="cb-col cb-col-8 text-right">7</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    0
                  </div>
                  <div class="cb-col cb-col-8 text-right">89.74</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Duckett"
                      href="/player-match-highlights/78628/1/8502/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/11691/ollie-pope"
                      title="View profile of Ollie Pope"
                      class="cb-text-link"
                    >
                      Ollie Pope
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">c Rohit b Ravindra Jadeja</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">1</div>
                  <div class="cb-col cb-col-8 text-right">11</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    0
                  </div>
                  <div class="cb-col cb-col-8 text-right">9.09</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Ollie Pope"
                      href="/player-match-highlights/78628/1/11691/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/8019/root"
                      title="View profile of Root"
                      class="cb-text-link"
                    >
                      Root
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">c Bumrah b Ravindra Jadeja</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">29</div>
                  <div class="cb-col cb-col-8 text-right">60</div>
                  <div class="cb-col cb-col-8 text-right">1</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    0
                  </div>
                  <div class="cb-col cb-col-8 text-right">48.33</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Root"
                      href="/player-match-highlights/78628/1/8019/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/6507/bairstow"
                      title="View profile of Bairstow"
                      class="cb-text-link"
                    >
                      Bairstow
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">b Axar</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">37</div>
                  <div class="cb-col cb-col-8 text-right">58</div>
                  <div class="cb-col cb-col-8 text-right">5</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    0
                  </div>
                  <div class="cb-col cb-col-8 text-right">63.79</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Bairstow"
                      href="/player-match-highlights/78628/1/6507/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/6557/stokes"
                      title="View profile of Stokes"
                      class="cb-text-link"
                    >
                      Stokes (c)
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">b Bumrah</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">70</div>
                  <div class="cb-col cb-col-8 text-right">88</div>
                  <div class="cb-col cb-col-8 text-right">6</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    3
                  </div>
                  <div class="cb-col cb-col-8 text-right">79.55</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Stokes"
                      href="/player-match-highlights/78628/1/6557/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/7859/foakes"
                      title="View profile of Foakes"
                      class="cb-text-link"
                    >
                      Foakes (wk)
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">c Srikar Bharat b Axar</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">4</div>
                  <div class="cb-col cb-col-8 text-right">24</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    0
                  </div>
                  <div class="cb-col cb-col-8 text-right">16.67</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Foakes"
                      href="/player-match-highlights/78628/1/7859/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/19767/rehan-ahmed"
                      title="View profile of Rehan Ahmed"
                      class="cb-text-link"
                    >
                      Rehan Ahmed
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">c Srikar Bharat b Bumrah</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">13</div>
                  <div class="cb-col cb-col-8 text-right">18</div>
                  <div class="cb-col cb-col-8 text-right">1</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    0
                  </div>
                  <div class="cb-col cb-col-8 text-right">72.22</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Rehan Ahmed"
                      href="/player-match-highlights/78628/1/19767/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/18199/tom-hartley"
                      title="View profile of Tom Hartley"
                      class="cb-text-link"
                    >
                      Tom Hartley
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">b Ravindra Jadeja</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">23</div>
                  <div class="cb-col cb-col-8 text-right">24</div>
                  <div class="cb-col cb-col-8 text-right">2</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    1
                  </div>
                  <div class="cb-col cb-col-8 text-right">95.83</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Tom Hartley"
                      href="/player-match-highlights/78628/1/18199/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/8383/mark-wood"
                      title="View profile of Mark Wood"
                      class="cb-text-link"
                    >
                      Mark Wood
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">b Ashwin</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">11</div>
                  <div class="cb-col cb-col-8 text-right">24</div>
                  <div class="cb-col cb-col-8 text-right">2</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    0
                  </div>
                  <div class="cb-col cb-col-8 text-right">45.83</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Mark Wood"
                      href="/player-match-highlights/78628/1/8383/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/8578/jack-leach"
                      title="View profile of Jack Leach"
                      class="cb-text-link"
                    >
                      Jack Leach
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">not out</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">0</div>
                  <div class="cb-col cb-col-8 text-right">3</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    0
                  </div>
                  <div class="cb-col cb-col-8 text-right">0.00</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Jack Leach"
                      href="/player-match-highlights/78628/1/8578/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-60">Extras</div>
                  <div
                    class="cb-col cb-col-8 text-bold cb-text-black text-right"
                  >
                    3
                  </div>
                  <div class="cb-col-32 cb-col">
                    &nbsp;(b 0, lb 1, w 0, nb 2, p 0)
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-60">Total</div>
                  <div class="cb-col cb-col-8 text-bold text-black text-right">
                    246
                  </div>
                  <div class="cb-col-32 cb-col">&nbsp;(10 wkts, 64.3 Ov)</div>
                </div>
              </div>
              <div
                class="cb-col cb-col-100 cb-scrd-sub-hdr cb-bg-gray text-bold"
              >
                Fall of Wickets
              </div>
              <div class="cb-col cb-col-100 cb-col-rt cb-font-13">
                <span
                  >55-1 (<a
                    href="/profiles/8502/duckett"
                    title="View profile of Duckett"
                    class="cb-text-link"
                    >Duckett</a
                  >, 11.5), </span
                ><span
                  >58-2 (<a
                    href="/profiles/11691/ollie-pope"
                    title="View profile of Ollie Pope"
                    class="cb-text-link"
                    >Ollie Pope</a
                  >, 14.4), </span
                ><span
                  >60-3 (<a
                    href="/profiles/12770/zak-crawley"
                    title="View profile of Zak Crawley"
                    class="cb-text-link"
                    >Zak Crawley</a
                  >, 15.1), </span
                ><span
                  >121-4 (<a
                    href="/profiles/6507/bairstow"
                    title="View profile of Bairstow"
                    class="cb-text-link"
                    >Bairstow</a
                  >, 32.4), </span
                ><span
                  >125-5 (<a
                    href="/profiles/8019/root"
                    title="View profile of Root"
                    class="cb-text-link"
                    >Root</a
                  >, 35.3), </span
                ><span
                  >137-6 (<a
                    href="/profiles/7859/foakes"
                    title="View profile of Foakes"
                    class="cb-text-link"
                    >Foakes</a
                  >, 42.5), </span
                ><span
                  >155-7 (<a
                    href="/profiles/19767/rehan-ahmed"
                    title="View profile of Rehan Ahmed"
                    class="cb-text-link"
                    >Rehan Ahmed</a
                  >, 48.3), </span
                ><span
                  >193-8 (<a
                    href="/profiles/18199/tom-hartley"
                    title="View profile of Tom Hartley"
                    class="cb-text-link"
                    >Tom Hartley</a
                  >, 54.6), </span
                ><span
                  >234-9 (<a
                    href="/profiles/8383/mark-wood"
                    title="View profile of Mark Wood"
                    class="cb-text-link"
                    >Mark Wood</a
                  >, 61.3), </span
                ><span
                  >246-10 (<a
                    href="/profiles/6557/stokes"
                    title="View profile of Stokes"
                    class="cb-text-link"
                    >Stokes</a
                  >, 64.3)</span
                >
              </div>
              <div class="cb-col cb-col-100 cb-ltst-wgt-hdr">
                <div class="cb-col cb-col-100 cb-scrd-sub-hdr cb-bg-gray">
                  <div class="cb-col cb-col-38 text-bold">Bowler</div>
                  <div class="cb-col cb-col-8 text-right">O</div>
                  <div class="cb-col cb-col-8 text-right">M</div>
                  <div class="cb-col cb-col-10 text-right">R</div>
                  <div class="cb-col cb-col-8 text-bold text-right">W</div>
                  <div class="cb-col cb-col-8 text-right">NB</div>
                  <div class="cb-col cb-col-8 text-right">WD</div>
                  <div class="cb-col cb-col-10 text-right">ECO</div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-38">
                    <a
                      href="/profiles/9311/bumrah"
                      title="View profile of Bumrah"
                      class="cb-text-link"
                    >
                      Bumrah
                    </a>
                  </div>
                  <div class="cb-col cb-col-8 text-right">8.3</div>
                  <div class="cb-col cb-col-8 text-right">1</div>
                  <div class="cb-col cb-col-10 text-right">28</div>
                  <div class="cb-col cb-col-8 text-right text-bold">2</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-10 text-right">3.30</div>
                  <div class="cb-col cb-col-2 text-right">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Bumrah"
                      href="/player-match-highlights/78628/1/9311/bowling"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-38">
                    <a
                      href="/profiles/10808/siraj"
                      title="View profile of Siraj"
                      class="cb-text-link"
                    >
                      Siraj
                    </a>
                  </div>
                  <div class="cb-col cb-col-8 text-right">4</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-10 text-right">28</div>
                  <div class="cb-col cb-col-8 text-right text-bold">0</div>
                  <div class="cb-col cb-col-8 text-right">1</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-10 text-right">7.00</div>
                  <div class="cb-col cb-col-2 text-right">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Siraj"
                      href="/player-match-highlights/78628/1/10808/bowling"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-38">
                    <a
                      href="/profiles/587/ravindra-jadeja"
                      title="View profile of Ravindra Jadeja"
                      class="cb-text-link"
                    >
                      Ravindra Jadeja
                    </a>
                  </div>
                  <div class="cb-col cb-col-8 text-right">18</div>
                  <div class="cb-col cb-col-8 text-right">4</div>
                  <div class="cb-col cb-col-10 text-right">88</div>
                  <div class="cb-col cb-col-8 text-right text-bold">3</div>
                  <div class="cb-col cb-col-8 text-right">1</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-10 text-right">4.90</div>
                  <div class="cb-col cb-col-2 text-right">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Ravindra Jadeja"
                      href="/player-match-highlights/78628/1/587/bowling"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-38">
                    <a
                      href="/profiles/1593/ashwin"
                      title="View profile of Ashwin"
                      class="cb-text-link"
                    >
                      Ashwin
                    </a>
                  </div>
                  <div class="cb-col cb-col-8 text-right">21</div>
                  <div class="cb-col cb-col-8 text-right">1</div>
                  <div class="cb-col cb-col-10 text-right">68</div>
                  <div class="cb-col cb-col-8 text-right text-bold">3</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-10 text-right">3.20</div>
                  <div class="cb-col cb-col-2 text-right">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Ashwin"
                      href="/player-match-highlights/78628/1/1593/bowling"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-38">
                    <a
                      href="/profiles/8808/axar"
                      title="View profile of Axar"
                      class="cb-text-link"
                    >
                      Axar
                    </a>
                  </div>
                  <div class="cb-col cb-col-8 text-right">13</div>
                  <div class="cb-col cb-col-8 text-right">1</div>
                  <div class="cb-col cb-col-10 text-right">33</div>
                  <div class="cb-col cb-col-8 text-right text-bold">2</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-10 text-right">2.50</div>
                  <div class="cb-col cb-col-2 text-right">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Axar"
                      href="/player-match-highlights/78628/1/8808/bowling"
                    ></a>
                  </div>
                </div>
              </div>
            </div>
            <div id="innings_2">
              <div class="cb-col cb-col-100 cb-ltst-wgt-hdr">
                <div class="cb-col cb-col-100 cb-scrd-hdr-rw">
                  <span>India 1st Innings</span>
                  <span class="pull-right">436-10 (121 Ov)</span>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-sub-hdr cb-bg-gray">
                  <div class="cb-col cb-col-25 text-bold">Batter</div>
                  <div class="cb-col cb-col-33"></div>
                  <div class="cb-col cb-col-8 text-right text-bold">R</div>
                  <div class="cb-col cb-col-8 text-right">B</div>
                  <div class="cb-col cb-col-8 text-right">4s</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    6s
                  </div>
                  <div class="cb-col cb-col-8 text-right">SR</div>
                  <div class="cb-col cb-col-82 text-right"></div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/13940/yashasvi-jaiswal"
                      title="View profile of Yashasvi Jaiswal"
                      class="cb-text-link"
                    >
                      Yashasvi Jaiswal
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">c and b Root</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">80</div>
                  <div class="cb-col cb-col-8 text-right">74</div>
                  <div class="cb-col cb-col-8 text-right">10</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    3
                  </div>
                  <div class="cb-col cb-col-8 text-right">108.11</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Yashasvi Jaiswal"
                      href="/player-match-highlights/78628/2/13940/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/576/rohit"
                      title="View profile of Rohit"
                      class="cb-text-link"
                    >
                      Rohit (c)
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">c Stokes b Jack Leach</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">24</div>
                  <div class="cb-col cb-col-8 text-right">27</div>
                  <div class="cb-col cb-col-8 text-right">3</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    0
                  </div>
                  <div class="cb-col cb-col-8 text-right">88.89</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Rohit"
                      href="/player-match-highlights/78628/2/576/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/11808/shubman-gill"
                      title="View profile of Shubman Gill"
                      class="cb-text-link"
                    >
                      Shubman Gill
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">c Duckett b Tom Hartley</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">23</div>
                  <div class="cb-col cb-col-8 text-right">66</div>
                  <div class="cb-col cb-col-8 text-right">2</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    0
                  </div>
                  <div class="cb-col cb-col-8 text-right">34.85</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Shubman Gill"
                      href="/player-match-highlights/78628/2/11808/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/8733/rahul"
                      title="View profile of Rahul"
                      class="cb-text-link"
                    >
                      Rahul
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">c Rehan Ahmed b Tom Hartley</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">86</div>
                  <div class="cb-col cb-col-8 text-right">123</div>
                  <div class="cb-col cb-col-8 text-right">8</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    2
                  </div>
                  <div class="cb-col cb-col-8 text-right">69.92</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Rahul"
                      href="/player-match-highlights/78628/2/8733/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/9428/shreyas-iyer"
                      title="View profile of Shreyas Iyer"
                      class="cb-text-link"
                    >
                      Shreyas Iyer
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">c Tom Hartley b Rehan Ahmed</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">35</div>
                  <div class="cb-col cb-col-8 text-right">63</div>
                  <div class="cb-col cb-col-8 text-right">3</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    1
                  </div>
                  <div class="cb-col cb-col-8 text-right">55.56</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Shreyas Iyer"
                      href="/player-match-highlights/78628/2/9428/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/587/ravindra-jadeja"
                      title="View profile of Ravindra Jadeja"
                      class="cb-text-link"
                    >
                      Ravindra Jadeja
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">lbw b Root</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">87</div>
                  <div class="cb-col cb-col-8 text-right">180</div>
                  <div class="cb-col cb-col-8 text-right">7</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    2
                  </div>
                  <div class="cb-col cb-col-8 text-right">48.33</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Ravindra Jadeja"
                      href="/player-match-highlights/78628/2/587/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/9025/srikar-bharat"
                      title="View profile of Srikar Bharat"
                      class="cb-text-link"
                    >
                      Srikar Bharat (wk)
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">lbw b Root</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">41</div>
                  <div class="cb-col cb-col-8 text-right">81</div>
                  <div class="cb-col cb-col-8 text-right">3</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    0
                  </div>
                  <div class="cb-col cb-col-8 text-right">50.62</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Srikar Bharat"
                      href="/player-match-highlights/78628/2/9025/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/1593/ashwin"
                      title="View profile of Ashwin"
                      class="cb-text-link"
                    >
                      Ashwin
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">run out (Tom Hartley/Foakes)</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">1</div>
                  <div class="cb-col cb-col-8 text-right">11</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    0
                  </div>
                  <div class="cb-col cb-col-8 text-right">9.09</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Ashwin"
                      href="/player-match-highlights/78628/2/1593/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/8808/axar"
                      title="View profile of Axar"
                      class="cb-text-link"
                    >
                      Axar
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">b Rehan Ahmed</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">44</div>
                  <div class="cb-col cb-col-8 text-right">100</div>
                  <div class="cb-col cb-col-8 text-right">7</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    1
                  </div>
                  <div class="cb-col cb-col-8 text-right">44.00</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Axar"
                      href="/player-match-highlights/78628/2/8808/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/9311/bumrah"
                      title="View profile of Bumrah"
                      class="cb-text-link"
                    >
                      Bumrah
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">b Root</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">0</div>
                  <div class="cb-col cb-col-8 text-right">1</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    0
                  </div>
                  <div class="cb-col cb-col-8 text-right">0.00</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Bumrah"
                      href="/player-match-highlights/78628/2/9311/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/10808/siraj"
                      title="View profile of Siraj"
                      class="cb-text-link"
                    >
                      Siraj
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">not out</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">0</div>
                  <div class="cb-col cb-col-8 text-right">2</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    0
                  </div>
                  <div class="cb-col cb-col-8 text-right">0.00</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Siraj"
                      href="/player-match-highlights/78628/2/10808/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-60">Extras</div>
                  <div
                    class="cb-col cb-col-8 text-bold cb-text-black text-right"
                  >
                    15
                  </div>
                  <div class="cb-col-32 cb-col">
                    &nbsp;(b 5, lb 6, w 2, nb 2, p 0)
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-60">Total</div>
                  <div class="cb-col cb-col-8 text-bold text-black text-right">
                    436
                  </div>
                  <div class="cb-col-32 cb-col">&nbsp;(10 wkts, 121 Ov)</div>
                </div>
              </div>
              <div
                class="cb-col cb-col-100 cb-scrd-sub-hdr cb-bg-gray text-bold"
              >
                Fall of Wickets
              </div>
              <div class="cb-col cb-col-100 cb-col-rt cb-font-13">
                <span
                  >80-1 (<a
                    href="/profiles/576/rohit"
                    title="View profile of Rohit"
                    class="cb-text-link"
                    >Rohit</a
                  >, 12.2), </span
                ><span
                  >123-2 (<a
                    href="/profiles/13940/yashasvi-jaiswal"
                    title="View profile of Yashasvi Jaiswal"
                    class="cb-text-link"
                    >Yashasvi Jaiswal</a
                  >, 23.4), </span
                ><span
                  >159-3 (<a
                    href="/profiles/11808/shubman-gill"
                    title="View profile of Shubman Gill"
                    class="cb-text-link"
                    >Shubman Gill</a
                  >, 34.5), </span
                ><span
                  >223-4 (<a
                    href="/profiles/9428/shreyas-iyer"
                    title="View profile of Shreyas Iyer"
                    class="cb-text-link"
                    >Shreyas Iyer</a
                  >, 52.3), </span
                ><span
                  >288-5 (<a
                    href="/profiles/8733/rahul"
                    title="View profile of Rahul"
                    class="cb-text-link"
                    >Rahul</a
                  >, 64.5), </span
                ><span
                  >356-6 (<a
                    href="/profiles/9025/srikar-bharat"
                    title="View profile of Srikar Bharat"
                    class="cb-text-link"
                    >Srikar Bharat</a
                  >, 88.2), </span
                ><span
                  >358-7 (<a
                    href="/profiles/1593/ashwin"
                    title="View profile of Ashwin"
                    class="cb-text-link"
                    >Ashwin</a
                  >, 90.3), </span
                ><span
                  >436-8 (<a
                    href="/profiles/587/ravindra-jadeja"
                    title="View profile of Ravindra Jadeja"
                    class="cb-text-link"
                    >Ravindra Jadeja</a
                  >, 119.3), </span
                ><span
                  >436-9 (<a
                    href="/profiles/9311/bumrah"
                    title="View profile of Bumrah"
                    class="cb-text-link"
                    >Bumrah</a
                  >, 119.4), </span
                ><span
                  >436-10 (<a
                    href="/profiles/8808/axar"
                    title="View profile of Axar"
                    class="cb-text-link"
                    >Axar</a
                  >, 120.6)</span
                >
              </div>
              <div class="cb-col cb-col-100 cb-ltst-wgt-hdr">
                <div class="cb-col cb-col-100 cb-scrd-sub-hdr cb-bg-gray">
                  <div class="cb-col cb-col-38 text-bold">Bowler</div>
                  <div class="cb-col cb-col-8 text-right">O</div>
                  <div class="cb-col cb-col-8 text-right">M</div>
                  <div class="cb-col cb-col-10 text-right">R</div>
                  <div class="cb-col cb-col-8 text-bold text-right">W</div>
                  <div class="cb-col cb-col-8 text-right">NB</div>
                  <div class="cb-col cb-col-8 text-right">WD</div>
                  <div class="cb-col cb-col-10 text-right">ECO</div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-38">
                    <a
                      href="/profiles/8383/mark-wood"
                      title="View profile of Mark Wood"
                      class="cb-text-link"
                    >
                      Mark Wood
                    </a>
                  </div>
                  <div class="cb-col cb-col-8 text-right">17</div>
                  <div class="cb-col cb-col-8 text-right">1</div>
                  <div class="cb-col cb-col-10 text-right">47</div>
                  <div class="cb-col cb-col-8 text-right text-bold">0</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-8 text-right">2</div>
                  <div class="cb-col cb-col-10 text-right">2.80</div>
                  <div class="cb-col cb-col-2 text-right">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Mark Wood"
                      href="/player-match-highlights/78628/2/8383/bowling"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-38">
                    <a
                      href="/profiles/18199/tom-hartley"
                      title="View profile of Tom Hartley"
                      class="cb-text-link"
                    >
                      Tom Hartley
                    </a>
                  </div>
                  <div class="cb-col cb-col-8 text-right">25</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-10 text-right">131</div>
                  <div class="cb-col cb-col-8 text-right text-bold">2</div>
                  <div class="cb-col cb-col-8 text-right">2</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-10 text-right">5.20</div>
                  <div class="cb-col cb-col-2 text-right">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Tom Hartley"
                      href="/player-match-highlights/78628/2/18199/bowling"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-38">
                    <a
                      href="/profiles/8578/jack-leach"
                      title="View profile of Jack Leach"
                      class="cb-text-link"
                    >
                      Jack Leach
                    </a>
                  </div>
                  <div class="cb-col cb-col-8 text-right">26</div>
                  <div class="cb-col cb-col-8 text-right">6</div>
                  <div class="cb-col cb-col-10 text-right">63</div>
                  <div class="cb-col cb-col-8 text-right text-bold">1</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-10 text-right">2.40</div>
                  <div class="cb-col cb-col-2 text-right">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Jack Leach"
                      href="/player-match-highlights/78628/2/8578/bowling"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-38">
                    <a
                      href="/profiles/19767/rehan-ahmed"
                      title="View profile of Rehan Ahmed"
                      class="cb-text-link"
                    >
                      Rehan Ahmed
                    </a>
                  </div>
                  <div class="cb-col cb-col-8 text-right">24</div>
                  <div class="cb-col cb-col-8 text-right">4</div>
                  <div class="cb-col cb-col-10 text-right">105</div>
                  <div class="cb-col cb-col-8 text-right text-bold">2</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-10 text-right">4.40</div>
                  <div class="cb-col cb-col-2 text-right">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Rehan Ahmed"
                      href="/player-match-highlights/78628/2/19767/bowling"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-38">
                    <a
                      href="/profiles/8019/root"
                      title="View profile of Root"
                      class="cb-text-link"
                    >
                      Root
                    </a>
                  </div>
                  <div class="cb-col cb-col-8 text-right">29</div>
                  <div class="cb-col cb-col-8 text-right">5</div>
                  <div class="cb-col cb-col-10 text-right">79</div>
                  <div class="cb-col cb-col-8 text-right text-bold">4</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-10 text-right">2.70</div>
                  <div class="cb-col cb-col-2 text-right">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Root"
                      href="/player-match-highlights/78628/2/8019/bowling"
                    ></a>
                  </div>
                </div>
              </div>
            </div>
            <div id="innings_3">
              <div class="cb-col cb-col-100 cb-ltst-wgt-hdr">
                <div class="cb-col cb-col-100 cb-scrd-hdr-rw">
                  <span>England 2nd Innings</span>
                  <span class="pull-right">420-10 (102.1 Ov)</span>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-sub-hdr cb-bg-gray">
                  <div class="cb-col cb-col-25 text-bold">Batter</div>
                  <div class="cb-col cb-col-33"></div>
                  <div class="cb-col cb-col-8 text-right text-bold">R</div>
                  <div class="cb-col cb-col-8 text-right">B</div>
                  <div class="cb-col cb-col-8 text-right">4s</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    6s
                  </div>
                  <div class="cb-col cb-col-8 text-right">SR</div>
                  <div class="cb-col cb-col-82 text-right"></div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/12770/zak-crawley"
                      title="View profile of Zak Crawley"
                      class="cb-text-link"
                    >
                      Zak Crawley
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">c Rohit b Ashwin</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">31</div>
                  <div class="cb-col cb-col-8 text-right">33</div>
                  <div class="cb-col cb-col-8 text-right">4</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    1
                  </div>
                  <div class="cb-col cb-col-8 text-right">93.94</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Zak Crawley"
                      href="/player-match-highlights/78628/3/12770/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/8502/duckett"
                      title="View profile of Duckett"
                      class="cb-text-link"
                    >
                      Duckett
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">b Bumrah</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">47</div>
                  <div class="cb-col cb-col-8 text-right">52</div>
                  <div class="cb-col cb-col-8 text-right">7</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    0
                  </div>
                  <div class="cb-col cb-col-8 text-right">90.38</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Duckett"
                      href="/player-match-highlights/78628/3/8502/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/11691/ollie-pope"
                      title="View profile of Ollie Pope"
                      class="cb-text-link"
                    >
                      Ollie Pope
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">b Bumrah</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">196</div>
                  <div class="cb-col cb-col-8 text-right">278</div>
                  <div class="cb-col cb-col-8 text-right">21</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    0
                  </div>
                  <div class="cb-col cb-col-8 text-right">70.50</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Ollie Pope"
                      href="/player-match-highlights/78628/3/11691/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/8019/root"
                      title="View profile of Root"
                      class="cb-text-link"
                    >
                      Root
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">lbw b Bumrah</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">2</div>
                  <div class="cb-col cb-col-8 text-right">6</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    0
                  </div>
                  <div class="cb-col cb-col-8 text-right">33.33</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Root"
                      href="/player-match-highlights/78628/3/8019/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/6507/bairstow"
                      title="View profile of Bairstow"
                      class="cb-text-link"
                    >
                      Bairstow
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">b Ravindra Jadeja</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">10</div>
                  <div class="cb-col cb-col-8 text-right">24</div>
                  <div class="cb-col cb-col-8 text-right">1</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    0
                  </div>
                  <div class="cb-col cb-col-8 text-right">41.67</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Bairstow"
                      href="/player-match-highlights/78628/3/6507/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/6557/stokes"
                      title="View profile of Stokes"
                      class="cb-text-link"
                    >
                      Stokes (c)
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">b Ashwin</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">6</div>
                  <div class="cb-col cb-col-8 text-right">33</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    0
                  </div>
                  <div class="cb-col cb-col-8 text-right">18.18</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Stokes"
                      href="/player-match-highlights/78628/3/6557/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/7859/foakes"
                      title="View profile of Foakes"
                      class="cb-text-link"
                    >
                      Foakes (wk)
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">b Axar</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">34</div>
                  <div class="cb-col cb-col-8 text-right">81</div>
                  <div class="cb-col cb-col-8 text-right">2</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    0
                  </div>
                  <div class="cb-col cb-col-8 text-right">41.98</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Foakes"
                      href="/player-match-highlights/78628/3/7859/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/19767/rehan-ahmed"
                      title="View profile of Rehan Ahmed"
                      class="cb-text-link"
                    >
                      Rehan Ahmed
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">c Srikar Bharat b Bumrah</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">28</div>
                  <div class="cb-col cb-col-8 text-right">53</div>
                  <div class="cb-col cb-col-8 text-right">3</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    0
                  </div>
                  <div class="cb-col cb-col-8 text-right">52.83</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Rehan Ahmed"
                      href="/player-match-highlights/78628/3/19767/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/18199/tom-hartley"
                      title="View profile of Tom Hartley"
                      class="cb-text-link"
                    >
                      Tom Hartley
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">b Ashwin</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">34</div>
                  <div class="cb-col cb-col-8 text-right">52</div>
                  <div class="cb-col cb-col-8 text-right">4</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    0
                  </div>
                  <div class="cb-col cb-col-8 text-right">65.38</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Tom Hartley"
                      href="/player-match-highlights/78628/3/18199/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/8383/mark-wood"
                      title="View profile of Mark Wood"
                      class="cb-text-link"
                    >
                      Mark Wood
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray"
                      >c Srikar Bharat b Ravindra Jadeja</span
                    >
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">0</div>
                  <div class="cb-col cb-col-8 text-right">7</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    0
                  </div>
                  <div class="cb-col cb-col-8 text-right">0.00</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Mark Wood"
                      href="/player-match-highlights/78628/3/8383/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/8578/jack-leach"
                      title="View profile of Jack Leach"
                      class="cb-text-link"
                    >
                      Jack Leach
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">not out</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">0</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    0
                  </div>
                  <div class="cb-col cb-col-8 text-right">0.00</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Jack Leach"
                      href="/player-match-highlights/78628/3/8578/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-60">Extras</div>
                  <div
                    class="cb-col cb-col-8 text-bold cb-text-black text-right"
                  >
                    32
                  </div>
                  <div class="cb-col-32 cb-col">
                    &nbsp;(b 20, lb 6, w 0, nb 6, p 0)
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-60">Total</div>
                  <div class="cb-col cb-col-8 text-bold text-black text-right">
                    420
                  </div>
                  <div class="cb-col-32 cb-col">&nbsp;(10 wkts, 102.1 Ov)</div>
                </div>
              </div>
              <div
                class="cb-col cb-col-100 cb-scrd-sub-hdr cb-bg-gray text-bold"
              >
                Fall of Wickets
              </div>
              <div class="cb-col cb-col-100 cb-col-rt cb-font-13">
                <span
                  >45-1 (<a
                    href="/profiles/12770/zak-crawley"
                    title="View profile of Zak Crawley"
                    class="cb-text-link"
                    >Zak Crawley</a
                  >, 9.2), </span
                ><span
                  >113-2 (<a
                    href="/profiles/8502/duckett"
                    title="View profile of Duckett"
                    class="cb-text-link"
                    >Duckett</a
                  >, 18.5), </span
                ><span
                  >117-3 (<a
                    href="/profiles/8019/root"
                    title="View profile of Root"
                    class="cb-text-link"
                    >Root</a
                  >, 20.6), </span
                ><span
                  >140-4 (<a
                    href="/profiles/6507/bairstow"
                    title="View profile of Bairstow"
                    class="cb-text-link"
                    >Bairstow</a
                  >, 27.4), </span
                ><span
                  >163-5 (<a
                    href="/profiles/6557/stokes"
                    title="View profile of Stokes"
                    class="cb-text-link"
                    >Stokes</a
                  >, 36.5), </span
                ><span
                  >275-6 (<a
                    href="/profiles/7859/foakes"
                    title="View profile of Foakes"
                    class="cb-text-link"
                    >Foakes</a
                  >, 66.6), </span
                ><span
                  >339-7 (<a
                    href="/profiles/19767/rehan-ahmed"
                    title="View profile of Rehan Ahmed"
                    class="cb-text-link"
                    >Rehan Ahmed</a
                  >, 82.3), </span
                ><span
                  >419-8 (<a
                    href="/profiles/18199/tom-hartley"
                    title="View profile of Tom Hartley"
                    class="cb-text-link"
                    >Tom Hartley</a
                  >, 100.1), </span
                ><span
                  >420-9 (<a
                    href="/profiles/8383/mark-wood"
                    title="View profile of Mark Wood"
                    class="cb-text-link"
                    >Mark Wood</a
                  >, 101.6), </span
                ><span
                  >420-10 (<a
                    href="/profiles/11691/ollie-pope"
                    title="View profile of Ollie Pope"
                    class="cb-text-link"
                    >Ollie Pope</a
                  >, 102.1)</span
                >
              </div>
              <div class="cb-col cb-col-100 cb-ltst-wgt-hdr">
                <div class="cb-col cb-col-100 cb-scrd-sub-hdr cb-bg-gray">
                  <div class="cb-col cb-col-38 text-bold">Bowler</div>
                  <div class="cb-col cb-col-8 text-right">O</div>
                  <div class="cb-col cb-col-8 text-right">M</div>
                  <div class="cb-col cb-col-10 text-right">R</div>
                  <div class="cb-col cb-col-8 text-bold text-right">W</div>
                  <div class="cb-col cb-col-8 text-right">NB</div>
                  <div class="cb-col cb-col-8 text-right">WD</div>
                  <div class="cb-col cb-col-10 text-right">ECO</div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-38">
                    <a
                      href="/profiles/9311/bumrah"
                      title="View profile of Bumrah"
                      class="cb-text-link"
                    >
                      Bumrah
                    </a>
                  </div>
                  <div class="cb-col cb-col-8 text-right">16.1</div>
                  <div class="cb-col cb-col-8 text-right">4</div>
                  <div class="cb-col cb-col-10 text-right">41</div>
                  <div class="cb-col cb-col-8 text-right text-bold">4</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-10 text-right">2.50</div>
                  <div class="cb-col cb-col-2 text-right">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Bumrah"
                      href="/player-match-highlights/78628/3/9311/bowling"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-38">
                    <a
                      href="/profiles/1593/ashwin"
                      title="View profile of Ashwin"
                      class="cb-text-link"
                    >
                      Ashwin
                    </a>
                  </div>
                  <div class="cb-col cb-col-8 text-right">29</div>
                  <div class="cb-col cb-col-8 text-right">4</div>
                  <div class="cb-col cb-col-10 text-right">126</div>
                  <div class="cb-col cb-col-8 text-right text-bold">3</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-10 text-right">4.30</div>
                  <div class="cb-col cb-col-2 text-right">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Ashwin"
                      href="/player-match-highlights/78628/3/1593/bowling"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-38">
                    <a
                      href="/profiles/8808/axar"
                      title="View profile of Axar"
                      class="cb-text-link"
                    >
                      Axar
                    </a>
                  </div>
                  <div class="cb-col cb-col-8 text-right">16</div>
                  <div class="cb-col cb-col-8 text-right">2</div>
                  <div class="cb-col cb-col-10 text-right">74</div>
                  <div class="cb-col cb-col-8 text-right text-bold">1</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-10 text-right">4.60</div>
                  <div class="cb-col cb-col-2 text-right">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Axar"
                      href="/player-match-highlights/78628/3/8808/bowling"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-38">
                    <a
                      href="/profiles/587/ravindra-jadeja"
                      title="View profile of Ravindra Jadeja"
                      class="cb-text-link"
                    >
                      Ravindra Jadeja
                    </a>
                  </div>
                  <div class="cb-col cb-col-8 text-right">34</div>
                  <div class="cb-col cb-col-8 text-right">1</div>
                  <div class="cb-col cb-col-10 text-right">131</div>
                  <div class="cb-col cb-col-8 text-right text-bold">2</div>
                  <div class="cb-col cb-col-8 text-right">6</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-10 text-right">3.90</div>
                  <div class="cb-col cb-col-2 text-right">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Ravindra Jadeja"
                      href="/player-match-highlights/78628/3/587/bowling"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-38">
                    <a
                      href="/profiles/10808/siraj"
                      title="View profile of Siraj"
                      class="cb-text-link"
                    >
                      Siraj
                    </a>
                  </div>
                  <div class="cb-col cb-col-8 text-right">7</div>
                  <div class="cb-col cb-col-8 text-right">1</div>
                  <div class="cb-col cb-col-10 text-right">22</div>
                  <div class="cb-col cb-col-8 text-right text-bold">0</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-10 text-right">3.10</div>
                  <div class="cb-col cb-col-2 text-right">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Siraj"
                      href="/player-match-highlights/78628/3/10808/bowling"
                    ></a>
                  </div>
                </div>
              </div>
            </div>
            <div id="innings_4">
              <div class="cb-col cb-col-100 cb-ltst-wgt-hdr">
                <div class="cb-col cb-col-100 cb-scrd-hdr-rw">
                  <span>India 2nd Innings</span>
                  <span class="pull-right">202-10 (69.2 Ov)</span>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-sub-hdr cb-bg-gray">
                  <div class="cb-col cb-col-25 text-bold">Batter</div>
                  <div class="cb-col cb-col-33"></div>
                  <div class="cb-col cb-col-8 text-right text-bold">R</div>
                  <div class="cb-col cb-col-8 text-right">B</div>
                  <div class="cb-col cb-col-8 text-right">4s</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    6s
                  </div>
                  <div class="cb-col cb-col-8 text-right">SR</div>
                  <div class="cb-col cb-col-82 text-right"></div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/576/rohit-sharma"
                      title="View profile of Rohit Sharma"
                      class="cb-text-link"
                    >
                      Rohit Sharma (c)
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">lbw b Tom Hartley</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">39</div>
                  <div class="cb-col cb-col-8 text-right">58</div>
                  <div class="cb-col cb-col-8 text-right">7</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    0
                  </div>
                  <div class="cb-col cb-col-8 text-right">67.24</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Rohit Sharma"
                      href="/player-match-highlights/78628/4/576/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/13940/yashasvi-jaiswal"
                      title="View profile of Yashasvi Jaiswal"
                      class="cb-text-link"
                    >
                      Yashasvi Jaiswal
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">c Ollie Pope b Tom Hartley</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">15</div>
                  <div class="cb-col cb-col-8 text-right">35</div>
                  <div class="cb-col cb-col-8 text-right">2</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    0
                  </div>
                  <div class="cb-col cb-col-8 text-right">42.86</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Yashasvi Jaiswal"
                      href="/player-match-highlights/78628/4/13940/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/11808/shubman-gill"
                      title="View profile of Shubman Gill"
                      class="cb-text-link"
                    >
                      Shubman Gill
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">c Ollie Pope b Tom Hartley</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">0</div>
                  <div class="cb-col cb-col-8 text-right">2</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    0
                  </div>
                  <div class="cb-col cb-col-8 text-right">0.00</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Shubman Gill"
                      href="/player-match-highlights/78628/4/11808/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/8733/kl-rahul"
                      title="View profile of KL Rahul"
                      class="cb-text-link"
                    >
                      KL Rahul
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">lbw b Root</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">22</div>
                  <div class="cb-col cb-col-8 text-right">48</div>
                  <div class="cb-col cb-col-8 text-right">3</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    0
                  </div>
                  <div class="cb-col cb-col-8 text-right">45.83</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of KL Rahul"
                      href="/player-match-highlights/78628/4/8733/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/8808/axar-patel"
                      title="View profile of Axar Patel"
                      class="cb-text-link"
                    >
                      Axar Patel
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">c and b Tom Hartley</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">17</div>
                  <div class="cb-col cb-col-8 text-right">42</div>
                  <div class="cb-col cb-col-8 text-right">3</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    0
                  </div>
                  <div class="cb-col cb-col-8 text-right">40.48</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Axar Patel"
                      href="/player-match-highlights/78628/4/8808/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/9428/shreyas-iyer"
                      title="View profile of Shreyas Iyer"
                      class="cb-text-link"
                    >
                      Shreyas Iyer
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">c Root b Jack Leach</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">13</div>
                  <div class="cb-col cb-col-8 text-right">31</div>
                  <div class="cb-col cb-col-8 text-right">1</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    0
                  </div>
                  <div class="cb-col cb-col-8 text-right">41.94</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Shreyas Iyer"
                      href="/player-match-highlights/78628/4/9428/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/587/ravindra-jadeja"
                      title="View profile of Ravindra Jadeja"
                      class="cb-text-link"
                    >
                      Ravindra Jadeja
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">run out (Stokes)</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">2</div>
                  <div class="cb-col cb-col-8 text-right">20</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    0
                  </div>
                  <div class="cb-col cb-col-8 text-right">10.00</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Ravindra Jadeja"
                      href="/player-match-highlights/78628/4/587/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/9025/srikar-bharat"
                      title="View profile of Srikar Bharat"
                      class="cb-text-link"
                    >
                      Srikar Bharat (wk)
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">b Tom Hartley</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">28</div>
                  <div class="cb-col cb-col-8 text-right">59</div>
                  <div class="cb-col cb-col-8 text-right">3</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    0
                  </div>
                  <div class="cb-col cb-col-8 text-right">47.46</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Srikar Bharat"
                      href="/player-match-highlights/78628/4/9025/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/1593/ravichandran-ashwin"
                      title="View profile of Ravichandran Ashwin"
                      class="cb-text-link"
                    >
                      Ravichandran Ashwin
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">st Foakes b Tom Hartley</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">28</div>
                  <div class="cb-col cb-col-8 text-right">84</div>
                  <div class="cb-col cb-col-8 text-right">2</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    0
                  </div>
                  <div class="cb-col cb-col-8 text-right">33.33</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Ravichandran Ashwin"
                      href="/player-match-highlights/78628/4/1593/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/9311/jasprit-bumrah"
                      title="View profile of Jasprit Bumrah"
                      class="cb-text-link"
                    >
                      Jasprit Bumrah
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">not out</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">6</div>
                  <div class="cb-col cb-col-8 text-right">18</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    0
                  </div>
                  <div class="cb-col cb-col-8 text-right">33.33</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Jasprit Bumrah"
                      href="/player-match-highlights/78628/4/9311/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-25">
                    <a
                      href="/profiles/10808/mohammed-siraj"
                      title="View profile of Mohammed Siraj"
                      class="cb-text-link"
                    >
                      Mohammed Siraj
                    </a>
                  </div>
                  <div class="cb-col cb-col-33">
                    <span class="text-gray">st Foakes b Tom Hartley</span>
                  </div>
                  <div class="cb-col cb-col-8 text-right text-bold">12</div>
                  <div class="cb-col cb-col-8 text-right">20</div>
                  <div class="cb-col cb-col-8 text-right">1</div>
                  <div
                    class="cb-col cb-col-8 text-right"
                    style="padding-right: 10px"
                  >
                    0
                  </div>
                  <div class="cb-col cb-col-8 text-right">60.00</div>
                  <div class="cb-col text-right cb-col-2">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Mohammed Siraj"
                      href="/player-match-highlights/78628/4/10808/batting"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-60">Extras</div>
                  <div
                    class="cb-col cb-col-8 text-bold cb-text-black text-right"
                  >
                    20
                  </div>
                  <div class="cb-col-32 cb-col">
                    &nbsp;(b 4, lb 14, w 1, nb 1, p 0)
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-60">Total</div>
                  <div class="cb-col cb-col-8 text-bold text-black text-right">
                    202
                  </div>
                  <div class="cb-col-32 cb-col">&nbsp;(10 wkts, 69.2 Ov)</div>
                </div>
              </div>
              <div
                class="cb-col cb-col-100 cb-scrd-sub-hdr cb-bg-gray text-bold"
              >
                Fall of Wickets
              </div>
              <div class="cb-col cb-col-100 cb-col-rt cb-font-13">
                <span
                  >42-1 (<a
                    href="/profiles/13940/yashasvi-jaiswal"
                    title="View profile of Yashasvi Jaiswal"
                    class="cb-text-link"
                    >Yashasvi Jaiswal</a
                  >, 11.4), </span
                ><span
                  >42-2 (<a
                    href="/profiles/11808/shubman-gill"
                    title="View profile of Shubman Gill"
                    class="cb-text-link"
                    >Shubman Gill</a
                  >, 11.6), </span
                ><span
                  >63-3 (<a
                    href="/profiles/576/rohit-sharma"
                    title="View profile of Rohit Sharma"
                    class="cb-text-link"
                    >Rohit Sharma</a
                  >, 17.5), </span
                ><span
                  >95-4 (<a
                    href="/profiles/8808/axar-patel"
                    title="View profile of Axar Patel"
                    class="cb-text-link"
                    >Axar Patel</a
                  >, 29.4), </span
                ><span
                  >107-5 (<a
                    href="/profiles/8733/kl-rahul"
                    title="View profile of KL Rahul"
                    class="cb-text-link"
                    >KL Rahul</a
                  >, 32.4), </span
                ><span
                  >119-6 (<a
                    href="/profiles/587/ravindra-jadeja"
                    title="View profile of Ravindra Jadeja"
                    class="cb-text-link"
                    >Ravindra Jadeja</a
                  >, 38.1), </span
                ><span
                  >119-7 (<a
                    href="/profiles/9428/shreyas-iyer"
                    title="View profile of Shreyas Iyer"
                    class="cb-text-link"
                    >Shreyas Iyer</a
                  >, 40.2), </span
                ><span
                  >176-8 (<a
                    href="/profiles/9025/srikar-bharat"
                    title="View profile of Srikar Bharat"
                    class="cb-text-link"
                    >Srikar Bharat</a
                  >, 61.6), </span
                ><span
                  >177-9 (<a
                    href="/profiles/1593/ravichandran-ashwin"
                    title="View profile of Ravichandran Ashwin"
                    class="cb-text-link"
                    >Ravichandran Ashwin</a
                  >, 63.2), </span
                ><span
                  >202-10 (<a
                    href="/profiles/10808/mohammed-siraj"
                    title="View profile of Mohammed Siraj"
                    class="cb-text-link"
                    >Mohammed Siraj</a
                  >, 69.2)</span
                >
              </div>
              <div class="cb-col cb-col-100 cb-ltst-wgt-hdr">
                <div class="cb-col cb-col-100 cb-scrd-sub-hdr cb-bg-gray">
                  <div class="cb-col cb-col-38 text-bold">Bowler</div>
                  <div class="cb-col cb-col-8 text-right">O</div>
                  <div class="cb-col cb-col-8 text-right">M</div>
                  <div class="cb-col cb-col-10 text-right">R</div>
                  <div class="cb-col cb-col-8 text-bold text-right">W</div>
                  <div class="cb-col cb-col-8 text-right">NB</div>
                  <div class="cb-col cb-col-8 text-right">WD</div>
                  <div class="cb-col cb-col-10 text-right">ECO</div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-38">
                    <a
                      href="/profiles/8019/joe-root"
                      title="View profile of Joe Root"
                      class="cb-text-link"
                    >
                      Joe Root
                    </a>
                  </div>
                  <div class="cb-col cb-col-8 text-right">19</div>
                  <div class="cb-col cb-col-8 text-right">3</div>
                  <div class="cb-col cb-col-10 text-right">41</div>
                  <div class="cb-col cb-col-8 text-right text-bold">1</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-10 text-right">2.20</div>
                  <div class="cb-col cb-col-2 text-right">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Joe Root"
                      href="/player-match-highlights/78628/4/8019/bowling"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-38">
                    <a
                      href="/profiles/8383/mark-wood"
                      title="View profile of Mark Wood"
                      class="cb-text-link"
                    >
                      Mark Wood
                    </a>
                  </div>
                  <div class="cb-col cb-col-8 text-right">8</div>
                  <div class="cb-col cb-col-8 text-right">1</div>
                  <div class="cb-col cb-col-10 text-right">15</div>
                  <div class="cb-col cb-col-8 text-right text-bold">0</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-10 text-right">1.90</div>
                  <div class="cb-col cb-col-2 text-right">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Mark Wood"
                      href="/player-match-highlights/78628/4/8383/bowling"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-38">
                    <a
                      href="/profiles/18199/tom-hartley"
                      title="View profile of Tom Hartley"
                      class="cb-text-link"
                    >
                      Tom Hartley
                    </a>
                  </div>
                  <div class="cb-col cb-col-8 text-right">26.2</div>
                  <div class="cb-col cb-col-8 text-right">5</div>
                  <div class="cb-col cb-col-10 text-right">62</div>
                  <div class="cb-col cb-col-8 text-right text-bold">7</div>
                  <div class="cb-col cb-col-8 text-right">1</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-10 text-right">2.40</div>
                  <div class="cb-col cb-col-2 text-right">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Tom Hartley"
                      href="/player-match-highlights/78628/4/18199/bowling"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-38">
                    <a
                      href="/profiles/8578/jack-leach"
                      title="View profile of Jack Leach"
                      class="cb-text-link"
                    >
                      Jack Leach
                    </a>
                  </div>
                  <div class="cb-col cb-col-8 text-right">10</div>
                  <div class="cb-col cb-col-8 text-right">1</div>
                  <div class="cb-col cb-col-10 text-right">33</div>
                  <div class="cb-col cb-col-8 text-right text-bold">1</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-8 text-right">1</div>
                  <div class="cb-col cb-col-10 text-right">3.30</div>
                  <div class="cb-col cb-col-2 text-right">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Jack Leach"
                      href="/player-match-highlights/78628/4/8578/bowling"
                    ></a>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-scrd-itms">
                  <div class="cb-col cb-col-38">
                    <a
                      href="/profiles/19767/rehan-ahmed"
                      title="View profile of Rehan Ahmed"
                      class="cb-text-link"
                    >
                      Rehan Ahmed
                    </a>
                  </div>
                  <div class="cb-col cb-col-8 text-right">6</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-10 text-right">33</div>
                  <div class="cb-col cb-col-8 text-right text-bold">0</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-8 text-right">0</div>
                  <div class="cb-col cb-col-10 text-right">5.50</div>
                  <div class="cb-col cb-col-2 text-right">
                    <a
                      class="cb-ico cb-caret-right"
                      title="view Highlights of Rehan Ahmed"
                      href="/player-match-highlights/78628/4/19767/bowling"
                    ></a>
                  </div>
                </div>
              </div>
            </div>
            <div class="cb-col cb-col-100">
              <div class="cb-col cb-col-100 cb-scrd-hdr-rw">Match Info</div>
              <div class="cb-col cb-col-100 cb-font-13">
                <div class="cb-col cb-col-100 cb-mtch-info-itm">
                  <div class="cb-col cb-col-27">Match</div>
                  <div class="cb-col cb-col-73">
                    IND vs ENG, 1st Test, England tour of India, 2024
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-mtch-info-itm">
                  <div class="cb-col cb-col-27">Date</div>
                  <div class="cb-col cb-col-73">
                    <span
                      class="schedule-date"
                      timestamp="1706155200000"
                      venue="+05:30"
                      format="EEEE, MMMM dd, yyyy"
                    ></span>
                    <span>- </span
                    ><span
                      class="schedule-date"
                      timestamp="1706443279000"
                      venue="+05:30"
                      format="EEEE, MMMM dd, yyyy"
                    ></span>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-mtch-info-itm">
                  <div class="cb-col cb-col-27">Toss</div>
                  <div class="cb-col cb-col-73">
                    England won the toss and opt to bat
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-mtch-info-itm">
                  <div class="cb-col cb-col-27">Time</div>
                  <div class="cb-col cb-col-73">
                    <span
                      class="schedule-date"
                      timestamp="1706155200000"
                      venue="+05:30"
                      format="h:mm a"
                    ></span>
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-mtch-info-itm">
                  <div class="cb-col cb-col-27">Venue</div>
                  <div class="cb-col cb-col-73">
                    Rajiv Gandhi International Stadium, Hyderabad
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-mtch-info-itm">
                  <div class="cb-col cb-col-27">Umpires</div>
                  <div class="cb-col cb-col-73">
                    Chris Gaffaney, Paul Reiffel
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-mtch-info-itm">
                  <div class="cb-col cb-col-27">Third Umpire</div>
                  <div class="cb-col cb-col-73">Marais Erasmus</div>
                </div>
                <div class="cb-col cb-col-100 cb-mtch-info-itm">
                  <div class="cb-col cb-col-27">Match Referee</div>
                  <div class="cb-col cb-col-73">Richie Richardson</div>
                </div>
                <div class="cb-col cb-col-100 cb-minfo-tm-nm">
                  India&nbsp;Squad
                </div>
                <div class="cb-col cb-col-100 cb-minfo-tm-nm">
                  <div class="cb-col cb-col-27">Playing</div>
                  <div class="cb-col cb-col-73">
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/576/rohit-sharma"
                      title="View profile of Rohit Sharma"
                      >Rohit Sharma (c)</a
                    >,
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/13940/yashasvi-jaiswal"
                      title="View profile of Yashasvi Jaiswal"
                      >Yashasvi Jaiswal</a
                    >,
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/11808/shubman-gill"
                      title="View profile of Shubman Gill"
                      >Shubman Gill</a
                    >,
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/8733/kl-rahul"
                      title="View profile of KL Rahul"
                      >KL Rahul</a
                    >,
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/9428/shreyas-iyer"
                      title="View profile of Shreyas Iyer"
                      >Shreyas Iyer</a
                    >,
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/587/ravindra-jadeja"
                      title="View profile of Ravindra Jadeja"
                      >Ravindra Jadeja</a
                    >,
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/9025/srikar-bharat"
                      title="View profile of Srikar Bharat"
                      >Srikar Bharat (wk)</a
                    >,
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/1593/ravichandran-ashwin"
                      title="View profile of Ravichandran Ashwin"
                      >Ravichandran Ashwin</a
                    >,
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/8808/axar-patel"
                      title="View profile of Axar Patel"
                      >Axar Patel</a
                    >,
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/9311/jasprit-bumrah"
                      title="View profile of Jasprit Bumrah"
                      >Jasprit Bumrah</a
                    >,
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/10808/mohammed-siraj"
                      title="View profile of Mohammed Siraj"
                      >Mohammed Siraj</a
                    >
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-minfo-tm-nm">
                  <div class="cb-col cb-col-27">Bench</div>
                  <div class="cb-col cb-col-73">
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/10636/rajat-patidar"
                      title="View profile of Rajat Patidar"
                      >Rajat Patidar</a
                    >,
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/10754/mukesh-kumar"
                      title="View profile of Mukesh Kumar"
                      >Mukesh Kumar</a
                    >,
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/14691/dhruv-jurel"
                      title="View profile of Dhruv Jurel"
                      >Dhruv Jurel</a
                    >,
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/8292/kuldeep-yadav"
                      title="View profile of Kuldeep Yadav"
                      >Kuldeep Yadav</a
                    >
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-minfo-tm-nm">
                  <div class="cb-col cb-col-27">Support Staff</div>
                  <div class="cb-col cb-col-73">
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/27/rahul-dravid"
                      title="View profile of Rahul Dravid"
                      >Rahul Dravid</a
                    >,
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/3909/vikram-rathour"
                      title="View profile of Vikram Rathour"
                      >Vikram Rathour</a
                    >,
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/3910/paras-mhambrey"
                      title="View profile of Paras Mhambrey"
                      >Paras Mhambrey</a
                    >
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-minfo-tm-nm cb-minfo-tm2-nm">
                  England&nbsp;Squad
                </div>
                <div class="cb-col cb-col-100 cb-minfo-tm-nm">
                  <div class="cb-col cb-col-27">Playing</div>
                  <div class="cb-col cb-col-73">
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/12770/zak-crawley"
                      title="View profile of Zak Crawley"
                      >Zak Crawley</a
                    >,
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/8502/ben-duckett"
                      title="View profile of Ben Duckett"
                      >Ben Duckett</a
                    >,
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/11691/ollie-pope"
                      title="View profile of Ollie Pope"
                      >Ollie Pope</a
                    >,
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/8019/joe-root"
                      title="View profile of Joe Root"
                      >Joe Root</a
                    >,
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/6507/jonny-bairstow"
                      title="View profile of Jonny Bairstow"
                      >Jonny Bairstow</a
                    >,
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/6557/ben-stokes"
                      title="View profile of Ben Stokes"
                      >Ben Stokes (c)</a
                    >,
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/7859/ben-foakes"
                      title="View profile of Ben Foakes"
                      >Ben Foakes (wk)</a
                    >,
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/19767/rehan-ahmed"
                      title="View profile of Rehan Ahmed"
                      >Rehan Ahmed</a
                    >,
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/18199/tom-hartley"
                      title="View profile of Tom Hartley"
                      >Tom Hartley</a
                    >,
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/8383/mark-wood"
                      title="View profile of Mark Wood"
                      >Mark Wood</a
                    >,
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/8578/jack-leach"
                      title="View profile of Jack Leach"
                      >Jack Leach</a
                    >
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-minfo-tm-nm">
                  <div class="cb-col cb-col-27">Bench</div>
                  <div class="cb-col cb-col-73">
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/9531/ollie-robinson"
                      title="View profile of Ollie Robinson"
                      >Ollie Robinson</a
                    >,
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/65/james-anderson"
                      title="View profile of James Anderson"
                      >James Anderson</a
                    >,
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/10385/daniel-lawrence"
                      title="View profile of Daniel Lawrence"
                      >Daniel Lawrence</a
                    >,
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/13681/gus-atkinson"
                      title="View profile of Gus Atkinson"
                      >Gus Atkinson</a
                    >
                  </div>
                </div>
                <div class="cb-col cb-col-100 cb-minfo-tm-nm">
                  <div class="cb-col cb-col-27">Support Staff</div>
                  <div class="cb-col cb-col-73">
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/201/brendon-mccullum"
                      title="View profile of Brendon McCullum"
                      >Brendon McCullum</a
                    >,
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/66/paul-collingwood"
                      title="View profile of Paul Collingwood"
                      >Paul Collingwood</a
                    >,
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/44/marcus-trescothick"
                      title="View profile of Marcus Trescothick"
                      >Marcus Trescothick</a
                    >,
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/435/jeetan-patel"
                      title="View profile of Jeetan Patel"
                      >Jeetan Patel</a
                    >,
                    <a
                      class="margin0 text-black text-hvr-underline"
                      href="/profiles/6554/neil-killeen"
                      title="View profile of Neil Killeen"
                      >Neil Killeen</a
                    >
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="cb-col cb-col-33 cb-col-rt">
            <div
              id="mpu"
              class="ad-unit cb-col cb-col-100"
              style="min-height: 250px"
            ></div>
            <div id="mpu2" class="ad-unit cb-col cb-nav-hdr"></div>
            <div
              class="cb-col cb-col-100 cb-sr-hist-pad"
              id="latest-news-mod"
              gtm-label="scorecard"
            >
              <h4 class="cb-ltst-hdr">LATEST NEWS</h4>
              <div
                class="cb-col cb-col-100 cb-lst-itm cb-pos-rel cb-lst-itm-sm"
              >
                <div
                  class="cb-col cb-col-33 cb-pos-rel"
                  itemscope
                  itemtype="https://schema.org/ImageObject"
                  itemprop="image"
                >
                  <meta itemprop="width" content="100" />
                  <meta itemprop="height" content="77" />
                  <meta
                    itemprop="url"
                    content="https:https://static.cricbuzz.com/a/img/v1/100x77/i1/c376495/mayank-is-expected-to-return-t.jpg"
                  /><a
                    target="_self"
                    href="/cricket-news/129320/mayank-agarwal-hospitalized-in-agartala-after-falling-sick-on-flight"
                    title="Mayank Agarwal hospitalized in Agartala after falling sick on flight"
                    ><img
                      height="77"
                      width="100"
                      alt="Mayank is expected to return to Bengaluru once he&#39;s discharged from an Agartala hospital"
                      title="Mayank is expected to return to Bengaluru once he&#39;s discharged from an Agartala hospital"
                      itemprop="image"
                      class="cb-lst-img lazy-loading"
                      source="https://static.cricbuzz.com/a/img/v1/100x77/i1/c376495/mayank-is-expected-to-return-t.jpg"
                      style="padding: 0px"
                  /></a>
                </div>
                <div
                  class="cb-col-67 cb-nws-lst-rt cb-col cb-col-text-container"
                >
                  <div class="cb-ltst-wgt-hdr">
                    <a
                      target="_self"
                      class="cb-nws-hdln-ancr text-hvr-underline"
                      href="/cricket-news/129320/mayank-agarwal-hospitalized-in-agartala-after-falling-sick-on-flight"
                      title="Mayank Agarwal hospitalized in Agartala after falling sick on flight"
                      >Mayank Agarwal hospitalized in Agartala after falling
                      sick on flight</a
                    >
                  </div>
                  <div><span class="cb-nws-time">23m ago</span></div>
                </div>
              </div>
              <span
                id="native_latest_news"
                class="ad-native ng-cloak"
                ng-if='!$root.$GEO.isGeo("EU")'
                ad-loaded="false"
                ad-content='<div class="cb-col cb-col-100 cb-lst-itm cb-lst-itm-sm" style="border-bottom: 1px solid #ecebeb"><div class="cb-col cb-col-33"><a rel="noreferrer" target="_blank" href="[[clk]]"><img style="width:90px;height:70px;" src="[[img]]" ></a></div><div class="cb-col-67 cb-nws-lst-rt cb-col cb-col-text-container"><a rel="nofollow" target="_blank" href="[[clk]]" class="cb-nws-hdln-ancr text-hvr-underline"><div class="cb-list-intro-text" style="height: 66px; overflow: hidden;">[[text]]</div><div class="cb-list-sub-text ad-native-sponsor">[[sponsor]]<img src="[[logo]]" class="pull-right" style="height:14px;" /></div></a><div style="float:right;margin-top:-85px;"><a rel="noreferrer" target="_blank" href="[[adchoicesClickURL]]"><img src="[[adchoicesImgURL]]"/></a></div></div></div>'
              ></span>
              <div
                class="cb-col cb-col-100 cb-lst-itm cb-pos-rel cb-lst-itm-sm"
              >
                <div
                  class="cb-col cb-col-33 cb-pos-rel"
                  itemscope
                  itemtype="https://schema.org/ImageObject"
                  itemprop="image"
                >
                  <meta itemprop="width" content="100" />
                  <meta itemprop="height" content="77" />
                  <meta
                    itemprop="url"
                    content="https:https://static.cricbuzz.com/a/img/v1/100x77/i1/c376435/dean-elgar-alleges-virat-kohli.jpg"
                  /><a
                    target="_self"
                    href="/cricket-news/129319/elgar-and-kohli-washed-away-2015-spitting-spat-with-drinks"
                    title="Elgar and Kohli washed away 2015 spitting spat with drinks"
                    ><img
                      height="77"
                      width="100"
                      alt="Dean Elgar alleges Virat Kohli spat at him during South Africa&#39;s Test series in India in November 2015"
                      title="Dean Elgar alleges Virat Kohli spat at him during South Africa&#39;s Test series in India in November 2015"
                      itemprop="image"
                      class="cb-lst-img lazy-loading"
                      source="https://static.cricbuzz.com/a/img/v1/100x77/i1/c376435/dean-elgar-alleges-virat-kohli.jpg"
                      style="padding: 0px"
                  /></a>
                </div>
                <div
                  class="cb-col-67 cb-nws-lst-rt cb-col cb-col-text-container"
                >
                  <div class="cb-ltst-wgt-hdr">
                    <a
                      target="_self"
                      class="cb-nws-hdln-ancr text-hvr-underline"
                      href="/cricket-news/129319/elgar-and-kohli-washed-away-2015-spitting-spat-with-drinks"
                      title="Elgar and Kohli washed away 2015 spitting spat with drinks"
                      >Elgar and Kohli washed away 2015 spitting spat with
                      drinks</a
                    >
                  </div>
                  <div><span class="cb-nws-time">4h ago</span></div>
                </div>
              </div>
              <div
                class="cb-col cb-col-100 cb-lst-itm cb-pos-rel cb-lst-itm-sm"
              >
                <div
                  class="cb-col cb-col-33 cb-pos-rel"
                  itemscope
                  itemtype="https://schema.org/ImageObject"
                  itemprop="image"
                >
                  <meta itemprop="width" content="100" />
                  <meta itemprop="height" content="77" />
                  <meta
                    itemprop="url"
                    content="https:https://static.cricbuzz.com/a/img/v1/100x77/i1/c376488/romario-and-shamar-though-fiv.jpg"
                  /><a
                    target="_self"
                    href="/cricket-news/129318/from-childhood-buddies-to-cricket-stars-the-romario-shamar-story"
                    title="From childhood buddies to cricket stars: The Romario-Shamar story"
                    ><img
                      height="77"
                      width="100"
                      alt="Romario and Shamar, though five years apart in age, have been lifelong buddies and neighbours"
                      title="Romario and Shamar, though five years apart in age, have been lifelong buddies and neighbours"
                      itemprop="image"
                      class="cb-lst-img lazy-loading"
                      source="https://static.cricbuzz.com/a/img/v1/100x77/i1/c376488/romario-and-shamar-though-fiv.jpg"
                      style="padding: 0px"
                  /></a>
                </div>
                <div
                  class="cb-col-67 cb-nws-lst-rt cb-col cb-col-text-container"
                >
                  <div class="cb-ltst-wgt-hdr">
                    <a
                      target="_self"
                      class="cb-nws-hdln-ancr text-hvr-underline"
                      href="/cricket-news/129318/from-childhood-buddies-to-cricket-stars-the-romario-shamar-story"
                      title="From childhood buddies to cricket stars: The Romario-Shamar story"
                      >From childhood buddies to cricket stars: The
                      Romario-Shamar story</a
                    >
                  </div>
                  <div><span class="cb-nws-time">4h ago</span></div>
                </div>
              </div>
              <div
                class="cb-col cb-col-100 cb-lst-itm cb-pos-rel cb-lst-itm-sm"
              >
                <div
                  class="cb-col cb-col-33 cb-pos-rel"
                  itemscope
                  itemtype="https://schema.org/ImageObject"
                  itemprop="image"
                >
                  <meta itemprop="width" content="100" />
                  <meta itemprop="height" content="77" />
                  <meta
                    itemprop="url"
                    content="https:https://static.cricbuzz.com/a/img/v1/100x77/i1/c376430/up-beat-mumbai-by-2-wickets.jpg"
                  /><a
                    target="_self"
                    href="/cricket-news/129317/how-karan-sharma-defied-pain-and-adversity-against-mumbai"
                    title="How Karan Sharma defied pain and adversity against Mumbai"
                    ><img
                      height="77"
                      width="100"
                      alt="UP beat Mumbai by 2 wickets"
                      title="UP beat Mumbai by 2 wickets"
                      itemprop="image"
                      class="cb-lst-img lazy-loading"
                      source="https://static.cricbuzz.com/a/img/v1/100x77/i1/c376430/up-beat-mumbai-by-2-wickets.jpg"
                      style="padding: 0px"
                  /></a>
                </div>
                <div
                  class="cb-col-67 cb-nws-lst-rt cb-col cb-col-text-container"
                >
                  <div class="cb-ltst-wgt-hdr">
                    <a
                      target="_self"
                      class="cb-nws-hdln-ancr text-hvr-underline"
                      href="/cricket-news/129317/how-karan-sharma-defied-pain-and-adversity-against-mumbai"
                      title="How Karan Sharma defied pain and adversity against Mumbai"
                      >How Karan Sharma defied pain and adversity against
                      Mumbai</a
                    >
                  </div>
                  <div><span class="cb-nws-time">13h ago</span></div>
                </div>
              </div>
              <div
                class="cb-col cb-col-100 cb-lst-itm cb-pos-rel cb-lst-itm-sm"
              >
                <div
                  class="cb-col cb-col-33 cb-pos-rel"
                  itemscope
                  itemtype="https://schema.org/ImageObject"
                  itemprop="image"
                >
                  <meta itemprop="width" content="100" />
                  <meta itemprop="height" content="77" />
                  <meta
                    itemprop="url"
                    content="https:https://static.cricbuzz.com/a/img/v1/100x77/i1/c376429/faf-du-plessis-smashed-a-20-ba.jpg"
                  /><a
                    target="_self"
                    href="/cricket-news/129316/faf-du-plessis-finds-form-as-joburg-super-kings-hammer-mi-cape-town"
                    title="Du Plessis finds form as Super Kings hammer MI"
                    ><img
                      height="77"
                      width="100"
                      alt="Faf du Plessis smashed a 20-ball fifty"
                      title="Faf du Plessis smashed a 20-ball fifty"
                      itemprop="image"
                      class="cb-lst-img lazy-loading"
                      source="https://static.cricbuzz.com/a/img/v1/100x77/i1/c376429/faf-du-plessis-smashed-a-20-ba.jpg"
                      style="padding: 0px"
                  /></a>
                </div>
                <div
                  class="cb-col-67 cb-nws-lst-rt cb-col cb-col-text-container"
                >
                  <div class="cb-ltst-wgt-hdr">
                    <a
                      target="_self"
                      class="cb-nws-hdln-ancr text-hvr-underline"
                      href="/cricket-news/129316/faf-du-plessis-finds-form-as-joburg-super-kings-hammer-mi-cape-town"
                      title="Du Plessis finds form as Super Kings hammer MI"
                      >Du Plessis finds form as Super Kings hammer MI</a
                    >
                  </div>
                  <div><span class="cb-nws-time">13h ago</span></div>
                </div>
              </div>
              <div
                class="cb-col cb-col-100 cb-lst-itm cb-pos-rel cb-lst-itm-sm"
              >
                <div
                  class="cb-col cb-col-33 cb-pos-rel"
                  itemscope
                  itemtype="https://schema.org/ImageObject"
                  itemprop="image"
                >
                  <meta itemprop="width" content="100" />
                  <meta itemprop="height" content="77" />
                  <meta
                    itemprop="url"
                    content="https:https://static.cricbuzz.com/a/img/v1/100x77/i1/c376428/gous-moved-to-america-in-2021.jpg"
                  /><a
                    target="_self"
                    href="/cricket-news/129315/no-regrets-of-moving-to-america-andries-gous"
                    title="No regrets of moving to America: Andries Gous"
                    ><img
                      height="77"
                      width="100"
                      alt="Gous moved to America in 2021 with an MLC contract after 60 first class caps in South Africa.."
                      title="Gous moved to America in 2021 with an MLC contract after 60 first class caps in South Africa.."
                      itemprop="image"
                      class="cb-lst-img lazy-loading"
                      source="https://static.cricbuzz.com/a/img/v1/100x77/i1/c376428/gous-moved-to-america-in-2021.jpg"
                      style="padding: 0px"
                  /></a>
                </div>
                <div
                  class="cb-col-67 cb-nws-lst-rt cb-col cb-col-text-container"
                >
                  <div class="cb-ltst-wgt-hdr">
                    <a
                      target="_self"
                      class="cb-nws-hdln-ancr text-hvr-underline"
                      href="/cricket-news/129315/no-regrets-of-moving-to-america-andries-gous"
                      title="No regrets of moving to America: Andries Gous"
                      >No regrets of moving to America: Andries Gous</a
                    >
                  </div>
                  <div><span class="cb-nws-time">14h ago</span></div>
                </div>
              </div>
              <div class="cb-col cb-col-100 cb-more-btn-cntnr">
                <a
                  target="_self"
                  title="Click to view more News"
                  href="/cricket-news"
                  class="cb-more-btn"
                  role="button"
                  >More News</a
                >
              </div>
            </div>
            <style>
              .cb-topic-header {
                margin-left: 0px !important;
              }
              .cb-list-heading {
                font-weight: normal !important;
              }
            </style>
            <div id="mpu3" class="ad-unit cb-col"></div>
          </div>
        </div>
        <style>
          .kaltura-play {
            display: none;
          }
        </style>
        <script>
          var is_video_enabled = false;
          CBQueueOnLoad.push(function () {
            var is_video_enabled = _GEO.country == "US" || _GEO.country == "CA";
            if (is_video_enabled) {
              _ele("body").append(
                "<style>.kaltura-play{display:inline-block;}</style>"
              );
            }
          });
        </script>
        <span
          id="skin_right"
          class="ad-unit"
          style="
            overflow: hidden;
            position: fixed;
            top: 0;
            left: calc(50% + 490px);
            margin-left: 3px;
            z-index: -99;
          "
        ></span>
        <div
          id="cb-plus-logout-msg"
          ng-controller="CBPlusAuth"
          class="disp-none"
        ></div>
      </div>
    </div>
    <div ng-cloak ng-if='$root.$GEO.isGeo("EU")'>
      <div
        class="feedback-bar text-center cb-col-100 disp-none feedback-menu"
        id="feedback-bar"
        ng-controller="FeedbackCtrl"
        ng-init="show_feedback_menu();"
      >
        <span class="feedback-txt"
          >We use cookies to improve your experience on our site and to show you
          non-personalized ads. Find out more in our
          <a style="color: #4a90e2" href="/info/privacy">privacy policy</a> and
          <a style="color: #4a90e2" href="/info/privacy#cookie_policy"
            >cookie policy</a
          ></span
        ><button
          class="cb-feedback-btn blue-btn cb-cursor"
          id="close_feedback_btn"
          ng-click="close_feedback();"
        >
          OK
        </button>
      </div>
    </div>
    <footer id="FooterWraper" itemscope itemtype="http://schema.org/WPFooter">
      <div class="cb-footer cb-col-100 cb-col">
        <div class="cb-ftr-cntnr">
          <div class="cb-col-25 cb-col">
            <a href="/" target="_self" class="cb-hm-text"
              ><img
                id="cb-logo-main-menu"
                itemprop="image"
                height="40"
                width="101"
                alt="Cricbuzz Logo"
                title="Cricbuzz Logo"
                src="https://static.cricbuzz.com/images/cb_logo.svg"
            /></a>
          </div>
          <div class="cb-col-25 cb-col">
            <div class="text-left cb-font-16 text-bold">MOBILE SITE & APPS</div>
            <ul class="cb-ftr-ul">
              <li class="cb-ftr-lst">
                <a href="https://m.cricbuzz.com" class="text-white"
                  ><span class="cb-mobile-site cb-ico"></span
                  ><span class="cb-footer-list-rt">m.cricbuzz.com</span></a
                >
              </li>
              <li class="cb-ftr-lst">
                <a
                  class="text-white"
                  href="https://play.google.com/store/apps/details?id=com.cricbuzz.android"
                  target="_blank"
                  rel="noopener noreferrer"
                  ><span class="cb-app-android cb-ico"></span
                  ><span class="cb-footer-list-rt">Android</span></a
                >
              </li>
              <li class="cb-ftr-lst">
                <a
                  class="text-white"
                  href="https://itunes.apple.com/app/id360466413"
                  target="_blank"
                  rel="noopener noreferrer"
                  ><span class="cb-app-ios cb-ico"></span
                  ><span class="cb-footer-list-rt">iOS</span></a
                >
              </li>
            </ul>
          </div>
          <div class="cb-col-25 cb-col">
            <div class="text-left cb-font-16 text-bold">FOLLOW US ON</div>
            <ul class="cb-ftr-ul">
              <li class="cb-ftr-lst">
                <a
                  class="text-white"
                  title="Facebook"
                  href="https://www.facebook.com/cricbuzz"
                  target="_blank"
                  rel="noopener noreferrer"
                  ><span class="cb-social-fb cb-ico"></span
                  ><span class="cb-footer-list-rt">facebook</span></a
                >
              </li>
              <li class="cb-ftr-lst">
                <a
                  class="text-white"
                  title="Twitter"
                  href="https://twitter.com/cricbuzz"
                  target="_blank"
                  rel="noopener noreferrer"
                  ><span class="cb-social-twitter cb-ico"></span
                  ><span class="cb-footer-list-rt">twitter</span></a
                >
              </li>
              <li class="cb-ftr-lst">
                <a
                  class="text-white"
                  title="Youtube"
                  href="https://www.youtube.com/channel/UCSRQXk5yErn4e14vN76upOw"
                  target="_blank"
                  rel="noopener noreferrer"
                  ><span class="cb-social-ytbe cb-ico"></span
                  ><span class="cb-footer-list-rt">youtube</span></a
                >
              </li>
              <li class="cb-ftr-lst">
                <a
                  class="text-white"
                  title="Pinterest"
                  href="https://in.pinterest.com/cricbuzz/"
                  target="_blank"
                  rel="noopener noreferrer"
                  ><span class="cb-social-pinterest cb-ico"></span
                  ><span class="cb-footer-list-rt">Pinterest</span></a
                >
              </li>
            </ul>
          </div>
          <div class="cb-col-25 cb-col">
            <div class="text-left cb-font-16 text-bold">COMPANY</div>
            <ul class="cb-ftr-ul">
              <li class="cb-ftr-lst">
                <a class="text-white" title="Careers" href="/careers"
                  >Careers</a
                >
              </li>
              <li class="cb-ftr-lst">
                <a class="text-white" title="Advertise" href="/info/advertise"
                  >Advertise</a
                >
              </li>
              <li class="cb-ftr-lst">
                <a
                  class="text-white"
                  rel="nofollow"
                  title="Privacy Policy"
                  href="/info/privacy"
                  >Privacy Policy</a
                >
              </li>
              <li class="cb-ftr-lst">
                <a
                  class="text-white"
                  rel="nofollow"
                  title="Terms of Use"
                  href="/info/termsofuse"
                  >Terms of Use</a
                >
              </li>
              <li class="cb-ftr-lst">
                <a
                  class="text-white"
                  title="Cricbuzz TV Ads"
                  href="/product-blog/cricbuzz-mobile-apps-tv-ad-cricket-ka-keeda"
                  rel="noopener noreferrer"
                  >Cricbuzz TV Ads</a
                >
              </li>
              <li ng-if='$root.$GEO.isGeo("EU")' class="cb-ftr-lst">
                <a
                  class="text-white cursor-pointer"
                  title="Privacy Preferences"
                  onclick="window._sp_.loadPrivacyManagerModal(17869)"
                  >Privacy Preferences</a
                >
              </li>
            </ul>
          </div>
          <div class="cb-col-100 cb-col cb-ftr-cpyrght">
            &copy; 2024 Cricbuzz.com, Times Internet Limited. All rights
            reserved |
            <a
              class="cb-ftr-cpyrght text-hvr-underline"
              href="http://timesofindia.indiatimes.com/"
              target="_blank"
              rel="noopener noreferrer"
              >The Times of India</a
            >
            |
            <a
              href="http://navbharattimes.indiatimes.com/"
              target="_blank"
              rel="noopener noreferrer"
              class="cb-ftr-cpyrght text-hvr-underline"
              >Navbharat Times</a
            >
          </div>
        </div>
      </div>
    </footer>
    <div class="cb-col-100 cb-top-btn">
      <div
        id="top-btn"
        class="cb-text-white text-center text-bold"
        title="Go to top"
      >
        <div>Move to top</div>
        <div class="cb-pageup-arrow cb-ico"></div>
      </div>
    </div>
    <script type="text/javascript">
      var script_tag = document.getElementsByTagName("script")[0];
      (function () {
        var cmin = document.createElement("script");
        cmin.type = "text/javascript";
        cmin.async = true;
        cmin.src = "/dist/js/cricbuzz.min.1704179977.js";
        script_tag.parentNode.insertBefore(cmin, script_tag);
      })();
    </script>
    <script>
      var firebaseScript = [
        "https://www.gstatic.com/firebasejs/7.22.0/firebase-app.js",
        "https://www.gstatic.com/firebasejs/7.22.0/firebase-analytics.js",
      ];
      var firebaseJS = [];
      for (var i = 0; i < firebaseScript.length; i++) {
        firebaseJS[i] = document.createElement("script");
        firebaseJS[i].type = "text/javascript";
        firebaseJS[i].async = true;
        firebaseJS[i].src = firebaseScript[i];
        var stag = document.getElementsByTagName("script")[0];
        stag.parentNode.insertBefore(firebaseJS[i], stag);
      }
      function initializeFirebaseJS() {
        var firebaseConfig = {
          apiKey: "AIzaSyCTfMJJ_bLdOnp_OKuxi9ce8vmnzgqUHiM",
          authDomain: "cricbuzz-desktop.firebaseapp.com",
          databaseURL: "https://cricbuzz-desktop.firebaseio.com",
          projectId: "cricbuzz-desktop",
          storageBucket: "cricbuzz-desktop.appspot.com",
          messagingSenderId: "820819117977",
          appId: "1:820819117977:web:eabf3544ac136b1a643508",
          measurementId: "G-4H06J8XXQH",
        };
        if (typeof firebase != undefined) {
          var cbPlusState =
            localStorage.getItem("UserState") != null
              ? localStorage.getItem("UserState")
              : "NOTSET";
          var cbPlusUId =
            localStorage.getItem("UserId") != null
              ? localStorage.getItem("UserId")
              : "NOTSET";
          var cbSubscriptionPlan =
            localStorage.getItem("PlanId") != null
              ? "PLAN" + localStorage.getItem("PlanId")
              : "PLAN0";
          cbSubscriptionPlan =
            localStorage.getItem("TermId") != null
              ? cbSubscriptionPlan + "-TERM" + localStorage.getItem("TermId")
              : cbSubscriptionPlan;
          var is_premium_page = false;
          firebase.initializeApp(firebaseConfig);
          firebase
            .analytics()
            .setUserProperties({
              cb_user: cbPlusUId,
              cb_subscription_plan: cbSubscriptionPlan,
              cb_sub_user_state: cbPlusState,
            });
          firebase
            .analytics()
            .logEvent("cb_screen_name", { cb_premium_screen: is_premium_page });
        } else {
          setTimeout(initializeFirebaseJS, 3000);
        }
      }
      firebaseJS[1].onload = function () {
        initializeFirebaseJS();
      };
    </script>
    <noscript
      ><iframe
        src="//www.googletagmanager.com/ns.html?id=GTM-PGNCT7"
        height="0"
        width="0"
        style="display: none; visibility: hidden"
      ></iframe
    ></noscript>
    <script>
      (function (w, d, s, l, i) {
        w[l] = w[l] || [];
        w[l].push({ "gtm.start": new Date().getTime(), event: "gtm.js" });
        var f = d.getElementsByTagName(s)[0],
          j = d.createElement(s),
          dl = l != "dataLayer" ? "&l=" + l : "";
        j.async = true;
        j.src = "//www.googletagmanager.com/gtm.js?id=" + i + dl;
        f.parentNode.insertBefore(j, f);
      })(window, document, "script", "dataLayer", "GTM-PGNCT7");
    </script>
    <script>
      window.onerror = function (message, file, line) {
        var sFormattedMessage = "[" + file + " (" + line + ")] " + message;
        dataLayer.push({
          EventAction: "Application",
          EventLabel: sFormattedMessage,
          event: "Exceptions",
        });
      };
    </script>
  </body>
</html>
'''
soup = BeautifulSoup(html_document, 'html.parser')
soup.prettify()

first = soup.find_all('div',{'id':'innings_1'})
# print(first)
eng = first[0].find_all('span')
print(eng[0].text)
ab = first[0].find_all('div',{'class':'cb-col cb-col-100 cb-scrd-itms'})
ab_length = len(ab)
count = 0
bc = 0
run = 0
while count < ab_length - 7:
    bc = ab[count].find_all('div',{'class':'cb-col cb-col-25'})
    cd = bc[0].find_all('a',{'class':'cb-text-link'})
    run = ab[count].find_all('div',{'class':'cb-col cb-col-8 text-right text-bold'})
    print(cd[0].text + '->' + run[0].text)
    # print(run[0].text)
    # print(cd[0].text)
    count+=1

ind_first = soup.find_all('div',{'id':'innings_2'})
# print(first)
ind = ind_first[0].find_all('span')
print(ind[0].text)
ind_ab = ind_first[0].find_all('div',{'class':'cb-col cb-col-100 cb-scrd-itms'})
ind_ab_length = len(ind_ab)
ind_count = 0
ind_bc = 0
ind_run = 0
while ind_count < ind_ab_length - 7:
    ind_bc = ind_ab[ind_count].find_all('div',{'class':'cb-col cb-col-25'})
    ind_cd = ind_bc[0].find_all('a',{'class':'cb-text-link'})
    ind_run = ind_ab[ind_count].find_all('div',{'class':'cb-col cb-col-8 text-right text-bold'})
    print(ind_cd[0].text + '->' + ind_run[0].text)
    # print(run[0].text)
    # print(cd[0].text)
    ind_count+=1
