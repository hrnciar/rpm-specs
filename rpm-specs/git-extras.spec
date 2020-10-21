Name:       git-extras
Version:    6.1.0
Release:    1%{?dist}
Summary:    Little git extras

License:    MIT
URL:        https://github.com/tj/%{name}
Source0:    %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:  noarch

BuildRequires: sed
Requires:   git

%description
%{name} adds the following extra-commands to git:

alias, archive-file, bug, changelog, commits-since, contrib, count,
create-branch, delete-branch, delete-submodule, delete-tag, effort,
extras, feature, fresh-branch, gh-pages, graft, ignore, info,
local-commits, obliterate, promote, refactor, release, repl, setup,
squash, summary, touch, undo

For more information about the extra-commands, see the included
README.md, HTML, mark-down or man-pages.


%prep
%setup -q
# scripts already use bash
# remove `/usr/bin/env` from hashbang
sed -i -e "s#/usr/bin/.*sh#/bin/bash#g" \
    bin/*

#Disable self-update feature
cat << EOF > bin/git-extras
#!/bin/sh
echo "Self-update feature disabled by maintainer."
EOF


%build


%install
%make_install PREFIX=%{_prefix} SYSCONFDIR=%{_sysconfdir}
mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d \
    html md
install -pm 0644 man/*.html html
install -pm 0644 man/*.md md


%files
%config(noreplace) %{_sysconfdir}/bash_completion.d
%doc AUTHORS Commands.md History.md Readme.md html/ md/
%license LICENSE
%{_bindir}/*
%{_mandir}/man*/*


%changelog
* Mon Sep 28 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 6.1.0-1
- Update to 6.1.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 6.0.0-1
- Update to 6.0.0 (#1849487)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 23 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 5.1.0-1
- Update to 5.1.0

* Fri Sep 06 2019 Sérgio Basto <sergio@serjux.com> - 5.0.0-1
- Update to 5.0.0 (#1742787)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 15 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 4.7.0-1
- Update to 4.7.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 19 2018 Sérgio Basto <sergio@serjux.com> - 4.6.0-4
- Not Requires bash-completion, because is not required, people may want not
  install it.
- Clean sed regular expression and add it to BuildRequires.

* Tue Sep 11 2018 Björn Esser <besser82@fedoraproject.org> - 4.6.0-3
- Use POSIX shell instead of '(/usr)/bin/bash'

* Tue Sep 11 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 4.6.0-2
- Correct shebang

* Fri Sep 07 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 4.6.0-1
- Update to 4.6.0
- Disable self-update feature

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 15 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 4.4.0-1
- Update to 4.4.0 (#1471372)

* Fri May 05 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 4.3.0-1
- Update to 4.3.0 (#1448429)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 20 2016 Sérgio Basto <sergio@serjux.com> - 4.2.0-3
- Don't need run ./manning-up.sh was already done by upstream.

* Sat Nov 19 2016 Sérgio Basto <sergio@serjux.com> - 4.2.0-2
- Add Commands.md to documentation (#1396467)

* Tue Oct 11 2016 Sérgio Basto <sergio@serjux.com> - 4.2.0-1
- Update to 4.2.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 4.1.0-1
- Update to 4.1.0 (#1301413)

* Sat Jan 16 2016 Sérgio Basto <sergio@serjux.com> - 4.0.0-1
- Update git-extras to 4.0.0 (#1294644)
- Create unowned directory bash_completion.d and fix make install.
- New upstream source URL.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 16 2015 Sérgio Basto <sergio@serjux.com> - 2.2.0-3
- Readded troublesome URLs solution from
  https://fedoraproject.org/wiki/Packaging:SourceURL#Troublesome_URLs

* Mon Jun 15 2015 Sérgio Basto <sergio@serjux.com> - 2.2.0-2
- Added License tag

* Mon Jun 15 2015 Sérgio Basto <sergio@serjux.com> - 2.2.0-1
- Update to 2.2.0 .
- Drop git-extras-1.9.0_fixes.patch .

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 20 2013 Björn Esser <bjoern.esser@gmail.com> - 1.9.0-1
- new upstream-version

* Mon Jun 10 2013 Björn Esser <bjoern.esser@gmail.com> - 1.8.0-3
- nuked `BuildRequires: groff-base`; gets pulled by rubygem-ronn

* Fri Jun 07 2013 Björn Esser <bjoern.esser@gmail.com> - 1.8.0-2
- added missing %%{version} in Source0
- added missing %%{name} in `install etc/bash_completion.sh`-line

* Mon Jun 03 2013 Björn Esser <bjoern.esser@gmail.com> - 1.8.0-1
- Initial rpm release
