Name:           PySolFC
Version:        2.10.0
Release:        1%{?dist}
Summary:        A collection of solitaire card games
License:        GPLv2+
URL:            https://pysolfc.sourceforge.io
Source0:        https://downloads.sourceforge.net/pysolfc/%{name}-%{version}.tar.xz
Source1:        pysol-start-script
Source2:        PySolFC-Cardsets--Minimal-2.0.tar.xz
Patch0:         PySolFC-desktop-exec.patch
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  desktop-file-utils
BuildRequires:  perl-interpreter
BuildRequires:  /usr/bin/pathfix.py
# optional but nice to have
Requires:       freecell-solver
Requires:       libfreecell-solver
Requires:       python%{python3_pkgversion}-freecell_solver
Requires:       python%{python3_pkgversion}-imaging
Requires:       tile
# used to get sound working with PulseAudio
Requires:       python%{python3_pkgversion}-pygame
# really required
Requires:       tcl
Requires:       tk
Requires:       tix
Requires:       python%{python3_pkgversion}-tkinter
Requires:       python%{python3_pkgversion}-imaging-tk
Requires:       python%{python3_pkgversion}-random2
%if 0%{?fedora} || 0%{?rhel} > 7
Recommends:     PySolFC-cardsets
Recommends:     PySolFC-music
%endif
Provides:       pysol = %{version}-%{release}

%description
%{name} is a collection of more than 1000 solitaire card games. It is a fork
of PySol solitaire. Its features include modern look and feel (uses Tile widget
set), multiple cardsets and tableau backgrounds, sound, unlimited undo, player
statistics, a hint system, demo games, a solitaire wizard, support for user
written plug-ins, an integrated HTML help browser, and lots of documentation.

%prep
%setup -q -a2
%patch0 -p1 -b .desktop-exec

%build
%py3_build

%install
%py3_install
# install desktop file
desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
    --vendor="fedora" \
%endif
    --delete-original \
    --dir=$RPM_BUILD_ROOT/%{_datadir}/applications \
    $RPM_BUILD_ROOT/%{_datadir}/applications/pysol.desktop

# install the startup wrapper
mv $RPM_BUILD_ROOT%{_bindir}/pysol.py $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m755 %{SOURCE1} $RPM_BUILD_ROOT/%{_bindir}/pysol
cp -a PySolFC-Cardsets--Minimal-2.0/cardset-* $RPM_BUILD_ROOT%{_datadir}/PySolFC
find "$RPM_BUILD_ROOT%{python3_sitelib}/pysollib" -name '*.py' | xargs -L1 perl -ln -i -E 'say if (not (($. == 1) and (m&^#![ \t]*/usr/&)))'
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" $RPM_BUILD_ROOT%{_bindir}/*

%find_lang pysol

%files -f pysol.lang
%license COPYING
%doc README.md
%{python3_sitelib}/pysollib
%{python3_sitelib}/*egg-info
%{_bindir}/pysol
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/applications/*.desktop


%changelog
* Tue Jun 23 2020 Shlomi Fish <shlomif@shlomifish.org> 2.10.0-1
- New upstream release
- Add BuildRequires on setuptools
- Add Requires on python3-freecell_solver

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.8.0-3
- Rebuilt for Python 3.9

* Sat Mar 28 2020 Shlomi Fish <shlomif@cpan.org> 2.8.0-2
- Fix or remove shebangs (RHBZ 1818150)
- Correct the changelog

* Tue Mar 24 2020 Shlomi Fish <shlomif@cpan.org> 2.8.0-1
- New upstream version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.6.4-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.6.4-7
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 11 2019 Sérgio Basto <sergio@serjux.com> - 2.6.4-5
- Fix some missing %%{python3_pkgversion}

* Mon May 06 2019 Sérgio Basto <sergio@serjux.com> - 2.6.4-4
- Add Minimal Cardsets

* Wed May 01 2019 Sérgio Basto <sergio@serjux.com> - 2.6.4-3
- Requires cartsets and music, clean old stuff and enable build for epel7

* Sun Apr 28 2019 Sérgio Basto <sergio@serjux.com> - 2.6.4-2
- Sound fix, seems using SOUND_MOD=auto it works

* Fri Apr 26 2019 Sérgio Basto <sergio@serjux.com> - 2.6.4-1
- Upgrade to 2.6.4 and python3 by Shlomi Fish
- Modernize spec
- Add Requires: python3-random2
- Reenable defaults of debug package and automagic Python byte compilation

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 11 2017 Iryna Shcherbina <ishcherb@redhat.com> - 2.0-16
- Fix ambiguous Python 2 dependency declarations
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-13
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar  6 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 2.0-8
- Remove vendor prefix from desktop files in F19+ https://fedorahosted.org/fesco/ticket/1077

* Wed Jan 30 2013 Toshio Kuratomi <toshio@fedoraproject.org> 2.0-7
- Build with a patch so we can use python-pillow instead of python-imaging

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Feb 22 2010 Stewart Adam <s.adam at diffingo.com> - 2.0-2
- Patch desktop file to use pysol and not pysol.py for exec
- Force pygame as sound mod, makes PySolFC work with PulseAudio

* Mon Jan 18 2010 Stewart Adam <s.adam at diffingo.com> - 2.0-1
- Update to 2.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.1-7
- Rebuild for Python 2.6

* Fri Apr 4 2008 Stewart Adam <s.adam@diffingo.com> 1.1-6
- Fix Source0 URL
- Add egg-info file
- Remove deprecated Encoding key from desktop file

* Sat Jan 19 2008 Stewart Adam <s.adam@diffingo.com> 1.1-5
- Rebuild

* Thu Nov 1 2007 Stewart Adam <s.adam@diffingo.com> 1.1-4
- Provides: pysol since PySolFC is almost a drop-in replacement for
  the now unmaintained pysol

* Mon Oct 22 2007 Stewart Adam <s.adam@diffingo.com> 1.1-3
- s/python-imageing-tk/python-imaging-tk/

* Fri Oct 19 2007 Stewart Adam <s.adam@diffingo.com> 1.1-2
- Add Requires: python-imageing-tk

* Sat Sep 29 2007 Stewart Adam <s.adam@diffingo.com> 1.1-1
- Initial release

