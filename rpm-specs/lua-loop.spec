%define luaver 5.2
%define luapkgdir %{_datadir}/lua/%{luaver}

Name:           lua-loop
Version:        2.3
Release:        0.19.beta%{?dist}
Summary:        Class models for Lua

License:        MIT
URL:            http://loop.luaforge.net/
Source0:        http://luaforge.net/frs/download.php/3525/loop-2.3-beta.tar.gz

Requires:       lua >= %{luaver}

BuildArch:      noarch

%description
LOOP stands for Lua Object-Oriented Programming and is a set of
packages for supporting different models of object-oriented
programming in the Lua language.

LOOP models are mainly concerned with dynamicity, although there is an
attempt to keep them as simple and efficient as
possible. Additionally, LOOP uses fundamental Lua concepts like tables
(objects) and meta-tables (classes), traditionally used to enable an
object-oriented programming style, to provide a common ground for the
interoperability of objects and classes of its different models.


%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}

%description    doc
LOOP stands for Lua Object-Oriented Programming and is a set of
packages for supporting different models of object-oriented
programming in the Lua language.

This package contains documentation for %{name}.


%prep
%setup -q -n loop-%{version}-beta
chmod +x lua/*.lua
for f in doc/*.css; do
  touch -r $f timestamp.txt
  sed -i 's|\r||' $f
  touch -r timestamp.txt $f
done


%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{luapkgdir}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp -pr lua/loop $RPM_BUILD_ROOT%{luapkgdir}
cp -p lua/*.lua $RPM_BUILD_ROOT%{_bindir}




%files
%doc LICENSE RELEASE
%{_bindir}/*.lua
%{luapkgdir}/*

%files doc
%doc doc/*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-0.19.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-0.18.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-0.17.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-0.16.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-0.15.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-0.14.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-0.13.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-0.12.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-0.11.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-0.10.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-0.9.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-0.8.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 12 2013 Tom Callaway <spot@fedoraproject.org> - 2.3-0.7.beta
- rebuild for lua 5.2

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-0.6.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-0.5.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-0.4.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-0.3.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov  7 2010 Michel Salim <salimma@fedoraproject.org> - 2.3-0.2.beta
- Move scripts to %%{_bindir}
- Remove unneeded dependencies

* Thu Oct  1 2009 Michel Salim <salimma@fedoraproject.org> - 2.3-0.1.beta
- Initial package
