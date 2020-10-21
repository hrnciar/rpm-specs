Name:           purple-plugin_pack
Version:        2.7.0
Release:        13%{?dist}
Summary:        A set of plugins for libpurple, pidgin, and finch

License:        GPLv2+
URL:            https://bitbucket.org/rekkanoryo/purple-plugin-pack
Source0:        https://bitbucket.org/rekkanoryo/purple-plugin-pack/downloads/purple-plugin-pack-%{version}.tar.bz2
Source1:        purple-plugin-pack.metainfo.xml

BuildRequires:  gcc
BuildRequires:  pidgin-devel xmms-devel perl(XML::Parser) gettext-devel
BuildRequires:  enchant-devel gtkspell-devel
BuildRequires:  diffutils intltool
BuildRequires:  python2
Provides:       purple-plugin-pack

%description
This package contains a number of plugins for use with the purple IM/IRC
library.

%package pidgin
Summary:        A set of plugins for pidgin
Requires:       %{name} = %{version}
Provides:       purple-plugin-pack-pidgin

%description pidgin
This package contains a number of plugins for use with the pidgin client.

%package pidgin-xmms
Summary:        A plugin for pidgin to control xmms
Requires:       %{name} = %{version}
Provides:       purple-plugin-pack-pidgin-xmms

%description pidgin-xmms
This package contains a plugin for pidgin to control xmms.

%prep
%setup -q -n purple-plugin-pack-%{version}

%build
%configure PYTHON=/usr/bin/python2
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name \*.la -exec rm {} \;
install -Dm 644 %SOURCE1 $RPM_BUILD_ROOT%{_datadir}/appdata/purple-plugin-pack.metainfo.xml
%find_lang plugin_pack

%files -f plugin_pack.lang
%doc AUTHORS ChangeLog COPYING NEWS
%{_datadir}/appdata/purple-plugin-pack.metainfo.xml
%{_libdir}/purple-2/*.so

%files pidgin
%doc AUTHORS ChangeLog COPYING NEWS
%dir %{_datadir}/pixmaps/pidgin/plugin_pack
%{_datadir}/pixmaps/pidgin/protocols
%{_libdir}/pidgin/[^x]*.so
%{_libdir}/pidgin/xchat-chats.so

%files pidgin-xmms
%{_datadir}/pixmaps/pidgin/plugin_pack/xmmsremote
%{_libdir}/pidgin/xmmsremote.so

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 16 2019 Pavel Raiskup <praiskup@redhat.com> - 2.7.0-11
- fix FTBFS (rhbz#1675694)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Jan Synáček <jsynacek@redhat.com> - 2.7.0-2
- Ship AppStream metainfo file (#1300463)

* Thu Jan 28 2016 Jan Synáček <jsynacek@redhat.com> - 2.7.0-1
- Update to 2.7.0 (#890738)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.6.3-3
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 04 2011 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 2.6.3-1
- Upstream update

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Nov 20 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 2.4.0-2
- Update Source0 URL

* Tue Oct  7 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 2.4.0-1
- Upstream update
- Extract inner function in switchspell (#462822)

* Sun Apr  6 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 2.3.0-1
- Upstream update

* Thu Feb 14 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 2.2.0-5
- Rebuild for GCC 4.3

* Tue Jan  8 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 2.2.0-4
- Switch from aspell to enchant (#427949)

* Mon Jan  7 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 2.2.0-3
- Switch from gtkspell to aspell

* Thu Nov 15 2007 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 2.2.0-2
- Added provides to other subpackages

* Wed Nov 14 2007 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 2.2.0-1
- Update to 2.2.0
- Add provides of purple-plugin-pack

* Thu Oct  4 2007 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 2.1.1-1
- Initial RPM release
