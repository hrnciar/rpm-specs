# Generated by go2rpm 1
%bcond_without check

# https://github.com/evanw/esbuild
%global goipath         github.com/evanw/esbuild
Version:                0.7.1

%gometa

%global common_description %{expand:
This is a JavaScript bundler and minifier. It packages up JavaScript and
TypeScript code for distribution on the web.}

%global golicenses      LICENSE.md
%global godocs          docs CHANGELOG.md README.md version.txt

Name:           %{goname}
Release:        1%{?dist}
Summary:        Fast JavaScript bundler and minifier

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/sys/unix)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/kylelemons/godebug/diff)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE.md
%doc docs CHANGELOG.md README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Mon Aug 24 15:12:26 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.7.1-1
- Initial package
