Name:       timew
Version:    1.3.0
Release:    1%{?dist}
Summary:    Timewarrior tracks and reports time

License:    MIT
URL:        https://timewarrior.net/
# Do not use github tag archives
# They do not contain the libshared git submodule
Source0:    https://github.com/GothenburgBitFactory/timewarrior/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:    README.Fedora

BuildRequires:  cmake gcc-c++

%description
Timewarrior is a time tracking utility that offers simple stopwatch features as
well as sophisticated calendar-base backfill, along with flexible reporting. It
is a portable, well supported and very active, Open Source project.

Please read the /usr/share/doc/timew/README.Fedora file on using the included
extensions.

%prep
%autosetup
mkdir %{_target_platform}
cp -v %{SOURCE1} .
chmod -x ext/*.py doc/holidays/*
for lib in ext/* doc/holidays/*; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done



%build
pushd %{_target_platform}
    %cmake ..
popd
%make_build -C %{_target_platform}


%install
%make_install -C %{_target_platform}
# Theme goes to datadir
mv -v $RPM_BUILD_ROOT/%{_docdir}/%{name}/doc $RPM_BUILD_ROOT/%{_datadir}/%{name}

# Not needed
rm -f $RPM_BUILD_ROOT/%{_docdir}/%{name}/INSTALL
# same as license
rm -f $RPM_BUILD_ROOT/%{_docdir}/%{name}/COPYING

# Install Fedora readme file
mv -v README.Fedora $RPM_BUILD_ROOT/%{_docdir}/%{name}/

# The tarball doesn't contain the tests

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}*
%{_mandir}/man7/%{name}*
%{_docdir}/%{name}

%changelog
* Tue Apr 21 2020 Aniket Pradhan <major AT fedoraproject DOT org> - 1.3.0-1
- Version update to 1.3.0

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.2.0-1
- Update to 1.2.0

* Tue Oct 01 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.1.1-5
- Add Readme: https://bugzilla.redhat.com/show_bug.cgi?id=1631025

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 05 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.1.1-1
- Update to latest upstream release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 03 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.0.0-3
- Add missing buildrequires

* Wed Dec 07 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.0.0-2
- Put files in the right place

* Wed Dec 07 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.0.0-1
- Initial rpmbuild
