Name:           tagainijisho
Version:        1.0.3
Release:        13%{?dist}
Summary:        A free Japanese dictionary and study assistant

License:        GPLv3+ and CC-BY-SA
URL:            http://www.tagaini.net/
Source0:        https://github.com/Gnurou/tagainijisho/archive/1.0.3/%{name}-%{version}.tar.gz
Patch0:         %{name}-1.0.3-fts3_tokenizer.patch

BuildRequires:  qt-devel >= 4.5
BuildRequires:  cmake >= 2.8.1
BuildRequires:  sqlite-devel > 3.7.8
BuildRequires:  desktop-file-utils
%if 0%{?fedora}
BuildRequires:  libappstream-glib
%endif
Requires:       %{name}-common = %{version}-%{release}
Requires:       %{name}-dic-en = %{version}-%{release}

%description
Tagaini Jisho is a free, open-source Japanese dictionary and kanji lookup tool
that is available for Windows, MacOS X and Linux and aims at becoming your
Japanese study assistant. It allows you to quickly search for entries and mark
those that you wish to study, along with tags and personal notes. It also let
you train entries you are studying and follows your progression in remembering
them. Finally, it makes it easy to review entries you did not remember by
listing them on screen or printing them on a small booklet.

Tagaini Jisho also features complete stroke order animations for more than
6000 kanji.

%package common
Summary:        Common files of Tagaini Jisho
License:        CC-BY-SA
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description common
Common files of Tagaini Jisho

%package dic-de
Summary:        Tagaini Jisho Japanese/German dictionary
License:        CC-BY-SA
BuildArch:      noarch
Provides:       %{name}-dic = %{version}-%{release}
Requires:       %{name}-common = %{version}-%{release}

%description dic-de
A Japanese/German dictionary for Tagaini Jisho.

%package dic-en
Summary:        Tagaini Jisho Japanese/English dictionary
License:        CC-BY-SA
BuildArch:      noarch
Provides:       %{name}-dic = %{version}-%{release}
Requires:       %{name}-common = %{version}-%{release}

%description dic-en
A Japanese/English dictionary for Tagaini Jisho.

%package dic-es
Summary:        Tagaini Jisho Japanese/Spanish dictionary
License:        CC-BY-SA
BuildArch:      noarch
Provides:       %{name}-dic = %{version}-%{release}
Requires:       %{name}-common = %{version}-%{release}

%description dic-es
A Japanese/Spanish dictionary for Tagaini Jisho.

%package dic-fr
Summary:        Tagaini Jisho Japanese/French dictionary
License:        CC-BY-SA
BuildArch:      noarch
Provides:       %{name}-dic = %{version}-%{release}
Requires:       %{name}-common = %{version}-%{release}

%description dic-fr
A Japanese/French dictionary for Tagaini Jisho.

%package dic-it
Summary:        Tagaini Jisho Japanese/Italian dictionary
License:        CC-BY-SA
BuildArch:      noarch
Provides:       %{name}-dic = %{version}-%{release}
Requires:       %{name}-common = %{version}-%{release}

%description dic-it
A Japanese/Italian dictionary for Tagaini Jisho.

%package dic-pt
Summary:        Tagaini Jisho Japanese/Portuguese dictionary
License:        CC-BY-SA
BuildArch:      noarch
Provides:       %{name}-dic = %{version}-%{release}
Requires:       %{name}-common = %{version}-%{release}

%description dic-pt
A Japanese/Portuguese dictionary for Tagaini Jisho.

%package dic-ru
Summary:        Tagaini Jisho Japanese/Russian dictionary
License:        CC-BY-SA
BuildArch:      noarch
Provides:       %{name}-dic = %{version}-%{release}
Requires:       %{name}-common = %{version}-%{release}

%description dic-ru
A Japanese/Russian dictionary for Tagaini Jisho.

%package dic-th
Summary:        Tagaini Jisho Japanese/Thai dictionary
License:        CC-BY-SA
BuildArch:      noarch
Provides:       %{name}-dic = %{version}-%{release}
Requires:       %{name}-common = %{version}-%{release}

%description dic-th
A Japanese/Thai dictionary for Tagaini Jisho.

%package dic-tr
Summary:        Tagaini Jisho Japanese/Turkish dictionary
License:        CC-BY-SA
BuildArch:      noarch
Provides:       %{name}-dic = %{version}-%{release}
Requires:       %{name}-common = %{version}-%{release}

%description dic-tr
A Japanese/Turkish dictionary for Tagaini Jisho.


%prep
%setup -q
%patch0 -p1 -b .fts3_tokenizer
rm -rf ./3rdparty/sqlite

%build
%cmake .

make %{?_smp_mflags}


%install
%make_install

%find_lang %{name} --with-qt
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%if 0%{?rhel}
rm -f $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.appdata.xml
%else
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
mv $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.appdata.xml \
   $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml
%endif

%files -f %{name}.lang
%doc doc/AUTHORS COPYING.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%if 0%{?fedora}
%{_datadir}/appdata/*.appdata.xml
%endif

%files common
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.css
%{_datadir}/%{name}/*.html
%{_datadir}/%{name}/doc
%{_datadir}/%{name}/jmdict.db
%{_datadir}/%{name}/kanjidic2.db

%files dic-de
%{_datadir}/%{name}/jmdict-de.db
%{_datadir}/%{name}/kanjidic2-de.db

%files dic-en
%{_datadir}/%{name}/jmdict-en.db
%{_datadir}/%{name}/kanjidic2-en.db

%files dic-es
%{_datadir}/%{name}/jmdict-es.db
%{_datadir}/%{name}/kanjidic2-es.db

%files dic-fr
%{_datadir}/%{name}/jmdict-fr.db
%{_datadir}/%{name}/kanjidic2-fr.db

%files dic-it
%{_datadir}/%{name}/jmdict-it.db
%{_datadir}/%{name}/kanjidic2-it.db

%files dic-pt
%{_datadir}/%{name}/jmdict-pt.db
%{_datadir}/%{name}/kanjidic2-pt.db

%files dic-ru
%{_datadir}/%{name}/jmdict-ru.db
%{_datadir}/%{name}/kanjidic2-ru.db

%files dic-th
%{_datadir}/%{name}/jmdict-th.db
%{_datadir}/%{name}/kanjidic2-th.db

%files dic-tr
%{_datadir}/%{name}/jmdict-tr.db
%{_datadir}/%{name}/kanjidic2-tr.db


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Martin Sourada <mso@fedoraproject.org> - 1.0.3-10
- First atempt to fix FTBFS and RHBZ #1395381

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.3-2
- Rebuilt for GCC 5 C++11 ABI change

* Sun Mar 08 2015 Martin Sourada <mso@fedoraproject.org> - 1.0.3-1
- Update to new bugfix release
- Re-add skip code, now licensed as CC-BY-SA-4.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 25 2014 Martin Sourada <mso@fedoraproject.org> - 1.0.1-2
- Update build-deps.

* Mon Feb 24 2014 Martin Sourada <mso@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1 (rhbz #1033895)
- Remove skip code from kanjidic2 (rhbz #969414) -- licence does not permit
  redistribution.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 11 2013 Martin Sourada <mso@fedoraproject.org> - 0.9.4-5
- Require -dic-en by main package for proper function on unsupported
  locales

* Sat Feb 09 2013 Martin Sourada <mso@fedoraproject.org> - 0.9.4-4
- Fix -common subpackage Summary and %%description
- Move more noarch files to -common subpackage
- Do not include separate licence text, they're not required by
  the licences, so shipping only those included in upstream
  tarball

* Fri Feb 08 2013 Martin Sourada <mso@fedoraproject.org> - 0.9.4-3
- Remove rm -rf %%{buildroot} from %%install
- Fix licences (JMdict and kanjidic2 are CC-BY-SA)
- Split -common subpackage with JMdict and kanjidic2 databases

* Mon Jan 14 2013 Martin Sourada <mso@fedoraproject.org> - 0.9.4-2
- Add missing BRs
- Remove 3rdparty/sqlite during prepapre -- not needed

* Sat Jan 05 2013 Martin Sourada <mso@fedoraproject.org> - 0.9.4-1
- Initial RPM package
