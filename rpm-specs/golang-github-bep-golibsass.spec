# Generated by go2rpm 1
%bcond_without check

# https://github.com/bep/golibsass
%global goipath         github.com/bep/golibsass
Version:                0.7.0

%gometa

%global godevelheader %{expand:
Requires:      gcc-c++
Requires:      libsass-devel}

%global common_description %{expand:
Easy to use Go bindings for LibSass. The primary motivation for this project is
to provide SCSS support to Hugo.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Easy to use Go bindings for LibSass

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  gcc-c++
BuildRequires:  libsass-devel
BuildRequires:  golang(github.com/frankban/quicktest)

%description
%{common_description}

%gopkg

%prep
%goprep

# Remove bundled libsass.
rm -r libsass_src
sed -e '/+build/d' internal/libsass/a__cgo_dev.go > internal/libsass/a__cgo.go
rm internal/libsass/a__cgo_dev.go

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.0-1
- Update to latest version

* Fri Feb 28 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.0-1
- Update to latest version

* Thu Feb 20 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.0-1
- Initial package
