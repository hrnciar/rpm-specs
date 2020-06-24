%global	gem_name	domain_name
%global	rubyabi	1.9.1

Summary:	Domain Name manipulation library for Ruby
Name:		rubygem-%{gem_name}
Version:	0.5.20190701
Release:	2%{?dist}

# See LICENSE.txt
# data/effective_tld_names.dat is not included in binary rpm
License:	BSD and (MPLv1.1 or GPLv2+ or LGPLv2+)
URL:		https://github.com/knu/ruby-domain_name
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:	ruby(release)
BuildRequires:	ruby(release)

Requires:	ruby(rubygems) 
Requires:	rubygem(unf)
BuildRequires:	rubygems-devel 
# %%check
BuildRequires:	rubygem(test-unit)
BuildRequires:	rubygem(unf)
BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}-%{release}

%description
This is a Domain Name manipulation library for Ruby.
It can also be used for cookie domain validation based on the Public
Suffix List.


%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	doc
Documentation for %{name}

%prep
%setup -q -c -T

TOPDIR=$(pwd)
mkdir tmpunpackdir
pushd tmpunpackdir

gem unpack %{SOURCE0}
cd %{gem_name}-%{version}

gem specification -l --ruby %{SOURCE0} > %{gem_name}.gemspec
gem build %{gem_name}.gemspec
mv %{gem_name}-%{version}.gem $TOPDIR

popd
rm -rf tmpunpackdir

%build
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

# Clean up
rm -f %{buildroot}%{gem_instdir}/{.document,.gitignore}

%check
pushd .%{gem_instdir}
sed -i.orig \
	-e '/begin/,/end/d' \
	-e '/bundler/d' \
	test/helper.rb

for f in test/test_*.rb
do
	ruby -Ilib:test:. $f
done
popd


%files
%dir	%{gem_instdir}
%doc	%{gem_instdir}/[A-Z]*
%exclude	%{gem_instdir}/Gemfile*
%exclude	%{gem_instdir}/Rakefile
%exclude	%{gem_instdir}/*.gemspec
%exclude	%{gem_instdir}/.travis.yml

%{gem_libdir}
%exclude	%{gem_cache}
%{gem_spec}

%files doc
%doc	%{gem_docdir}
%exclude	%{gem_instdir}/test/
%exclude	%{gem_instdir}/tool/
%exclude	%{gem_instdir}/data/

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.20190701-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 31 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.20190701-1
- 0.5.20190701

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.20180417-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.20180417-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.20180417-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 30 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.20180417-1
- 0.5.20180417

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.20170404-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.20170404-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May  5 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.20170404-1
- 0.5.20170404

* Tue Mar 14 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.20170223-1
- 0.5.20170223

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.20161129-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 31 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.20161129-1
- 0.5.20161129

* Fri Nov 18 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.20161021-1
- 0.5.20161021

* Sat Sep 10 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.20160826-1
- 0.5.20160826

* Thu Jun 30 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.20160615-1
- 0.5.20160615

* Mon Mar 28 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.20160310-1
- 0.5.20160310

* Mon Mar 14 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.20160309-1
- 0.5.20160309

* Wed Mar  9 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.20160216-1
- 0.5.20160216

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.20160128-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb  1 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.20160128-1
- 0.5.20160128

* Thu Oct  8 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.25-1
- 0.5.25

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 17 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.24-1
- 0.5.24

* Sun Dec 21 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.23-1
- 0.5.23

* Tue Nov  4 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.22-1
- 0.5.22

* Wed Sep 10 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.21-1
- 0.5.21

* Sun Aug 31 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.20-1
- 0.5.20

* Fri Jun 27 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.19-1
- 0.5.19

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 08 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.18-2
- Support Minitest 5+

* Mon Apr 07 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.18-1
- 0.5.18

* Sat Feb 15 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.16-1
- 0.5.16

* Tue Nov 19 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.15-1
- 0.5.15

* Tue Oct 22 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.14-1
- 0.5.14

* Fri Oct 11 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.13-2
- Remove redundant BR

* Tue Oct  8 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.13-1
- 0.5.13

* Mon Apr 29 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.11-1
- 0.5.11

* Fri Mar 22 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.9-1
- 0.5.9

* Sun Jan 27 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.7-2
- A bit clean up

* Sun Jan 27 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.7-1
- Initial package
