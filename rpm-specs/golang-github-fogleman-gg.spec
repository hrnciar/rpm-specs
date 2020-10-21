# Generated by go2rpm
# https://github.com/fogleman/gg/issues/79
%ifnarch aarch64 ppc64le s390x
%bcond_without check
%endif

# https://github.com/fogleman/gg
%global goipath         github.com/fogleman/gg
Version:                1.3.0
%global commit          ad4d1eafac46916fde6a6b375f7389e555f7e040

%gometa

%global common_description %{expand:
Gg is a library for rendering 2D graphics in pure Go.}

%global golicenses      LICENSE.md
%global godocs          examples README.md

Name:           %{goname}
Release:        7%{?dist}
Summary:        2D rendering in Go with a simple API

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
# https://github.com/fogleman/gg/issues/93
Patch0:         0001-fix-test-for-1.13.patch

BuildRequires:  golang(github.com/golang/freetype/raster)
BuildRequires:  golang(github.com/golang/freetype/truetype)
BuildRequires:  golang(golang.org/x/image/draw)
BuildRequires:  golang(golang.org/x/image/font)
BuildRequires:  golang(golang.org/x/image/font/basicfont)
BuildRequires:  golang(golang.org/x/image/font/gofont/goregular)
BuildRequires:  golang(golang.org/x/image/math/f64)
BuildRequires:  golang(golang.org/x/image/math/fixed)

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 26 17:33:04 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.0-6.20200726gitad4d1ea
- Bump to commit ad4d1eafac46916fde6a6b375f7389e555f7e040

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 30 2019 Robin Lee <cheeselee@fedoraproject.org> - 1.3.0-4
- Fix test with go 1.13+

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 16 23:37:24 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.0-2.20190516git72436a1
- Bump to commit 72436a171bf31757dc87fb8fa9f7485307350307

* Sat Mar 09 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.0-1
- Release 1.3.0

* Wed Mar 06 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.2.0-1
- Release 1.2.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2.git0e0ff3a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov  5 2018 mosquito <sensor.wen@gmail.com> - 1.1.0-1.20181106gite843337
- Initial package build
