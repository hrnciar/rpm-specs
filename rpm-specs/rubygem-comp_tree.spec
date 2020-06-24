%global gem_name comp_tree

Name:           rubygem-%{gem_name}
Version:        1.1.3
Release:        12%{?dist}
Summary:        A simple framework for automatic parallelism

License:        MIT
URL:            http://quix.github.io/comp_tree/
Source0:        http://rubygems.org/downloads/%{gem_name}-%{version}.gem
# https://github.com/quix/comp_tree/pull/1
Patch1:         0001-Make-it-work-with-Minitest-5.patch
Patch2:         0002-Make-tests-work-with-Rake-10.patch
Patch3:         0003-Fix-throw_test-test.patch
Patch4:         0004-Fix-run-with-Minitest-5.patch
BuildArch:      noarch

BuildRequires:  rubygems-devel
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(rake)
Requires:       ruby(release) >= 1.8
Requires:       rubygems
Provides:       rubygem(%{gem_name}) = %{version}-%{release}

%description
CompTree is a parallel computation tree structure based upon concepts from
pure functional programming.


%package doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}

%description doc
Documentation for %{name}


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
gem spec %{SOURCE0} -l --ruby >%{gem_name}.gemspec


%build
gem build %{gem_name}.gemspec
%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/


%check
rake test


%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/devel
%exclude %{gem_cache}
%exclude %{gem_instdir}/*.rdoc
%exclude %{gem_instdir}/test
%exclude %{gem_instdir}/Rakefile
%{gem_spec}
%doc *.rdoc


%files doc
%{gem_docdir}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 12 2014 Lubomir Rintel <lkundrak@v3.sk> - 1.1.3-2
- Fix test run

* Mon Apr 28 2014 Lubomir Rintel <lkundrak@v3.sk> - 1.1.3-1
- Initial packaging
