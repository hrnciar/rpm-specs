Name:       kchildlock
Version:    0.91.1
Release:    12%{?dist}
License:    GPLv2
Source0:    http://downloads.sourceforge.net/kchildlock/%{name}/%{version}/%{name}-%{version}.tar.gz

Summary:    KDE Parental Control Application 
URL:        http://sourceforge.net/projects/kchildlock/ 

BuildRequires:  kdelibs4-devel
BuildRequires:  cmake >= 2.6
BuildRequires:  gettext

%description
kchildlock is a tool to monitor and restrict the time a children spends on the
computer. The limits can be specified per day of the week, by lower and upper
hour limits, maximum daily usage time, and maximum weekly usage time. The same
restriction limits can be applied to applications based on the user login. It
requires the KDE4 Desktop.

%prep
%setup -q

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ../
popd
make %{?_smp_mflags} -C %{_target_platform} 

%install
make install/fast DESTDIR=${RPM_BUILD_ROOT} -C %{_target_platform}

%find_lang %{name} --with-kde

%files -f %{name}.lang
%doc COPYING README TODO ChangeLog
%{_kde4_libdir}/kde4/*
%{_kde4_configdir}/kchildlockrc
%{_kde4_iconsdir}/hicolor/*/*/*
%{_kde4_datadir}/kde4/services/*
%{_localstatedir}/opt/%{name}/

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.91.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.91.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.91.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.91.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.91.1-8
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.91.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.91.1-6
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.91.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.91.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.91.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.91.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 16 2015 Vasiliy N. Glazov <vascom2@gmail.com> 0.91.1-1
- Update to 0.91.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.90.4.2-9
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 10 2012 Minh Ngo <minh@fedoraproject.org> 0.90.4.2-4
- Removing gtk2 requirement

* Sat Nov 10 2012 Minh Ngo <minh@fedoraproject.org> 0.90.4.2-3
- using %%find_lang --with-kde macro

* Sun Nov 04 2012 Minh Ngo <minh@fedoraproject.org> 0.90.4.2-2
- Changing the source archive URL (according to recommendations
for SourceForge
- Fixing kdelibs build dependencies
- Fixing kde source macroses
- Adding icon scriptlets

* Wed Sep 26 2012 Minh Ngo <nlminhtl@gmail.com> 0.90.4.2-1
- initial build
