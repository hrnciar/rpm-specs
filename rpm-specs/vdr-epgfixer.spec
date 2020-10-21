%global pname   epgfixer
%global __provides_exclude_from ^%{vdr_plugindir}/
%global commit  354f28b0112ba27f08f6509243b410899f74b6ed
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20180416

Name:           vdr-%{pname}
Version:        0.3.1
Release:        14.%{gitdate}git%{shortcommit}%{?dist}
Summary:        VDR plugin for doing extra fixing of EPG data

License:        GPLv2+
URL:            https://projects.vdr-developer.org/projects/plg-epgfixer
Source0:        https://projects.vdr-developer.org/git/vdr-plugin-epgfixer.git/snapshot/vdr-plugin-epgfixer-%{commit}.tar.bz2

Source1:        %{name}.conf
# https://projects.vdr-developer.org/git/vdr-plugin-epgfixer.git/commit/?id=2b099cc01701e784fa5b1c53f38fd592b0b3ae42
Patch0:         0001-Fix-replacing-at-the-end-of-string-when-using-s-.-Fi.patch
# https://projects.vdr-developer.org/git/vdr-plugin-epgfixer.git/commit/?id=16d0db40d37706c79c7e911aebcdd344200a4725
Patch1:         0001-Fix-LoadConfigFile-return-value-on-success.patch

BuildRequires:  gcc-c++
BuildRequires:  vdr-devel >= 1.7.26
BuildRequires:  pcre-devel
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description
Epgfixer is a VDR plugin for doing extra fixing of EPG data. Features
include modifying EPG data using regular expressions, character set
conversions, blacklists, cloning EPG data, removing HTML tags, and
editing all settings through setup menu.


%prep
%setup -q -n vdr-plugin-%{pname}-%{commit}


%build
make CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC" %{?_smp_mflags} \
     LIBDIR=. LOCALEDIR=./locale VDRDIR=%{_libdir}/vdr


%install
install -dm 755 $RPM_BUILD_ROOT%{vdr_configdir}/plugins/%{pname}
install -pm 644 epgfixer/{blacklist,charset,epgclone,regexp}.conf \
    $RPM_BUILD_ROOT%{vdr_configdir}/plugins/%{pname}
install -Dpm 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
%make_install
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc HISTORY README
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
%{vdr_plugindir}/libvdr-%{pname}*.so.%{vdr_apiversion}
%defattr(-,%{vdr_user},root,-)
%config(noreplace) %{vdr_configdir}/plugins/%{pname}/
%defattr(-,root,root,-)


%changelog
* Fri Aug 28 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.3.1-14.20180416git354f28b
- Rebuilt for new VDR API version

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-13.20180416git354f28b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-12.20180416git354f28b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-11.20180416git354f28b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.3.1-10.20180416git354f28b
- Rebuilt for new VDR API version

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-9.20180416git354f28b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-8.20180416git354f28b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 26 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.3.1-7.20180416git354f28b
- Update to 0.3.1-7.20180416git354f28b
- Rebuilt for vdr-2.4.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  1 2016 Ville Skyttä <ville.skytta@iki.fi> - 0.3.1-1
- First Fedora build
