
Name:    prboom-plus
Version: 2.5.1.4
Release: 19%{?dist}
Summary: Free enhanced DOOM engine
URL:     http://prboom-plus.sourceforge.net/
License: GPLv2+ and MIT and Public Domain and BSD and LGPLv2+

Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1: %{name}.desktop
Source2: %{name}.png
Patch0: CVE-2019-20797.patch

Requires:      freedoom

BuildRequires:  gcc
BuildRequires: dumb-devel fluidsynth-devel pcre-devel libpng-devel
BuildRequires: SDL_image-devel SDL_mixer-devel SDL_net-devel libGLU-devel
BuildRequires: desktop-file-utils

%description
Doom is a classic 3D shoot-em-up game.
PrBoom+ is a Doom source port developed from the original PrBoom project
by Andrey Budko.
The target of the project is to extend the original port with features
that are necessary or useful.


%prep
%setup -q

%patch0 -p0

# fixing the FSF address
sed -i 's|59 Temple Place - Suite 330, Boston, MA  02111-1307, USA|51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA|' COPYING

%build
export CPPFLAGS="$CPPFLAGS -fcommon"
%configure --prefix=/usr \
           --with-waddir=%{_datadir}/doom \
           --disable-cpu-opt \
           --enable-gl

make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} docdir=%{_docdir}/%{name} install

# fixing the bin path
mv %{buildroot}/usr/games %{buildroot}%{_bindir}

# desktop + icons
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
install -Dpm 644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png


%files
%{_docdir}/*
%{_bindir}/*
%{_datadir}/doom/*
%{_mandir}/man5/*
%{_mandir}/man6/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.5.1.4-18
- Patch for CVE-2019-20797.

* Mon Feb 17 2020 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 2.5.1.4-17
- Rebuild against fluidsynth2

* Thu Feb 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.5.1.4-16
- Fix FTBFS.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 06 2018 Gwyn Ciesla <limburgher@gmail.com> - 2.5.1.4-1
- 2.5.1.4.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Nov 07 2013 Jaromir Capik <jcapik@redhat.com> - 2.5.1.3-3
- Replacing mktemp with mkstemp to satisfy rpmlint

* Thu Nov 07 2013 Jaromir Capik <jcapik@redhat.com> - 2.5.1.3-2
- Fixing the license tag

* Mon Nov 04 2013 Jaromir Capik <jcapik@redhat.com> - 2.5.1.3-1
- Initial package
