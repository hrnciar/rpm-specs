Name:             ddccontrol-db
URL:              https://github.com/ddccontrol/ddccontrol-db
Version:          20190825
Release:          3%{?dist}
# Agreed by usptream to be GPLv2+
# http://sourceforge.net/mailarchive/message.php?msg_id=29762202
License:          GPLv2+
Summary:          DDC/CI control database for ddccontrol
Source0:          https://github.com/ddccontrol/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# use autopoint instead of gettextize that is interactive tool
BuildRequires:    gettext, gettext-devel, libtool, intltool, perl(XML::Parser)
BuildArch:        noarch

%description
DDC/CU control database for DDCcontrol.

%prep
%setup -q

./autogen.sh

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md
%{_datadir}/%{name}

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20190825-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20190825-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 30 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 20190825-1
- New version
  Resolves: rhbz#1747028

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180602-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180602-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20180602-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun  6 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 20180602-1
- New version
  Resolves: rhbz#1587984

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20171217-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan  2 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 20171217-2
- Fixed URL

* Tue Dec 19 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 20171217-1
- New version
  Resolves: rhbz#1527446

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170716-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 20170716-1
- New version
- Dropped autopoint patch (not needed)

* Fri Jun 23 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 20061014-10.20170623git9dd986fb
- New snapshot
- New source URL (GitHub)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20061014-9.20120904gite8cc385a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20061014-8.20120904gite8cc385a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20061014-7.20120904gite8cc385a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20061014-6.20120904gite8cc385a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20061014-5.20120904gite8cc385a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20061014-4.20120904gite8cc385a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep  4 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 20061014-3.20120904gite8cc385a
- Updated to latest git head

* Tue Sep  4 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 20061014-2
- License tag changed to GPLv2+ (agreed by upstream)

* Wed Aug 29 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 20061014-1
- Initial version
