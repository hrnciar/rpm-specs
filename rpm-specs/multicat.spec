Name:           multicat
Version:        2.3
Release:        6%{?dist}
Summary:        Simple and efficient multicast and transport stream manipulation

License:        GPLv2+
URL:            http://www.videolan.org/projects/multicat.html
Source0:        https://get.videolan.org/multicat/%{version}/multicat-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  bitstream-devel >= 1.4


%description
Simple and efficient multicast and transport stream manipulation.


%prep
%setup -q
sed -i -e 's|-O3|%{optflags}|' Makefile


%build
%make_build


%install
%make_install PREFIX=%{_prefix}
chmod -x %{buildroot}%{_mandir}/man1/*


%files
%doc AUTHORS Changelog README
%license COPYING
%{_bindir}/aggregartp
%{_bindir}/ingests
%{_bindir}/lasts
%{_bindir}/multicat
%{_bindir}/multicat_validate
%{_bindir}/multilive
%{_bindir}/offsets
%{_bindir}/reordertp
%{_mandir}/man1/aggregartp.1.*
%{_mandir}/man1/ingests.1.*
%{_mandir}/man1/lasts.1.*
%{_mandir}/man1/multicat.1.*
%{_mandir}/man1/offsets.1.*
%{_mandir}/man1/reordertp.1.*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 04 2018 Nicolas Chauvet <kwizart@gmail.com> - 2.3-1
- Update to 2.3

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 29 2016 Nicolas Chauvet <kwizart@gmail.com> - 2.1-1
- Update to 2.1

* Mon Jan 16 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.0-1
- Update to 2.0

* Sat Apr 24 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 1.0-1
- Initial spec file
