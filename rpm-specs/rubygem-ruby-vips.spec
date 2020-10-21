# Generated from ruby-vips-2.0.17.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ruby-vips

Name: rubygem-%{gem_name}
Version: 2.0.17
Release: 1%{?dist}
Summary: Ruby extension for the vips image processing library
License: MIT
URL: http://github.com/libvips/ruby-vips
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Tests are not shipped with the gem, you may check them out like so:
# git clone --no-checkout http://github.com/libvips/ruby-vips
# cd ruby-vips && git archive -v -o ruby-vips-2.0.17-spec.txz v2.0.17 spec/
Source1: %{gem_name}-%{version}-spec.txz

Requires: (libvips.so.42()(64bit) if libffi.so.6()(64bit))
Requires: (libvips.so.42 if libffi.so.6)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec) >= 3.3
BuildRequires: rubygem(ffi)
BuildRequires: (libvips.so.42()(64bit) if libffi.so.6()(64bit))
BuildRequires: (libvips.so.42 if libffi.so.6)
BuildArch: noarch

%description
ruby-vips is a binding for the vips image processing library. It is fast and
it can process large images without loading the whole image in memory.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b1

# Do not use `env` in shebangs
# https://github.com/libvips/ruby-vips/pull/245
sed -i 's|/usr/bin/env ruby|/usr/bin/ruby|' example/thumb.rb
sed -i 's|/usr/bin/env ruby|/usr/bin/ruby|' example/example1.rb

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
ln -s %{_builddir}/spec .
rspec spec
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec
%doc %{gem_instdir}/TODO
%{gem_instdir}/VERSION
%{gem_instdir}/example
%{gem_instdir}/install-vips.sh

%changelog
* Wed Aug 12 2020 Pavel Valena <pvalena@redhat.com> - 2.0.17-1
- Initial package
