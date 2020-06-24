Name:           komparator
Version:        0.9
Release:        25%{?dist}
Summary:        Kompare and merge two folders

License:        GPLv2
URL:            http://komparator.sourceforge.net/
Source0:        http://downloads.sourceforge.net/sourceforge/komparator/%{name}-%{version}.tar.bz2
# fix FTBFS with g++ 4.7
Patch0:         komparator-0.9-gcc47.patch

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  kdelibs3-devel, desktop-file-utils

%description
Kompare and merge two folders.
They will be searched for duplicate files and empty folders.

%prep
%setup -q
%patch0 -p1 -b .gcc47
%{__sed} -i "s|\%u \%u|\%u|" src/%{name}.desktop

%build
unset QTDIR || : ; source /etc/profile.d/qt.sh
%configure \
         --disable-rpath

make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

HTML_DIR=$(kde-config --expandvars --install html)

# this is junk
rm -rf $RPM_BUILD_ROOT$HTML_DIR/%{name} 

# locale's
%find_lang %{name} || touch %{name}.lang
# HTML (1.0)
if [ -d $RPM_BUILD_ROOT$HTML_DIR ]; then
for lang_dir in $RPM_BUILD_ROOT$HTML_DIR/* ; do
  if [ -d $lang_dir ]; then
    lang=$(basename $lang_dir)
    echo "%lang($lang) $HTML_DIR/$lang/*" >> %{name}.lang
    # replace absolute symlinks with relative ones
    pushd $lang_dir
      for i in *; do
        [ -d $i -a -L $i/common ] && rm -f $i/common && ln -sf ../common $i/common
      done
    popd
  fi
done
fi

# Desktop.
desktop-file-install  \
%if 0%{?fedora} && 0%{?fedora} < 19
    --vendor fedora \
%endif
    --dir $RPM_BUILD_ROOT%{_datadir}/applications  \
    --delete-original \
        $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities/komparator.desktop


%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog README TODO
%{_bindir}/komparator
%{_datadir}/applications/*
%{_datadir}/icons/*/*/*/komparator.png
%{_datadir}/icons/*/*/*/komparator_working.mng


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9-20
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9-14
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar  6 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.9-10
- Remove vendor prefix from desktop files in F19+ https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jul 31 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.9-8
- Fix FTBFS with g++ 4.7

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Mar 25 2008 Rex Dieter <rdieter@fedoraproject.org> - 0.9-2
- drop broken BR: qt-devel
- BR: gettext
- BR: kdelibs3-devel (was kdebase3-devel)
- fix Source Url
- fix configure logic (64bit)

* Wed Feb 27 2008 Neal Becker <ndbecker2@gmail.com> - 0.9-1
- Update to 0.9

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.8-3
- Autorebuild for GCC 4.3

* Sun Dec  2 2007 Neal Becker <ndbecker2@gmail.com> - 0.8-2
- Fix mock build
- BR kdebase -> kdebase3

* Thu Oct 11 2007 Neal Becker <ndbecker2@gmail.com> - 0.7-1
- Update to 0.8

* Fri Aug 31 2007 Neal Becker <ndbecker2@gmail.com> - 0.7-1
- Update to 0.7

* Tue Aug 28 2007 Neal Becker <ndbecker2@gmail.com> - 0.6-3
- Fix .desktop entry for F8

* Tue Aug 28 2007 Neal Becker <ndbecker2@gmail.com> - 0.6-2
- Fix summary
- Add changelog
- Fix license
- Fix desktop-file-install
