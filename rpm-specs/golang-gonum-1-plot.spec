# Generated by go2rpm
%bcond_without check

# https://github.com/gonum/plot
%global goipath         gonum.org/v1/plot
%global forgeurl        https://github.com/gonum/plot
%global commit          e2840ee46a6b612972d746f9fea9920d329a0605

%gometa

%global common_description %{expand:
Plot provides an API for building and drawing plots in Go.}

%global golicenses      LICENSE
%global godocs          AUTHORS README.md

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Package for plotting and visualizing data

License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/ajstarks/svgo)
BuildRequires:  golang(github.com/fogleman/gg)
BuildRequires:  golang(github.com/golang/freetype/truetype)
BuildRequires:  golang(github.com/jung-kurt/gofpdf)
BuildRequires:  golang(golang.org/x/image/font)
BuildRequires:  golang(golang.org/x/image/math/fixed)
BuildRequires:  golang(golang.org/x/image/tiff)
BuildRequires:  golang(rsc.io/pdf)

%if %{with check}
# Tests
BuildRequires:  golang(golang.org/x/exp/rand)
BuildRequires:  golang(gonum.org/v1/gonum/floats)
BuildRequires:  golang(gonum.org/v1/gonum/mat)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck -d palette/moreland -d plotter
%endif

%gopkgfiles

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 22:30:38 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190703gite2840ee
- Initial package
