%global gem_name powerpack

Name:           rubygem-%{gem_name}
Version:        0.1.1
Release:        8%{?dist}
Summary:        A few useful extensions to core Ruby classes

License:        MIT
URL:            https://github.com/bbatsov/powerpack
# git clone git@github.com:bbatsov/powerpack.git
# cd powerpack && git checkout f7e2b9b7815e8fc202bd8874ed9376011af4a203
# gem build powerpack.gemspec
Source0:        %{gem_name}-%{version}.gem

BuildRequires:   rubygems-devel
BuildRequires:   rubygem(rspec)
BuildRequires:   rubygem(yard)

BuildArch:       noarch

%description
A few useful extensions to core Ruby classes.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

%check
rspec -Ilib spec

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%{gem_spec}
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/powerpack.gemspec
%exclude %{gem_instdir}/spec

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 13 2018 Ilya Gradina <ilya.gradina@gmail.com> - 0.1.1-4
- small fix in spec

* Fri Jul 28 2017 Ilya Gradina <ilya.gradina@gmail.com> - 0.1.1-3
- new version from commit(Fixing the tests and the definition of sum)

* Sat Sep 03 2016 Ilya Gradina <ilya.gradina@gmail.com> - 0.1.1-2
- changes in files

* Mon Oct 05 2015 Ilya Gradina <ilya.gradina@gmail.com> - 0.1.1-1
- Initial package
