# Generated by go2rpm
%bcond_without check

# https://github.com/kubernetes-sigs/structured-merge-diff
%global goipath         sigs.k8s.io/structured-merge-diff
%global forgeurl        https://github.com/kubernetes-sigs/structured-merge-diff
Version:                3.0.0

%gometa

%global common_description %{expand:
This package contains code which implements the Kubernetes "apply" operation.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md RELEASE.md code-of-\\\
                        conduct.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Test cases and implementation for "server-side apply"

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/json-iterator/go)
BuildRequires:  golang(gopkg.in/yaml.v2)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/google/gofuzz)
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
%gocheck
%endif

%gopkgfiles

%changelog
* Sun Apr 12 21:31:55 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 3.0.0-1
- Update to 3.0.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 06 20:47:45 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.6.20190706gite85c7b2
- Bump to commit e85c7b244fd2cc57bb829d73a061f93a441e63ce

* Sat Jul 06 18:40:21 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2.20190706git059502f
- Bump to commit 059502f641438a5cc3dc366d0b8a933bf67528b7

* Fri May 10 13:24:17 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190629gitea680f0
- Initial package