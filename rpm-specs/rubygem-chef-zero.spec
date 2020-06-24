# Generated from chef-zero-2.0.2.gem by gem2rpm -*- rpm-spec -*-

%global gem_name chef-zero

Name: rubygem-%{gem_name}
Version: 2.2
Release: 10%{?dist}
Summary: Self-contained in-memory Chef server for testing and solo setup purposes
License: ASL 2.0
URL: https://github.com/opscode/chef-zero
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
%{!?el6:Requires: ruby(release)}
Requires: ruby(rubygems)
Requires: rubygem(mixlib-log)
Requires: rubygem(hashie)
Requires: rubygem(json)
Requires: rubygem(rack)
%{!?el6:BuildRequires: ruby(release)}
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rack)
BuildRequires: rubygem(mixlib-log)
BuildRequires: rubygem(hashie)
%{!?el6:BuildRequires: rubygem(rspec)}
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Self-contained, easy-setup, fast-start in-memory Chef server for testing and
solo setup purposes.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
%if %{?el6}0
# spec is too old; need RSpec2
%else
pushd .%{gem_instdir}
rspec
popd
%endif

%files
%dir %{gem_instdir}
%{_bindir}/chef-zero
%{gem_instdir}/bin
%doc %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/spec
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/Rakefile

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 21 2014 Julian C. Dunn <jdunn@aquezada.com> - 2.2-2
- Update to 2.2 (bz#1111886)

* Fri Jun 06 2014 Julian C. Dunn <jdunn@aquezada.com> - 2.1.5-2
- Fix build on EL6

* Thu Jun 05 2014 Julian C. Dunn <jdunn@aquezada.com> - 2.1.5-1
- Update to 2.1.5

* Thu Mar 20 2014 Julian C. Dunn <jdunn@aquezada.com> - 2.0.2-1
- Initial package
