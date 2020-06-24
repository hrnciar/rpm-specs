# Generated from sprockets-2.4.5.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sprockets

Name: rubygem-%{gem_name}
Version: 3.7.2
Release: 5%{?dist}
Summary: Rack-based asset packaging system
License: MIT
URL: https://github.com/rails/sprockets
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# to get tests:
# git clone https://github.com/rails/sprockets.git && cd sprockets/
# git checkout v3.7.2 && tar czf sprockets-3.7.2-tests.tgz test/
Source1: sprockets-%{version}-tests.tgz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.9.3
BuildRequires: rubygem(concurrent-ruby)
BuildRequires: rubygem(coffee-script)
BuildRequires: rubygem(ejs)
BuildRequires: rubygem(execjs)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(nokogiri)
BuildRequires: rubygem(rack-test)
BuildRequires: rubygem(rake)
BuildRequires: rubygem(sass)
BuildRequires: rubygem(uglifier)
BuildRequires: help2man
BuildRequires: %{_bindir}/node
BuildArch: noarch

%description
Sprockets is a Rack-based asset packaging system that concatenates and serves
JavaScript, CoffeeScript, CSS, LESS, Sass, and SCSS.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -c -T
%gem_install -n %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Turn `sprockets --help` into man page
export GEM_PATH="%{buildroot}/%{gem_dir}:%{gem_dir}"
mkdir -p %{buildroot}%{_mandir}/man1
help2man --no-discard-stderr -N -s1 -o %{buildroot}%{_mandir}/man1/%{gem_name}.1 \
    %{buildroot}/usr/share/gems/gems/%{gem_name}-%{version}/bin/%{gem_name}

# Run the test suite
%check
pushd .%{gem_instdir}
tar xzf %{SOURCE1}

# We don't enable rubygem(closure-compiler).
# https://bugzilla.redhat.com/show_bug.cgi?id=1353473
mv test/test_closure_compressor.rb{,.disabled}
mv lib/sprockets/autoload/closure.rb{,.disabled}
sed -i '/:Closure/ s/^/#/' lib/sprockets/autoload.rb

# We don't have rubygem(eco) yet.
mv test/test_eco_processor.rb{,.disabled}
mv lib/sprockets/autoload/eco.rb{,.disabled}
sed -i '/:Eco/ s/^/#/' lib/sprockets/autoload.rb
sed -i '/test "eco templates" do/,/^  end/ s/^/#/' test/test_environment.rb

# We don't have rubygem(yui-compressor) yet.
# https://bugzilla.redhat.com/show_bug.cgi?id=725768
mv test/test_yui_compressor.rb{,.disabled}
mv lib/sprockets/autoload/yui.rb{,.disabled}
sed -i '/:YUI/ s/^/#/' lib/sprockets/autoload.rb

# Required by TestPathUtils#test_find_upwards test.
touch Gemfile

RUBYOPT=-Ilib:test ruby -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{_bindir}/sprockets
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%{_mandir}/man1/%{gem_name}.1*

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 pvalena <pvalena@redhat.com> - 3.7.2-1
- Update to sprockets 3.7.2.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 05 2017 Vít Ondruch <vondruch@redhat.com> - 3.7.1-1
- Update to Sprockets 3.7.1.

* Mon Aug 15 2016 Vít Ondruch <vondruch@redhat.com> - 3.7.0-1
- Update to Sprockets 3.7.0.

* Mon Jul 04 2016 Jun Aruga <jaruga@redhat.com> - 3.6.3-1
- Fix a JavaScript runtime issue. (rhbz#1352650)
- Update to Sprockets 3.6.3.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Vít Ondruch <vondruch@redhat.com> - 3.2.0-1
- Update to Sprockets 3.2.0.

* Tue Nov 18 2014 Josef Stribny <jstribny@redhat.com> - 2.12.3-1
- Update to 2.12.3

* Mon Aug 18 2014 Josef Strzibny <jstribny@redhat.com> - 2.12.1-3
- Fix FTBFS: ExecJS changed the exception names

* Thu Jun 19 2014 Vít Ondruch <vondruch@redhat.com> - 2.12.1-2
- Filter tilt requires.

* Thu Jun 19 2014 Vít Ondruch <vondruch@redhat.com> - 2.12.1-1
- Update to sprockets 2.12.1.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 08 2013 Vít Ondruch <vondruch@redhat.com> - 2.8.2-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 11 2012 Josef Stribny <jstribny@redhat.com> - 2.8.2-1
- Upgraded to version 2.8.2
- Added rubygem-uglifier build dependency

* Wed Jul 18 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.4.5-1
- Initial package
