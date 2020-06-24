Name:           kitsune
Version:        2.0
Release:        28%{?dist}
Summary:        Program to solve mathematical problems

License:        GPLv2+
URL:            http://%{name}.tuxfamily.org/wiki/doku.php?id=homepage
Source0:        http://%{name}.tuxfamily.org/%{name}/%{name}%{version}/%{name}%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        http://%{name}.tuxfamily.org/download.php?url=icons/%{name}-icones.tar.gz

BuildRequires:  qt4-devel
BuildRequires:  desktop-file-utils

%description
Kitsune is a software aiming at solving digit problems 
of a famous television game show called "Countdown" in England 
and "Les chiffres et les lettres" in France.

%prep
%setup -q -a 2 -n %{name}%{version}

for f in Changelog.txt txt/gpl-fr.html txt/aide-fr.html txt/licence-fr.html ; do
   %{_bindir}/iconv -f iso8859-1 -t utf-8 ${f} > ${f}.conv && /bin/mv -f ${f}.conv ${f}
   /bin/sed -i -e "s/ISO-8859-1/UTF-8/" ${f} 
done

%build
%{qmake_qt4}
lrelease-qt4 kitsune.pro
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 0755 bin/kitsune $RPM_BUILD_ROOT%{_bindir}

for f in 16 22 32 48 64 ; do
  mkdir -p  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${f}x${f}/apps
  install -p -m 0644 %{name}-icones/%{name}-${f}X${f}.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${f}x${f}/apps/%{name}.png || \
  install -p -m 0644 %{name}-icones/%{name}-${f}x${f}.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${f}x${f}/apps/%{name}.png
done

desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
       --vendor="fedora"                                 \
%endif
       --dir=$RPM_BUILD_ROOT%{_datadir}/applications    \
       %{SOURCE1}



%files
%doc Changelog.txt txt/*
%{_bindir}/%{name}
%if 0%{?fedora} && 0%{?fedora} < 19
%{_datadir}/applications/fedora-%{name}.desktop
%else
%{_datadir}/applications/%{name}.desktop
%endif
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0-23
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.0-18
- use %%qmake_qt4 macro to ensure proper build flags

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.0-16
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar  6 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 2.0-12
- Remove vendor prefix from desktop files in F19+ https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-9
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.0-4
- Autorebuild for GCC 4.3

* Wed Dec 12 2007 Martin-Gomez Pablo <pablo.martin-gomez@laposte.net> 2.0-3
- Change Source0 adress
- Change in %%setup option
- Complete change of some files' encoding
- Simplification of icon installing
- Correct files' ownership in %%files

* Mon Dec 3 2007 Martin-Gomez Pablo <pablo.martin-gomez@laposte.net> 2.0-2
- Add update GTK+ icon cache
- Add icon 
- Remove deprecated key from desktop file
- Change of some files' encoding

* Wed Nov 7 2007 Martin-Gomez Pablo <pablo.martin-gomez@laposte.net> 2.0-1
- First RPM release. 
