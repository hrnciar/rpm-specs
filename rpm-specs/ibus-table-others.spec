%global cur_ver 1.3.10

Name:       ibus-table-others
Version:    1.3.11
Release:    2%{?dist}
Summary:    Various tables for IBus-Table
License:    GPLv3
URL:        http://github.com/moebiuscurve/ibus-table-others
Source0:    http://mfabian.fedorapeople.org/ibus-table-others/%{name}-%{version}.tar.gz
BuildArch:  noarch

Requires:         ibus-table
BuildRequires:    ibus-table-devel

%description
The package contains various IBus-Tables which include languages of \
Latin-America, Europe, Southeast Asia, as well as math and other symbols

%package -n ibus-table-code
Requires:  ibus-table
Summary:   Ibus-Tables for Latex, CNS11643 & Emoji

%description -n ibus-table-code
The package contains ibus-tables for Latex, CNS11643, Emoji. 

%package -n ibus-table-cyrillic
Requires:  ibus-table
Summary:   Ibus-Tables for Cyrillic

%description -n ibus-table-cyrillic
The Cyrillic rustrad & yawerty tables for IBus Table.

%package -n ibus-table-latin
Requires:  ibus-table
Summary:   Ibus-Tables for Latin

%description -n ibus-table-latin
The Latin compose & ipa-x-sampa tables for Ibus-Table.

%package -n ibus-table-translit
Requires:  ibus-table
Summary:   Ibus-Tables for Russian Translit

%description -n ibus-table-translit
The Cyrillic translit & translit-ua tables for IBus-Table.

%package -n ibus-table-tv
Requires:  ibus-table
Summary:   Ibus-Tables for Thai and Viqr (Vietnamese)

%description -n ibus-table-tv
The Thai and Viqr (Vietnamese) tables for IBus-Table.

%package -n ibus-table-mathwriter
Requires:  ibus-table
Summary:  Ibus-Tables for Unicode mathematics symbols

%description -n ibus-table-mathwriter
The package contains table for writing Unicode mathematics symbols.


%prep
%setup -q

%build
%configure

make %{?_smp_mflags}

%install
make DESTDIR=${RPM_BUILD_ROOT} NO_INDEX=true install
cd ${RPM_BUILD_ROOT}/%{_datadir}/ibus-table/tables/
%{_bindir}/ibus-table-createdb -i -n cns11643.db
%{_bindir}/ibus-table-createdb -i -n compose.db
%{_bindir}/ibus-table-createdb -i -n emoji-table.db
%{_bindir}/ibus-table-createdb -i -n ipa-x-sampa.db
%{_bindir}/ibus-table-createdb -i -n latex.db
%{_bindir}/ibus-table-createdb -i -n rusle.db
%{_bindir}/ibus-table-createdb -i -n rustrad.db
%{_bindir}/ibus-table-createdb -i -n thai.db
%{_bindir}/ibus-table-createdb -i -n translit.db
%{_bindir}/ibus-table-createdb -i -n translit-ua.db
%{_bindir}/ibus-table-createdb -i -n viqr.db
%{_bindir}/ibus-table-createdb -i -n yawerty.db
%{_bindir}/ibus-table-createdb -i -n mathwriter-ibus.db

# Register as AppStream components to be visible in the software center
#
# NOTE: It would be *awesome* if these files were maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/emoji-table.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<component type="inputmethod">
  <id>emoji-table.db</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>Emoji</name>
  <summary>Emoji input method</summary>
  <description>
    <p>
      Emoji is an input method that allows the user to enter pictographs that are used
      like emoticons.
      Some emoji strings are specific to Japanese culture.
    </p>
    <p>
      Input methods are typing systems allowing users to input complex languages.
      They are necessary because these contain too many characters to simply be laid
      out on a traditional keyboard.
    </p>
  </description>
  <url type="homepage">https://code.google.com/p/ibus-table-emoji/</url>
  <screenshots>
    <!-- FIXME: Needs an official up to date screenshot -->
    <screenshot type="default">
      <image>http://ibus-table-emoji.googlecode.com/hg/screenshot.png</image>
      <caption><!-- Describe this screenshot in less than ~10 words --></caption>
    </screenshot>
  </screenshots>  <url type="bugtracker">https://code.google.com/p/ibus/issues/list</url>
  <url type="help">https://code.google.com/p/ibus/wiki/FAQ</url>
  <languages>
    <lang percentage="100">zh_CN</lang>
    <lang percentage="100">zh_HK</lang>
    <lang percentage="100">zh_SG</lang>
    <lang percentage="100">zh_TW</lang>
  </languages>
  <update_contact><!-- upstream-contact_at_email.com --></update_contact>
</component>
EOF
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/ipa-x-sampa.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<component type="inputmethod">
  <id>ipa-x-sampa.db</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>International Phonetic Alphabet</name>
  <summary>IPA X-SAMPA input method</summary>
  <description>
    <p>
      International Phonetic Alphabet X-SAMPA is an input method.
      The Extended Speech Assessment Methods Phonetic Alphabet is a type of SAMPA
      developed by John C. Wells.
      It was designed to unify the individual SAMPA alphabets.
    </p>
    <p>
      Input methods are typing systems allowing users to input complex languages.
      They are necessary because these contain too many characters to simply be laid
      out on a traditional keyboard.
    </p>
    <p>
      Input methods are typing systems allowing users to input complex languages.
      They are necessary because these contain too many characters to simply be laid
      out on a traditional keyboard.
    </p>
  </description>
  <url type="homepage">https://github.com/mike-fabian/ibus-table-others</url>
  <url type="bugtracker">https://code.google.com/p/ibus/issues/list</url>
  <url type="help">https://code.google.com/p/ibus/wiki/FAQ</url>
  <update_contact><!-- upstream-contact_at_email.com --></update_contact>
</component>
EOF
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/mathwriter-ibus.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<component type="inputmethod">
  <id>mathwriter-ibus.db</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>Mathwriter</name>
  <summary>Math symbols input method</summary>
  <description>
    <p>
      The input method is designed for entering mathematical symbols.
    </p>
    <p>
      Input methods are typing systems allowing users to input complex languages.
      They are necessary because these contain too many characters to simply be laid
      out on a traditional keyboard.
    </p>
  </description>
  <url type="homepage">https://github.com/mike-fabian/ibus-table-others</url>
  <url type="bugtracker">https://code.google.com/p/ibus/issues/list</url>
  <url type="help">https://code.google.com/p/ibus/wiki/FAQ</url>
  <update_contact><!-- upstream-contact_at_email.com --></update_contact>
</component>
EOF

%files
%doc AUTHORS COPYING README

%files -n ibus-table-code
%{_datadir}/appdata/emoji-table.appdata.xml
%{_datadir}/ibus-table/tables/latex.db
%{_datadir}/ibus-table/tables/cns11643.db
%{_datadir}/ibus-table/tables/emoji-table.db
%{_datadir}/ibus-table/icons/latex.svg
%{_datadir}/ibus-table/icons/cns11643.png
%{_datadir}/ibus-table/icons/ibus-emoji.svg

%files -n ibus-table-cyrillic
%{_datadir}/ibus-table/tables/rusle.db
%{_datadir}/ibus-table/tables/rustrad.db
%{_datadir}/ibus-table/tables/yawerty.db
%{_datadir}/ibus-table/icons/rusle.png
%{_datadir}/ibus-table/icons/rustrad.png
%{_datadir}/ibus-table/icons/yawerty.png

%files -n ibus-table-latin
%{_datadir}/appdata/ipa-x-sampa.appdata.xml
%{_datadir}/ibus-table/tables/compose.db
%{_datadir}/ibus-table/tables/ipa-x-sampa.db
%{_datadir}/ibus-table/tables/hu-old-hungarian-rovas.db
%{_datadir}/ibus-table/icons/compose.svg
%{_datadir}/ibus-table/icons/ipa-x-sampa.svg
%{_datadir}/ibus-table/icons/hu-old-hungarian-rovas.svg

%files -n ibus-table-translit
%{_datadir}/ibus-table/tables/translit.db
%{_datadir}/ibus-table/tables/translit-ua.db
%{_datadir}/ibus-table/icons/translit.svg
%{_datadir}/ibus-table/icons/translit-ua.svg

%files -n ibus-table-tv
%{_datadir}/ibus-table/tables/telex.db
%{_datadir}/ibus-table/tables/thai.db
%{_datadir}/ibus-table/tables/viqr.db
%{_datadir}/ibus-table/tables/vni.db
%{_datadir}/ibus-table/icons/telex.png
%{_datadir}/ibus-table/icons/thai.png
%{_datadir}/ibus-table/icons/viqr.png
%{_datadir}/ibus-table/icons/vni.png

%files -n ibus-table-mathwriter
%{_datadir}/appdata/mathwriter-ibus.appdata.xml
%{_datadir}/ibus-table/tables/mathwriter-ibus.db
%{_datadir}/ibus-table/icons/mathwriter.png

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Mike FABIAN <mfabian@redhat.com> - 1.3.11-1
- update to latest upstream 1.3.11
- Add Vietnamese input methods Telex and VNI
  (thanks to Nguyễn Gia Phong <vn.mcsinyx@gmail.com>)
- Extend russian translit for latin slavic layouts
  (thanks to Marek Nečada <marek@necada.org>)

* Tue Jan 07 2020 Mike FABIAN <mfabian@redhat.com> - 1.3.10-1
- update to latest upstream 1.3.10
- latex: add most of Unicode 9.0 block Mathematical Alphanumeric Symbols
  (thanks to Pavel Zorin-Kranich)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Aug 18 2016 Mike FABIAN <mfabian@redhat.com> - 1.3.9-1
- update to latest upstream 1.3.9
- Add ZERO WIDTH JOINERS to hu-old-hungarian-rovas.txt to make
  ligatures work with supporting fonts

* Tue Aug 16 2016 Mike FABIAN <mfabian@redhat.com> - 1.3.8-1
- update to latest upstream 1.3.8
- Add table for Rovás (Old Hungarian)
- Fix wrong key for keyboard in rusle.txt

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jun 22 2015 Richard Hughes <rhughes@redhat.com> - 1.3.7-4
- Increase AppStream search result weighting when using various 'zh' locales.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 25 2015 Richard Hughes <rhughes@redhat.com> - 1.3.7-2
- Register as AppStream components.

* Tue Jan 13 2015 Mike FABIAN <mfabian@redhat.com> - 1.3.7-1
- update to latest upstream 1.3.7
- Use F1,F2,F3,F4,F5,F6,F7,F8,F9 as select keys for the latex table
- Make rusle agree with http://ru.pc-history.com/wp-content/uploads/ok-keyboard_xt-at1.jpg

* Sat Nov 22 2014 Mike FABIAN <mfabian@redhat.com> - 1.3.6-1
- update to latest upstream 1.3.6
-  Fix typo in compose.txt

* Tue Sep 30 2014 Mike FABIAN <mfabian@redhat.com> - 1.3.5-1
- update to latest upstream 1.3.5
- Use better localized names for the rusle table

* Mon Sep 15 2014 Mike FABIAN <mfabian@redhat.com> - 1.3.4-1
- update to latest upstream 1.3.4
- Make status prompts and symbols more consistent

* Mon Sep 01 2014 Mike FABIAN <mfabian@redhat.com> - 1.3.3-1
- update to latest upstream 1.3.3
- Delete the RULES from the emoji-table
- Change MAX_KEY_LENGTH from 2 to 1 for the rusle, rustrad, thai,
  and yawerty tables

* Fri Jul 25 2014 Mike FABIAN <mfabian@redhat.com> - 1.3.2-1
- update to latest upstream 1.3.2
- Add “\circ ∘ U+2218 RING OPERATOR” back to the latex table
- Add Russian Legacy layout (by Stas Sergeev <stsp@users.sourceforge.net>)
- Resolves: rhbz#995838

* Wed Jul 23 2014 Mike FABIAN <mfabian@redhat.com> - 1.3.1-1
- update to latest upstream 1.3.1
- Add _ and ^ to the start characters for the LaTeX table
- Updates and bugfixes for the LaTeX table by
  Giuseppe Castagna (original author of the LaTeX table)

* Mon Jul 07 2014 Mike FABIAN <mfabian@redhat.com> - 1.3.0.20140707-1
- update to latest upstream 1.3.0.20140707
- Use SELECT_KEYS = F1,F2,F3,F4,F5,F6,F7,F8,F9 for ipa-x-sampa

* Wed Jun 25 2014 Mike FABIAN <mfabian@redhat.com> - 1.3.0.20140625-1
- update to latest upstream 1.3.0.20140625
- Add single and multi wildcard options to all tables

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0.20140603-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jun 03 2014 Mike FABIAN <mfabian@redhat.com> - 1.3.0.20140603-1
- update to latest upstream 1.3.0.20140603
- use AUTO_WILDCARD=TRUE for all tables, this option started working
  in ibus-table > 1.8.0

* Tue May 27 2014 Mike FABIAN <mfabian@redhat.com> - 1.3.0.20140512-2
- bump release number to build against updated ibus-table

* Mon May 12 2014 Mike FABIAN <mfabian@redhat.com> - 1.3.0.20140512-1
- update to latest upstream 1.3.0.20140512
- Don’t force “us” layout for cns11643, compose, ipa-x-sampa, viqr,
  emoji, mathwriter-ibus, translit-ua, and translit
- Keep forcing “us” layout only for “rustrad”, “yawerty”, and “thai”.
  But ibus does not use the option “KEYBOARD_LAYOUT”, the correct name
  of that option is just “LAYOUT”. Fix that for all tables.

* Mon May 05 2014 Mike FABIAN <mfabian@redhat.com> - 1.3.0.20140505-1
- update to latest upstream 1.3.0.20140505
- Don’t force “us” layout for the latex input method
- The “latex” table uses “\” as a startchar
- fix wrong weekday in rpm changelog

* Tue Feb 18 2014 Mike FABIAN <mfabian@redhat.com> - 1.3.0.20140218-1
- update to latest upstream 1.3.0.20140218
- includes "Set symbols to be displayed in IM switchers" by Sean Burke

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0.20130204-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 04 2013 Mike FABIAN <mfabian@redhat.com> - 1.3.0.20130204-1
- update to latest upstream 1.3.0.20130204
- Resolves: #907586 - 3 letter transliteration keys in translit.txt
  and translit-ua.txt in translit.txt and translit-ua.txt do not work
- remove fix-trailing-comments.patch (included upstream)

* Thu Sep 13 2012 Mike FABIAN <mfabian@redhat.com> - 1.3.0.20120912-2
- Resolves: #856948
- Trailing comments in tables should use ### instead of just #

* Wed Sep 12 2012 Mike FABIAN <mfabian@redhat.com> - 1.3.0.20120912-1
- update to latest upstream 1.3.0.20120912
- remove the patches already included upstream

* Mon Sep 10 2012 Mike FABIAN <mfabian@redhat.com> - 1.3.0.20100907-14
- Resolves: #855788
- Make the status prompts for Ukrainian and Russian unique
  (from Daniil Ivanov <daniil.ivanov@gmail.com>)
- Make icons for Ukrainian and Russian unique
  (from Daniil Ivanov <daniil.ivanov@gmail.com>)

* Thu Sep 06 2012 Mike FABIAN <mfabian@redhat.com> - 1.3.0.20100907-13
- Resolves: #855098
- Correct the filename of the ipa-x-sampa icon and replace it with a nicer
  .svg version.

* Thu Sep 06 2012 Mike FABIAN <mfabian@redhat.com> - 1.3.0.20100907-12
- Resolves: #855102
- Supported languages should not be left empty in a table.
  For an input method which has LANGUAGES set to an empty string,
  nothing at all is shown by ibus when trying to change to that input
  method using the trigger key which makes the input method hard to
  select.

* Thu Sep 06 2012 Mike FABIAN <mfabian@redhat.com> - 1.3.0.20100907-11
- Related: #845798, #854539
- enable build of Russian transliteration table again,
  should work now because of the fix for ibus-table, see #845798
- improvements for the Russian and Ukrainian transliteration tables
  translit.txt and translit-ua.txt by  the original author
  Daniil Ivanov <daniil.ivanov@gmail.com>

* Wed Aug 29 2012 Mike FABIAN <mfabian@redhat.com> - 1.3.0.20100907-10
- Fix build for emoji-table and enable it again.
- Resolves: #845797

* Sat Aug 04 2012 Parag Nemade <paragn AT fedoraproject DOT org> - 1.3.0.20100907-9
- Save this package for f18 by blocking emoji-table 

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0.20100907-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0.20100907-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0.20100907-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 19 2010 Naveen Kumar <nkumar@redhat.com> - 1.3.0.20100907-5
- dropped --disable-static & --prefix from configure
- Dropped the cleaning of buildroot
- macros removed from make
- clean section dropped
- doc moved to main package
- versions from BuildRequires and Requires removed

* Wed Oct 6 2010 Naveen Kumar <nkumar@redhat.com> - 1.3.0.20100907-4
- delete all Obsoletes fields in spec
- removed BuildRoot as specified in new guidelines

* Thu Sep 30 2010 Naveen Kumar <nkumar@redhat.com> - 1.3.0.20100907-3
- delete Provides fields in spec for main & sub packages
- added -n in spec file so that it looks like "package -n ibus-table*"
- added -n in spec file so that it looks like "files -n ibus-table*
- "Requires:  ibus-table >= 1.2.0.20090912" moved to all subpackages
- "files" section for main package removed
- used rm and make to macros "__make" and "__rm"

* Tue Sep 28 2010 Naveen Kumar <nkumar@redhat.com> - 1.3.0.20100907-2
- divided the package into subpackages.

* Tue Sep 7 2010 Naveen Kumar <nkumar@redhat.com> - 1.3.0.20100907-1
- Packaging for new version
- ibus-table-mathwriter included

* Fri May 28 2010 Caius 'kaio' Chance  <kaio at fedoraproject.org> - 1.3.0.20100528-1
- Included all non-Chinese tables.

* Wed Mar 10 2010 Caius 'kaio' Chance  <cchance at redhat.com> - 1.2.0.20100305-6
- Remove Conflicts, Provides, Obsoletes tag.

* Fri Mar 05 2010 Caius 'kaio' Chance  <cchance at redhat.com> - 1.2.0.20100305-5
- Fix source tag.

* Fri Mar 05 2010 Caius 'kaio' Chance  <cchance at redhat.com> - 1.2.0.20100305-4
- Fix source tag.

* Fri Mar 05 2010 Caius 'kaio' Chance  <cchance at redhat.com> - 1.2.0.20100305-3
- Fix BuildRequires tag to ibus-table-devel.

* Fri Mar 05 2010 Caius 'kaio' Chance  <cchance at redhat.com> - 1.2.0.20100305-2
- Modify index creation locations.

* Fri Mar 05 2010 Caius 'kaio' Chance  <cchance at redhat.com> - 1.2.0.20100305-1
- Upgrade source from upstream.

* Wed Jan 20 2010 Caius 'kaio' Chance  <k at kaio.me> - 1.2.0.20100120-1
- Introduce Emoji input method.
- Updated spec file.

* Fri Jan 08 2010 Caius 'kaio' Chance  <k at kaio.me> - 1.2.0.20100108-1
- The first version.
- Merged from ibus-table-additional.
