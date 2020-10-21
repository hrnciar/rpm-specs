Name:           toppler
Version:        1.1.5
Release:        21%{?dist}
Summary:        Platform game
License:        GPLv2+
URL:            http://toppler.sf.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch1:         toppler-1.1.5-move_hiscores_file.patch
Patch2:         toppler-1.1.5-highscore.patch
Patch3:         toppler-1.1.5-no-strncpy.patch
Patch4:         toppler-1.1.5-format-security.patch

BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  SDL-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  zlib-devel
BuildRequires:  gettext
BuildRequires:  desktop-file-utils


%description
Help a cute little green animal switch off some kind of "evil" mechanism. The
"power off switch" is hidden somewhere in high towers. On your way to the
target you need to avoid a lot of strange robots that guard the tower.


%prep
%setup -q
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p0

for i in AUTHORS ChangeLog toppler.6; do { 
  iconv -f iso8859-1 -t utf-8 $i > $i.utf8 && \
  touch -r $i $i.utf8 && \
  mv -f $i.utf8 $i;
};
done;


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
                     %{buildroot}/%{_datadir}/applications/toppler.desktop

touch %{buildroot}%{_localstatedir}/games/toppler.hsc

rm -rf %{buildroot}%{_datadir}/doc/toppler

%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/toppler
%{_datadir}/toppler
%{_datadir}/applications/toppler.desktop
%{_datadir}/pixmaps/toppler.xpm
%verify(not md5 size mtime) %config(noreplace) %attr(0664,root,games) %{_localstatedir}/games/toppler.hsc
%{_mandir}/man6/toppler.6.*


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 26 2018 Xavier Bachelot <xavier@bachelot.org> - 1.1.5-16
- Add BR: gcc.
- Clean up spec.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1.5-9
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 11 2014 Filipe Rosset <rosset.filipe@gmail.com> - 1.1.5-7
- Rebuilt to fix FTBFS, format-security patch, fixes rhbz #1107454, #1037362 and #926648

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue May 03 2011 Xavier Bachelot <xavier@bachelot.org> 1.1.5-1
- Update to 1.1.5.
- Add better highscore patch (from Hans de Goede).
- Add patch to remove strncpy (from Hans de Goede).
- Clean up spec.

* Sun Oct 11 2009 Xavier Bachelot <xavier@bachelot.org> 1.1.4-1
- Update to 1.1.4.
- Drop upstream'ed patches.

* Fri Oct 02 2009 Xavier Bachelot <xavier@bachelot.org> 1.1.3-4
- Fix highscores file lock creation patch to use a better mode.

* Fri Oct 02 2009 Xavier Bachelot <xavier@bachelot.org> 1.1.3-3
- Fix License.
- Fix buffer overflow in level editor.

* Tue Sep 22 2009 Xavier Bachelot <xavier@bachelot.org> 1.1.3-2
- Fix Source0 URL.
- Fix BuildRequires.
- Keep timestamp on files encoding conversion.
- Fix highscores directory ownership and mode.
- Add patch to create highscores file if missing.
- Ghost highscores file.

* Sat Nov 29 2008 Xavier Bachelot <xavier@bachelot.org> 1.1.3-1
- Initial build.
