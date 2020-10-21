# Generated by go2rpm
%bcond_without check

# https://github.com/opencontainers/selinux
%global goipath         github.com/opencontainers/selinux
Version:                1.6.0

%gometa

%global common_description %{expand:
Common SELinux package used across the container ecosystem.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md

%global gosupfiles      ${selinux[@]}

Name:           %{goname}
Release:        1%{?dist}
Summary:        Common SELinux implementation

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/pkg/errors)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%install
mapfile -t selinux <<< $(find . -name "*.go" -type f)
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Thu Jul 30 18:01:26 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.6.0-1
- Update to 1.6.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 04 17:43:15 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.2.2-1
- Initial package
