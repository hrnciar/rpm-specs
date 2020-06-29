# Generated by go2rpm 1
%bcond_without check

# https://github.com/chromedp/cdproto
%global goipath         github.com/chromedp/cdproto
%global commit          7e00b02ea7d290cf17b5a5c6f81d7a18b6810379

%gometa

%global common_description %{expand:
Package cdproto contains the generated commands, types, and events for the
Chrome DevTools Protocol domains.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Generated commands, types, and events for the Chrome DevTools Protocol domains

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/knq/sysutil)
BuildRequires:  golang(github.com/mailru/easyjson)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Mon Apr 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.1.20200406git7e00b02
- Initial package

