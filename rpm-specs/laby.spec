%global shortcommit 27ecf89
%global commit 27ecf893d093ad88d92ac84fbfc40671cdee0dec
%global snapinfo 20200413git%{shortcommit}

Name:           laby
Version:        0.6.4
Release:        18.%{snapinfo}%{?dist}
Summary:        Learn programming, playing with ants and spider webs

License:        GPLv3+
URL:            https://sgimenez.github.io/laby/
Source0:        https://github.com/sgimenez/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-lablgtk-devel >= 2.14.0
BuildRequires:  ocaml-ocamldoc
BuildRequires:  chrpath
BuildRequires:  gtksourceview2-devel >= 2.10
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  ocaml-ocamlbuild

# Note: rpmlint suggest to add
# BuildRequires: python2-devel
# or
# BuildRequires: python3-devel
# but they're not used during the build so they've not been added.

%description
Laby is a small program to learn how to program with ants and spider webs.
You have to move an ant out of a labyrinth, avoid spider webs, move rocks, etc.


%prep
%setup -q -n %{name}-%{commit}

%build
make %{?_smp_mflags} native

%install
export DESTDIR=%{buildroot}
make install

appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop


%files
%license COPYRIGHT
%license gpl-3.0.txt
%doc AUTHORS
%{_bindir}/%{name}
%{_datadir}/%{name}/

# Note above contains also:
# /usr/share/laby/mods/c/lib/robot.h
# /usr/share/laby/mods/cpp/lib/robot.h
# Which rpmlint suggest to have in -devel subpackage.
# This is intentional. The game teach you also how to program in C and in order
# to move the ant, you'll need the robot.h header file. It isn't the use case
# addressed by -devel subpackages.

%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg


%changelog
* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 0.6.4-18.20200413git27ecf89
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.6.4-17.20200413git27ecf89
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 17 2020 Richard W.M. Jones <rjones@redhat.com> - 0.6.4-16.20200413git27ecf89
- OCaml 4.11.0 pre-release

* Mon Apr 13 2020 Sandro Bonazzola <sandro.bonazzola@gmail.com> - 0.6.4-15.20200413git27ecf89
- switch to github snapshot

* Thu Apr 02 2020 Richard W.M. Jones <rjones@redhat.com> - 0.6.4-14
- Update all OCaml dependencies for RPM 4.16.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 18 2018 Sandro Bonazzola <sandro.bonazzola@gmail.com> - 0.6.4-9
- Workaround unsafe-string change in ocam 4.06
  Resolves: BZ#1556013

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.4-7
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun May 21 2017 Sandro Bonazzola <sandro.bonazzola@gmail.com> - 0.6.4-4
- Addressed comment #10 from rhbz#1450679

* Fri May 19 2017 Sandro Bonazzola <sandro.bonazzola@gmail.com> - 0.6.4-3
- Addressed comments #3-7 from rhbz#1450679

* Tue May 16 2017 Sandro Bonazzola <sandro.bonazzola@gmail.com> - 0.6.4-2
- Add Fedora >= 26 support

* Sun May 14 2017 Sandro Bonazzola <sandro.bonazzola@gmail.com> - 0.6.4-1
- Initial packaging
