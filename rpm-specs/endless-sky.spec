%define		gittag0		v0.9.12

Name:		endless-sky
Version:	0.9.12
Release:	3%{?dist}
Summary:	Space exploration, trading, and combat game

License:	GPLv3
URL:		https://%{name}.github.io
Source0:	https://github.com/%{name}/%{name}/archive/%{gittag0}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        endless-sky-wrapper
# Replace /usr/games with /usr/bin and /usr/share/games with /usr/share per
# https://fedoraproject.org/wiki/SIGs/Games/Packaging.
# Patch not submitted upstream. Upstream conforms to Debian packaging
# standards where the use of /usr/games is acceptable.
Patch0:		endless-sky-0.8.10-remove-games-path.patch
# Unset CCFLAGS override inside SConstruct.
Patch1:		endless-sky-0.9.4-remove-additional-ccflags.patch
Patch2:		endless-sky-0.9.10-gcc10.patch
Patch3:         endless-sky-gcc11.patch

Requires:	%{name}-data = %{version}-%{release}
BuildRequires:	scons
BuildRequires:	gcc-c++
BuildRequires:	SDL2-devel
BuildRequires:	openal-soft-devel
BuildRequires:	glew-devel
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libappstream-glib
BuildRequires:	desktop-file-utils
BuildRequires:	libmad-devel

%description
Explore other star systems. Earn money by trading, carrying passengers, or
completing missions. Use your earnings to buy a better ship or to upgrade the
weapons and engines on your current one. Blow up pirates. Take sides in a civil
war. Or leave human space behind and hope to find some friendly aliens whose
culture is more civilized than your own...


%package data
Summary:	Game data for %{name}
# Sound and images appear to be a mix of Public Domain and CC-BY-SA licensing
# See copyright for details.
License:	Public Domain and CC-BY-SA
BuildArch:	noarch


%description data
Images, sound, and game data for %{name}.


%prep
%autosetup -p0


%build
%ifarch ppc64le
sed -i 's/std=c++11/std=gnu++11/' SConstruct
%endif
CXXFLAGS="%{optflags}"		\
LDFLAGS="%{?__global_ldflags}"	\
/usr/bin/scons		\
	%{?_smp_mflags}		\
	PREFIX=%{_prefix}

%check
appstream-util validate-relax --nonet %{name}.appdata.xml
desktop-file-validate %{name}.desktop


%install
CXXFLAGS="%{optflags}"		\
LDFLAGS="%{?__global_ldflags}"	\
/usr/bin/scons		\
	%{?_smp_mflags}		\
	PREFIX=%{_prefix}	\
	DESTDIR=%{buildroot}	\
	install
install -m644 -D endless-sky.appdata.xml %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
mv %{buildroot}%{_bindir}/%{name}  %{buildroot}%{_bindir}/%{name}.bin
install -m755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}
sed -i 's|/app|%{_prefix}|g' %{buildroot}%{_bindir}/%{name}

%files
%doc README.md
%license license.txt
%{_bindir}/%{name}*
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/22x22/apps/%{name}.png
%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_mandir}/man6/%{name}.6.gz


%files data
%license copyright
%{_datadir}/%{name}


%changelog
* Wed Oct 14 2020 Jeff Law <law@redhat.com> - 0.9.12-3
- Add missing #includes for gcc-11

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 02 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.9.12-1
- 0.9.12

* Tue Feb 25 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.9.11-1
- 0.9.11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Jeff Law <law@redhat.com> - 0.9.10-2
- Fix missing #include for gcc-10

* Mon Sep 30 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.9.10-1
- 0.9.10
- Environment patch upstreamed.

* Wed Aug 21 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.9.8-12
- Add flatpak wrapper.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 fedora-toolbox <otaylor@redhat.com> - 0.9.8-9
- Pass the entire environment to build commands; fixes CPLUS_INCLUDE_PATH for
  flatpaks.

* Fri Sep  7 2018 Owen Taylor <otaylor@redhat.com> - 0.9.8-8
- scons is in /usr/bin, even if we're compiling with a different %%{_prefix}

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.9.8-7
- Rebuilt for glew 2.1.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 0.9.8-5
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.8-3
- Remove obsolete scriptlets

* Wed Sep 13 2017 Link Dupont <linkdupont@fedoraproject.org> - 0.9.8-2
- Remove GNU C++ extensions patch
- Only use GNU C++ extensions when building on ppc64le

* Mon Aug 21 2017 Link Dupont <linkdupont@fedoraproject.org> - 0.9.8-1
- New upstream release (RH#1473666)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sun Feb 26 2017 Link Dupont <linkdupont@fedoraproject.org> - 0.9.6-1
- New upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 0.9.4-5
- Rebuild for glew 2.0.0

* Sun Jan 1 2017 Link Dupont <linkdupont@fedoraproject.org> - 0.9.4-4
- Remove CCFLAGS override inside SConstruct

* Sat Dec 31 2016 Link Dupont <linkdupont@fedoraproject.org> - 0.9.4-3
- Build and install with identical CXXFLAGS (RH#1402807)

* Thu Dec 8 2016 Link Dupont <linkdupont@fedoraproject.org> - 0.9.4-2
- Build with $RPM_OPT_FLAGS (#1402807)

* Sat Oct 15 2016 Link Dupont <linkdupont@fedoraproject.org> - 0.9.4-1
- New upstream release
- Remove local appdata.xml file deferring to upstream

* Sat Aug 20 2016 Link Dupont <linkdupont@fedoraproject.org> - 0.9.2-1
- New upstream release
- Remove installation of 'extra' directory

* Sat Jan 16 2016 Link Dupont <linkdupont@fedoraproject.org> - 0.8.10-5
- Add strict version requirement to data package
- Document dual licensing characteristics of game data
- Add appdata validation
- Update icon cache on installation

* Mon Jan 11 2016 Link Dupont <linkdupont@fedoraproject.org> - 0.8.10-4
- Combine patches into single file

* Sun Jan 10 2016 Link Dupont <linkdupont@fedoraproject.org> - 0.8.10-3
- Patch game to load resources from /usr/share/endless-sky

* Sun Jan 10 2016 Link Dupont <linkdupont@fedoraproject.org> - 0.8.10-2
- Split data into separate package
- Patch game to avoid deprecated path /usr/games

* Sat Jan 9 2016 Link Dupont <linkdupont@fedoraproject.org> - 0.8.10-1
- New upstream release
- Added appdata.xml

* Sun Jan 3 2016 Link Dupont <linkdupont@fedoraproject.org> - 0.8.9-1
- Initial package
