%{?nodejs_find_provides_and_requires}

%global commit 3aae5f7aa45906cfcb283817cfb6fcb15360391d
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           nodejs-ctype
Version:        0.5.3
Release:        17%{?dist}
Summary:        Read and write binary structures and data types with Node.js
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

License:        MIT
URL:            https://github.com/rmustacc/node-ctype
Source0:        https://registry.npmjs.org/ctype/-/ctype-%{version}.tgz
#grab the tests from github
Source1:        https://github.com/rmustacc/node-ctype/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

# fedora-specific patch to have README indicate proper directions for reading
# the man page from the system path
Patch1:         nodejs-ctype-README.patch

BuildRequires:  nodejs-packaging

%description
Node-CType is a way to read and write binary data in a structured and easy to 
use format. Its name comes from the C header file.

There are two APIs that you can use, depending on what abstraction you'd like.
The low level API lets you read and write individual integers and floats from
buffers. The higher level API lets you read and write structures of these.

%prep
%setup -q -n package -a1
%patch1 -p1

#move tests into regular directory
mv node-ctype-%{commit}/tst .
rm -rf node-ctype-%{commit}

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/ctype
cp -pr package.json ctf.js ctio.js ctype.js %{buildroot}%{nodejs_sitelib}/ctype

mkdir -p %{buildroot}%{_mandir}/man3
cp -pr man/man3ctype/ctio.3ctype %{buildroot}%{_mandir}/man3/ctio.3

%nodejs_symlink_deps

%check
pushd tst
for dir in ctf ctio/* ctype; do
    pushd $dir
    for f in *.js; do
        %{__nodejs} $f
    done
    popd
done
popd

%files
%{nodejs_sitelib}/ctype
%{_mandir}/man3/ctio.3.*
%doc CHANGELOG README README.old
%license LICENSE

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-17
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 07 2016 Piotr Popieluch <piotr1212@gmail.com> - 0.5.3-8
- cleanup spec

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.5.3-3
- restrict to compatible arches

* Fri Jun 21 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.5.3-2
- fix spelling in description

* Thu Jun 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.5.3-1
- initial package
