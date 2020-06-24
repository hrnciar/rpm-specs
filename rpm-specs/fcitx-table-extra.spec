Name:		fcitx-table-extra
Version:	0.3.8
Release:	7%{?dist}
Summary:	Extra tables for Fcitx
License:	GPLv2+
URL:		http://fcitx-im.org/wiki/Fcitx
Source0:	http://download.fcitx-im.org/%{name}/%{name}-%{version}.tar.xz

BuildRequires:	cmake, fcitx-devel, gettext, intltool, libtool, fcitx
BuildArch:	noarch
Requires:	fcitx

%description
Fcitx-table-extra provides extra table for Fcitx, including Boshiamy, Zhengma,
and Cangjie 3/5.

Boshiamy table and its icon are released under their own license.


%prep
%setup -q -n %{name}-%{version}


%build
mkdir -pv build
pushd build
%cmake ..
make VERBOSE=1 %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
pushd build
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
popd

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING
%{_datadir}/fcitx/table/*.mb
%{_datadir}/fcitx/table/*.conf
%{_datadir}/fcitx/imicon/*.png
%{_datadir}/icons/hicolor/64x64/apps/*.png
%{_datadir}/icons/hicolor/48x48/apps/*.png


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.8-2
- Remove obsolete scriptlets

* Sun Sep 24 2017 Robin Lee <cheeselee@fedoraproject> - 0.3.8-1
- Update to 0.3.8

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct  1 2015 Robin Lee <cheeselee@fedoraproject.org> - 0.3.7-1
- Update to 0.3.7

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 09 2013 Liang Suilong <liangsuilong@gmail.com> - 0.3.4-1
- Upstream to 0.3.4

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 09 2012 Liang Suilong <liangsuilong@gmail.com> - 0.3.3-1
- Upstream to 0.3.3

* Wed Jul 25 2012 Liang Suilong <liangsuilong@gmail.com> - 0.3.2-1
- Upstream to 0.3.2

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 07 2012 Liang Suilong <liangsuilong@gmail.com> - 0.3.0-1
- Upstream to 0.3.0

* Fri May 03 2012 Liang Suilong <liangsuilong@gmail.com> - 0.2.1-1
- Upstream to 0.2.1

* Wed Feb 08 2012 Liang Suilong <liangsuilong@gmail.com> - 0.1.0-1
- Initial Package
