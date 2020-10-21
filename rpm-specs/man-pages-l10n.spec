%global upstream_name manpages-l10n

%global translations \
    de:    "German" \
    fr:    "French" \
    nl:    "Dutch" \
    pl:    "Polish" \
    pt_BR: "Portuguese (Brazil)" \
    ro:    "Romanian"

Name:           man-pages-l10n
Version:        4.2.0
Release:        1%{?dist}
Summary:        Translated man pages from the Linux Documentation Project and other software projects

# original man pages are under various licenses, translations are GPLv3+
# generated from upstream/fedora-rawhide/packages.txt with:
#   dnf --disablerepo=* --enablerepo=rawhide repoquery --queryformat "%%{license}" $(<upstream/fedora-rawhide/packages.txt) |\
#   sed 's/) and (/)\n(/g;s/) and /)\n/g;s/ and (/\n(/g' |\
#   sed '/^(/!s/\(.* or .*\)/(\1)/' |\
#   sed '/^(/!s/ and /\n/g' |\
#   (echo GPLv3+ && cat) |\
#   sort -u
License:        Artistic Licence 2.0 and BSD and BSD with advertising and Copyright only and GFDL and GPL+ and GPLv2 and GPLv2+ and (GPLv2+ or Artistic) and GPLv2 with exceptions and GPLv2+ with exceptions and GPLv3+ and (GPLv3+ and BSD) and (GPLv3+ or BSD) and IEEE and IJG and ISC and LGPLv2+ and LGPLv3+ and (LGPLv3+ or BSD) and MIT and psutils and Public Domain and Sendmail and Verbatim

URL:            https://manpages-l10n-team.pages.debian.net/manpages-l10n/
Source0:        https://salsa.debian.org/manpages-l10n-team/%{upstream_name}/-/archive/v%{version}/%{upstream_name}-v%{version}.tar.bz2

BuildArch:      noarch

BuildRequires:  po4a


%description
Translated man pages from the Linux Documentation Project
and other software projects.


# generate subpackages
%{lua: for code, name in rpm.expand('%{translations}'):gmatch('(%S+):%s+(%b"")') do
    name = name:gsub('"', '')

    print('%package -n man-pages-' .. code .. '\n')
    print('Summary: ' .. name .. ' man pages from the Linux Documentation Project\n')
    print('Requires: man-pages-reader\n')
    print('Supplements: (man-pages and langpacks-' .. code .. ')\n')

    print('%description -n man-pages-' .. code .. '\n')
    print('Manual pages from the Linux Documentation Project, translated into ' .. name .. '.\n')
end}


%prep
%autosetup -p1 -n %{upstream_name}-v%{version}


%build
%configure --enable-distribution=fedora-rawhide
%make_build


%install
%make_install

# generate %files sections
%{lua: for code in rpm.expand('%{translations}'):gmatch('(%S+):%s+%b""') do
    print('%files -n man-pages-' .. code .. '\n')
    print('%license LICENSE COPYRIGHT.md\n')
    print('%doc AUTHORS.md CHANGES.md README.md\n')
    print(rpm.expand('%{_mandir}') .. '/' .. code .. '/man*/*\n')

    -- handle .(1) man page in man-pages-fr and man-pages-pl
    if code == 'fr' or code == 'pl' then
        print(rpm.expand('%{_mandir}') .. '/' .. code .. '/man*/..1*\n')
    end
end}


%changelog
* Thu Oct 15 2020 Rafael Fontenelle <rafaelff@gnome.org> - 4.2.0-1
- Update to version 4.2.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 03 2020 Nikola Forró <nforro@redhat.com> - 4.1.0-1
- Update to version 4.1.0
  resolves: #1852799

* Sun Mar 22 2020 Nikola Forró <nforro@redhat.com> - 4.0.0-1.20200322gitbff338d
- Remove man pages provided by xz-5.2.5
- Update to the latest commit

* Wed Mar 18 2020 Nikola Forró <nforro@redhat.com> - 4.0.0-1.20200318gite5c0d56
- Fix summary and description
- Update to the latest commit

* Tue Mar 17 2020 Nikola Forró <nforro@redhat.com> - 4.0.0-1.20200317gitb4ac9e9
- Initial package
