Name:       augeas-vala
Version:    0.10.0
Release:    17%{?dist}
Summary:    Vala bindings for augeas

License:    LGPLv2+
URL:        http://www.gitorious.org/valastuff/augeas-vala/
# Source: curl https://gitorious.org/valastuff/augeas-vala/archive-tarball/0.10.0-4 -o {source0}
Source0:    augeas-vala-%{version}-4.tar.gz
BuildArch:  noarch

BuildRequires:  autoconf automake
BuildRequires:  libtool
BuildRequires:  vala
BuildRequires:  glib2-devel
BuildRequires:  augeas-devel >= %{version}
# FIXME the following tortures rpmlint, maybe rpmlint needs to modified for this case:
Requires:       augeas-devel >= %{version}

%description
Vala bindings for augeas.

%prep
%setup -q -n valastuff-augeas-vala

%build
./bootstrap
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%check
make %{?_smp_mflags} check

%files
%doc COPYING.LIB README TODO NEWS AUTHORS
%{_datadir}/vala/vapi/augeas.deps
%{_datadir}/vala/vapi/augeas.vapi

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Oct 20 2012 - Fabian Deutsch <fabiand@fedoraproject.org> - 0.10.0-4
- Update license file
- Fix automake macros

* Fri Oct 12 2012 - Fabian Deutsch <fabiand@fedoraproject.org> - 0.10.0-3
- Add autoconf dependency

* Mon Oct 08 2012 - Fabian Deutsch <fabiand@fedoraproject.org> - 0.10.0-2
- Add glib2-devel dependency
- Use autotools
- Removed defattr from files
- Remove initial buildroot cleanup

* Wed Feb 22 2012 - Fabian Deutsch <fabiand@fedoraproject.org> - 0.10.0-1
- Initial version

