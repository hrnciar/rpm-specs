Name:       js-jquery-jqplot
Version:    1.0.9
Release:    5%{?dist}
Summary:    Pure JavaScript plotting plugin for jQuery
License:    MIT or GPLv2
URL:        http://www.jqplot.com/
Source0:    https://github.com/jqPlot/jqPlot/archive/%{version}/jqplot-%{version}.tar.gz
BuildArch:  noarch

BuildRequires:  web-assets-devel
BuildRequires:  nodejs-packaging
BuildRequires:  npm(grunt)
BuildRequires:  npm(grunt-contrib-clean)
# Review request : https://bugzilla.redhat.com/show_bug.cgi?id=1378423
#BuildRequires:  npm(grunt-contrib-compress)
BuildRequires:  npm(grunt-contrib-concat)
BuildRequires:  npm(grunt-contrib-copy)
BuildRequires:  npm(grunt-contrib-cssmin)
BuildRequires:  npm(grunt-contrib-uglify)
# Not available
#BuildRequires:  npm(grunt-git-revision)
#BuildRequires:  npm(grunt-jslint)
#BuildRequires:  npm(grunt-natural-docs)

Requires:  web-assets-filesystem
Requires:  js-jquery >= 1.4


%description
jqPlot is a plotting and charting plugin for the jQuery Javascript framework.
jqPlot produces beautiful line, bar and pie charts with many features:
- Numerous chart style options.
- Date axes with customizable formatting.
- Up to 9 Y axes.
- Rotated axis text.
- Automatic trend line computation.
- Tooltips and data point highlighting.
- Sensible defaults for ease of use.


%prep
%setup -q -n jqPlot-%{version}
find examples -type f -exec chmod a-x {} \;


%build
%nodejs_symlink_deps --build
# For some reason, the plugins are not minified if running all the tasks at once
# See :
#   https://github.com/jqPlot/jqPlot/issues/66
#   https://github.com/jqPlot/jqPlot/issues/88
grunt --verbose clean copy:build copy:build_examples clean:examples copy:dist copy:dist_examples copy:dist_docs
grunt --verbose uglify cssmin


%install
mkdir -p %{buildroot}%{_jsdir}/jquery-jqplot/
cp -p dist/jquery.jqplot*.js %{buildroot}%{_jsdir}/jquery-jqplot/
cp -p dist/jquery.jqplot*.css %{buildroot}%{_jsdir}/jquery-jqplot/
cp -p dist/plugins/*.js %{buildroot}%{_jsdir}/jquery-jqplot/


%files
%license dist/gpl-2.0.txt dist/MIT-LICENSE.txt 
%doc dist/README.md dist/copyright.txt
%doc dist/usage.txt dist/optionsTutorial.txt dist/changes.txt
%doc dist/jqPlotCssStyling.txt dist/jqPlotOptions.txt
%doc dist/examples/
%{_jsdir}/jquery-jqplot/


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Xavier Bachelot <xavier@bachelot.org> - 1.0.9-2
- Bump release.

* Wed Oct 03 2018 Xavier Bachelot <xavier@bachelot.org> - 1.0.9-1
- Initial package.
