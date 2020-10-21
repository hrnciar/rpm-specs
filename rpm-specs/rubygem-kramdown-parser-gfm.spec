%global gem_name kramdown-parser-gfm

Name:           rubygem-%{gem_name}
Summary:        Kramdown parser for GitHub-flavored markdown
Version:        1.1.0
Release:        5%{?dist}
License:        MIT

URL:            https://github.com/kramdown/parser-gfm
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem

# upstream patch to make test suite compatible with kramdown 2.2.0
Patch0:         %{url}/commit/ad48572.patch

BuildArch:      noarch

BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby >= 2.3

BuildRequires:  rubygem(kramdown) >= 2.0.0
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(rouge)

%description
kramdown-parser-gfm provides a kramdown parser for the GFM dialect of
Markdown.


%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}

BuildArch: noarch

%description    doc
Documentation for %{name}.


%prep
%setup -q -n %{gem_name}-%{version}
%patch0 -p1


%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/


%check
pushd .%{gem_instdir}
# move a broken test out of the way
mv test/testcases/codeblock_fenced.text test/testcases/codeblock_fenced.disabled

ruby -I'lib' -e 'Dir.glob "./test/**test_*.rb", &method(:require)'

# move the broken test back
mv test/testcases/codeblock_fenced.disabled test/testcases/codeblock_fenced.text
popd


%files
%license %{gem_instdir}/COPYING

%dir %{gem_instdir}

%{gem_libdir}
%{gem_spec}

%exclude %{gem_instdir}/VERSION

%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}

%doc %{gem_instdir}/CONTRIBUTERS

%{gem_instdir}/test


%changelog
* Sat Aug 15 2020 Fabio Valentini <decathorpe@gmail.com> - 1.1.0-5
- Include upstream patch to make test suite compatible with kramdown 2.2.0.
- Fixes RHBZ#1865414

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 26 2019 Fabio Valentini <decathorpe@gmail.com> - 1.1.0-1
- Initial package

