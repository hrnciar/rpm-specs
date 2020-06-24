# Generated by go2rpm
# Needs netlink
%bcond_with check

# https://github.com/mdlayher/wifi
%global goipath         github.com/mdlayher/wifi
%global commit          b1436901ddee2ea3ee8782a440a084e457615766

%gometa

%global common_description %{expand:
Package wifi provides access to IEEE 802.11 WiFi device actions and statistics.}

%global golicenses      LICENSE.md
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.7%{?dist}
Summary:        Access to IEEE 802.11 WiFi device actions and statistics

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/mdlayher/genetlink)
BuildRequires:  golang(github.com/mdlayher/netlink)
BuildRequires:  golang(github.com/mdlayher/netlink/nlenc)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/mdlayher/genetlink/genltest)
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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 23 14:25:53 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.5.20190523gitb143690
- Bmup to commit b1436901ddee2ea3ee8782a440a084e457615766

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git17fb838
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.3.git17fb838
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git17fb838
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Paul Gier <pgier@redhat.com> - 0-0.1.20180517git17fb838
- First package for Fedora
