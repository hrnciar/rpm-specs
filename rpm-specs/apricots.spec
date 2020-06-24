#remove once using %%configure again
%global debug_package %{nil}
%define apricotsdir %{_datadir}/apricots
Name: apricots
Version:  0.2.6
Release:  28%{?dist}
Summary: 2D air combat game

License: GPLv2
URL: http://www.fishies.org.uk/apricots.html
Source0: http://www.fishies.org.uk/apricots-%{version}.tar.gz       
Source1: apricots.png
#Icon created from screenshot on website
Source2: apricots.desktop
Patch0: apricots-0.2.6-alut-apricots.patch
Patch1: apricots-0.2.6-alut-sampleio.patch
Patch2: apricots-0.2.6-alut-configure.patch
# alut patches sent upstream.
Patch3: apricots-0.2.6-path.patch
#Patch4: apricots-0.2.6-alincludes.patch
BuildRequires: gcc gcc-c++
BuildRequires: SDL-devel
BuildRequires: freealut-devel
BuildRequires: desktop-file-utils
BuildRequires: openal-soft-devel
BuildRequires: autoconf automake
ExcludeArch: ppc64le aarch64

%description
It's a game where you fly a little plane around the screen and
shoot things and drop bombs on enemy targets, and it's meant to be quick 
and fun.

%prep
%setup -q

chmod -x apricots/*.cpp
chmod -x apricots/*.h
chmod -x AUTHORS
chmod -x ChangeLog
chmod -x COPYING
chmod -x README
chmod -x TODO

%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
#%patch4 -p0

%build
#Use %%configure once --as-needed is fixed, and fix debug at top of spec.
./configure --prefix=%{_prefix}
%make_build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 755 apricots/apricots %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/apricots
install -m 644 apricots/*.wav %{buildroot}%{_datadir}/apricots
mkdir -p %{buildroot}%{_sysconfdir}
install -m 644 apricots/apricots.cfg %{buildroot}%{_sysconfdir}
ln -s ../../..%{_sysconfdir}/apricots.cfg %{buildroot}%{_datadir}/apricots/apricots.cfg
install -m 644 apricots/*.psf %{buildroot}%{_datadir}/apricots
install -m 644 apricots/*.shapes %{buildroot}%{_datadir}/apricots

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install            \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE2}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps
install -p -m 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps


%files
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/apricots
%{_datadir}/apricots
%{_datadir}/applications/apricots.desktop
%{_datadir}/icons/hicolor/24x24/apps/apricots.png
%config(noreplace) %{_sysconfdir}/apricots.cfg


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 30 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.2.6-27
- Fix AP_PATH.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.2.6-25
- Fix FTBFS.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.2.6-23
- BR fix.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.6-20
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.2.6-14
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 09 2013 Jon Ciesla <limburgher@gmail.com> - 0.2.6-10
- Drop desktop vendor tag.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-8
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug 20 2009 Jon Ciesla <limb@jcomserv.net> - 0.2.6-5
- Rebuild for openal-soft.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Sep 09 2008 Jon Ciesla <limb@jcomserv.net> - 0.2.6-2
- Re-base off of pristine tarball, md5 error in review.

* Tue Aug 26 2008 Jon Ciesla <limb@jcomserv.net> - 0.2.6-1
- Initial packaging.
