Name:           powwow
Version:        1.2.21
Release:        3%{?dist}
Summary:        A console MUD client

License:        GPLv2+
URL:            http://hoopajoo.net/projects/powwow.html
Source:         http://hoopajoo.net/static/projects/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  ncurses-devel
BuildRequires:  pcre-devel

%description
Powwow is a powerful console MUD client that supports triggers, aliases,
multiple connections, and more. It is primarily designed for DikuMUDs, but
nothing prevents its use for other types of MUDs. This client is also
extensible through a plugin interface.


%package devel
Summary:        Development files for powwow
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The powwow-devel package contains the headers files and developer docs
for developing applications which use powwow plugin interface.


%prep
%setup -q

# Convert to utf-8
for file in README doc/powwow.doc; do
    mv $file timestamp
    iconv -f ISO-8859-1 -t UTF-8 -o $file timestamp
    touch -r timestamp $file
done


%build
%configure
%make_build


%install
%make_install

# Remove the documentation here. We install it with %doc instead to
# the standard directory.
rm -f $RPM_BUILD_ROOT%{_datadir}/powwow/powwow.doc


%files
%license COPYING
%doc ChangeLog doc/Config.demo doc/powwow.doc README
%{_datadir}/powwow/
%{_bindir}/*
%{_mandir}/man6/*

%files devel
%{_includedir}/powwow/


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 02 2020 Kalev Lember <klember@redhat.com> - 1.2.21-1
- Update to 1.2.21
- Switch to pcre for regular expression support

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 23 2019 Kalev Lember <klember@redhat.com> - 1.2.20-1
- Update to 1.2.20

* Fri Apr 26 2019 Kalev Lember <klember@redhat.com> - 1.2.19-1
- Update to 1.2.19

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 13 2018 Kalev Lember <klember@redhat.com> - 1.2.18-1
- Update to 1.2.18
- Tighten -devel subpackage deps
- Use make_build and make_install macros

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Kalev Lember <kalevlember@gmail.com> - 1.2.17-1
- Update to 1.2.17

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep 01 2009 Kalev Lember <kalev@smartlink.ee> - 1.2.16-1
- Update to powwow 1.2.16.
- Dropped upstreamed powwow-long-prompt.patch.
- Added a plugin example to -devel docs.

* Fri Aug 07 2009 Kalev Lember <kalev@smartlink.ee> - 1.2.15-4
- Update powwow-long-prompt.patch to the version sent upstream.

* Fri Aug 07 2009 Kalev Lember <kalev@smartlink.ee> - 1.2.15-3
- Apply patch to match prompts longer than terminal width (#509288).

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 02 2009 Kalev Lember <kalev@smartlink.ee> - 1.2.15-1
- Update to powwow 1.2.15.

* Mon Apr 20 2009 Kalev Lember <kalev@smartlink.ee> - 1.2.14-3
- Rework powwow-devel description.
- Rename movie_play and muc, remove catrw and follow to avoid
  possible name clashes and to reflect upstream changes.

* Thu Apr 16 2009 Kalev Lember <kalev@smartlink.ee> - 1.2.14-2
- Remove COPYING from %%doc, because it is needed at runtime.

* Wed Apr 15 2009 Kalev Lember <kalev@smartlink.ee> - 1.2.14-1
- Update to powwow 1.2.14.

* Wed Mar 25 2009 Kalev Lember <kalev@smartlink.ee> - 1.2.13-2
- Fix the package to own all the directories it creates.
- Move development-related docs to devel subpackage.

* Sun Mar 22 2009 Kalev Lember <kalev@smartlink.ee> - 1.2.13-1
- Initial RPM release.
