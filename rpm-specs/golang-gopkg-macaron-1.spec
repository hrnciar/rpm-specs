# Generated by go2rpm
%bcond_without check

# https://github.com/go-macaron/macaron
%global goipath         gopkg.in/macaron.v1
%global forgeurl        https://github.com/go-macaron/macaron
Version:                1.3.9

%gometa

%global goaltipaths     github.com/go-macaron/macaron

%global common_description %{expand:
Package Macaron is a high productive and modular web framework in Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        High productive and modular web framework in Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
# Go 1.15: https://github.com/go-macaron/macaron/issues/204
Patch0:         0001-Convert-int-to-string-using-fmt.Sprintf.patch

BuildRequires:  golang(github.com/go-macaron/inject)
BuildRequires:  golang(github.com/Unknwon/com)
BuildRequires:  golang(golang.org/x/crypto/pbkdf2)
BuildRequires:  golang(gopkg.in/ini.v1)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/smartystreets/goconvey/convey)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1
sed -i "s|github.com/unknwon/com|github.com/Unknwon/com|" $(find . -iname "*.go" -type f)

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Wed Jul 29 16:24:02 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.9-1
- Update to 1.3.9

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 18:22:06 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.2-2
- Update to new macros

* Fri Mar 22 2019 Nathan Scott <nathans@redhat.com> - 1.3.2-1
- First package for Fedora
