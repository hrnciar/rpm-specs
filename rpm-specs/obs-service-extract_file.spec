%global commit 8ea7a76324b19e0ea3b1a559cbdfb8da9d038304
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapdate 20190325

%global service extract_file

Name:           obs-service-%{service}
# Version comes from what openSUSE has released as in openSUSE:Tools
# From: https://build.opensuse.org/package/show/openSUSE:Tools/obs-service-extract_file
Version:        0.3
Release:        5%{?snapdate:.%{snapdate}git%{shortcommit}}%{?dist}
Summary:        An OBS source service: Extract a file from an archive

License:        GPLv2+
URL:            https://github.com/openSUSE/obs-service-%{service}
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildArch:      noarch
Requires:       cpio
Requires:       bzip2
Requires:       findutils
Requires:       gzip
Requires:       tar
Requires:       unzip
Requires:       xz

%description
This is a source service for openSUSE Build Service.

It supports to extract a file from an archive, for example a spec file from a tar.


%prep
%autosetup -n %{name}-%{commit}


%build
# Nothing to build


%install
mkdir -p %{buildroot}%{_prefix}/lib/obs/service
install -pm 0755 extract_file %{buildroot}%{_prefix}/lib/obs/service
install -pm 0644 extract_file.service %{buildroot}%{_prefix}/lib/obs/service


%files
# In lieu of a proper license file: https://github.com/openSUSE/obs-service-extract_file/issues/13
%license debian/copyright
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service



%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-5.20190325git8ea7a76
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-4.20190325git8ea7a76
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-3.20190325git8ea7a76
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 25 2019 Neal Gompa <ngompa13@gmail.com> - 0.3-2.20190325git8ea7a763
- Add findutils dependency

* Mon Mar 25 2019 Neal Gompa <ngompa13@gmail.com> - 0.3-1.20190325git8ea7a763
- Initial packaging
