# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

%global enable_tests 1
%global srcname elasticdump

Name:           %{srcname}
Version:        2.2.0
Release:        10%{?dist}
Summary:        Import and export tools for elasticsearch
License:        ASL 2.0
URL:            https://github.com/taskrabbit/elasticsearch-dump
Source0:        https://registry.npmjs.org/%{srcname}/-/%{srcname}-%{version}.tgz
Source10:       elasticdump.1

BuildArch:      noarch

%if 0%{?rhel} && 0%{?rhel} < 7
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch
%else
ExclusiveArch:  %{nodejs_arches} noarch
%endif

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(line-reader)
BuildRequires:  npm(mocha)
BuildRequires:  npm(request)
BuildRequires:  npm(should)
%endif


%description
%{summary}.


%prep
%setup -q -n package
chmod 644 lib/transports/elasticsearch.js

%nodejs_fixdep JSONStream
%nodejs_fixdep async '<2'

sed -i '1s|#!/usr/bin/env node.*|#!/usr/bin/node|' bin/multielasticdump
sed -i '1s|#!/usr/bin/env node.*|#!/usr/bin/node|' bin/elasticdump


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{srcname}
cp -pr package.json elasticdump.js bin/ lib/ \
    %{buildroot}%{nodejs_sitelib}/%{srcname}

mkdir -p %{buildroot}%{_bindir}
ln -s %{nodejs_sitelib}/%{srcname}/bin/elasticdump \
    %{buildroot}%{_bindir}/elasticdump
ln -s %{nodejs_sitelib}/%{srcname}/bin/multielasticdump \
    %{buildroot}%{_bindir}/multielasticdump

%nodejs_symlink_deps

install -D -p -m0644 %{SOURCE10} %{buildroot}%{_mandir}/man1/elasticdump.1

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
# don't run tests which require an elasticsearch instance
mocha -i -g 'ELASTICDUMP|parent child'
%endif


%files
%doc README.md
%license LICENSE.txt
%{nodejs_sitelib}/%{srcname}
%{_bindir}/elasticdump
%{_bindir}/multielasticdump
%{_mandir}/man1/elasticdump.1*


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 21 2017 Piotr Popieluch <piotr1212@gmail.com> - 2.2.0-2
- Fixdep async for all working versions (needed for epel)
- Add node require check
- Set correct interpreter in scripts

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 09 2016 Piotr Popieluch <piotr1212@gmail.com> - - 2.2.0-1
- Update to 2.2.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 19 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.16.1-1
- Update to 0.16.1

* Sun Sep 27 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.16.0-1
- Update to 0.16.0

* Tue Sep 22 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.15.0-1
- Update to 0.15.0

* Thu Sep 03 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.14.6-1
- Update to 0.14.16

* Fri Aug 28 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.14.4-1
- Update to 0.14.14

* Mon Aug 24 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.14.3-2
- Add el6 support

* Sat Aug 15 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.14.3-1
- Update to 0.14.3

* Sun Aug 02 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.14.2-1
- Update to 0.14.2

* Fri Jul 24 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.14.1-1
- Update to 0.14.1

* Sat Jun 13 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.13.1-1
- Initial package
