# Generated by go2rpm
# https://github.com/gophercloud/gophercloud/issues/1634
%ifnarch %{ix86} %{arm}
%bcond_without check
%endif

# https://github.com/gophercloud/gophercloud
%global goipath         github.com/gophercloud/gophercloud
Version:                0.12.0

%gometa

%global common_description %{expand:
Package Gophercloud provides a multi-vendor interface to OpenStack-compatible
clouds. The library has a three-level hierarchy: providers, services, and
resources.}

%global golicenses      LICENSE
%global godocs          docs CHANGELOG.md README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        OpenStack SDK for Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/crypto/ssh)
BuildRequires:  golang(gopkg.in/yaml.v2)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck -d acceptance/openstack/baremetal/noauth       \
         -d acceptance/openstack/imageservice/v2        \
         -d acceptance/openstack/networking/v2/extensions/qos/rules   \
         -t acceptance/openstack/sharedfilesystems/v2   \
         -d acceptance/openstack/workflow/v2
%endif

%gopkgfiles

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 15:50:15 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.12.0-1
- Update to 0.12.0

* Wed Feb 12 20:43:02 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.8.0-1
- Update to 0.8.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 02 20:01:24 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190627gite0311c0
- Initial package
