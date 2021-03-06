# Generated by go2rpm 1
%bcond_without check

# https://github.com/dustmop/soup
%global goipath         github.com/dustmop/soup
Version:                1.1.1

%gometa

%global common_description %{expand:
Web Scraper in Go, similar to BeautifulSoup.}

%global golicenses      license
%global godocs          examples CHANGELOG.md README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Web Scraper in Go, similar to BeautifulSoup

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/net/html)

%description
%{common_description}

%gopkg

%prep
%goprep
sed -i 's|github.com/anaskhan96/soup|github.com/dustmop/soup|' $(find . -iname "*.go" -type f)

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Mon Aug 17 10:03:29 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.1-1
- Initial package
